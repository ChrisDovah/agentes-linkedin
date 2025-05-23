# -*- coding: utf-8 -*-
"""Cópia de Imersão IA Alura + Google Gemini - Aula 05 - Agentes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ApO2xS2YU0Bw5qB5FWBLOSNcZHZnRl31
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip -q install google-genai
# %pip install -q google-adk

# Configura a API Key do Google Gemini

import os
from google.colab import userdata
from IPython.display import HTML, Markdown

os.environ["GOOGLE_API_KEY"] = userdata.get('GOOGLE_API_KEY')

# Configura o cliente da SDK do Gemini

from google import genai

client = genai.Client()

MODEL_ID = "gemini-2.0-flash"

from google.adk.agents import Agent # Importa a classe Agent do módulo
from google.adk.runners import Runner # Importa a classe Runner do módulo
from google.adk.sessions import InMemorySessionService #mporta o InMemorySessionService de google.adk.sessions
from google.adk.tools import google_search
from google.genai import types  # Para criar conteúdos (Content e Part)
from datetime import date
import textwrap # Para formatar melhor a saída de texto
from IPython.display import display, Markdown # Para exibir texto formatado no Colab
import requests # Para fazer requisições HTTP
import warnings

warnings.filterwarnings("ignore")

# Função auxiliar que envia uma mensagem para um agente via Runner e retorna a resposta final
def call_agent(agent: Agent, message_text: str) -> str:
    # Cria um serviço de sessão em memória
    session_service = InMemorySessionService()
    # Cria uma nova sessão (você pode personalizar os IDs conforme necessário)
    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    # Cria um Runner para o agente
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    # Cria o conteúdo da mensagem de entrada
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    # Itera assincronamente pelos eventos retornados durante a execução do agente
    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
          for part in event.content.parts:
            if part.text is not None:
              final_response += part.text
              final_response += "\n"
    return final_response

# Função auxiliar para exibir texto formatado em Markdown no Colab
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

##########################################
# --- Agente 1: Buscador de Vagas --- #
##########################################
def agente_buscador(topico, data_de_hoje):
    buscador = Agent(
        name="agente_buscador",
        model="gemini-2.0-flash",
        description="Agente buscador de notícias no Google",
        tools=[google_search],
        instruction= """
        Você é um assistente de pesquisa. A sua tarefa é usar a ferramenta de buscas do Google (google_search)
        para recuperar as vagas de emprego em Manaus.
        Foque em no máximo de 5 lançamentos relevantes e dê prioridade ao site Indeed
        """
    )
    entrada_do_agente_buscador= f"Tópico: {topico}\nData de hoje: {data_de_hoje}"
        # Executa o agente
    lancamentos_buscados = call_agent(buscador, entrada_do_agente_buscador)
    return lancamentos_buscados

def agente_planejador(topico, lancamentos_buscados):
    planejador = Agent(
        name="agente_planejador",
        model="gemini-2.0-flash",
        # Inserir as instruções do Agente Planejador #################################################
        instruction="""
        Você é um planejador de conteúdo, especialista em redes sociais. Com base na lista de
        lançamentos mais recentes e relevantes buscados, você deve:
        Usar a ferramenta de busca do Google (google_search) para criar um plano sobre
        quais são os pontos mais relevantes que poderíamos abordar em um post sobre cada um deles.
        Você também pode usar o Google (google_search) para pesquisar mais detalhes sobre os temas e aprofundar.
        Indique pelo menos 2 cursos do catálogo da empresa como sugestões para o post.
        Ao final, você irá escolher o tema mais relevante entre todos eles com base nas suas pesquisas e
        retornar esse tema, seus pontos mais relevantes, e um plano com os assuntos a serem abordados no post que será escrito posteriormente
        Catálogo:
        Curso de TBO (Treinamento Básico Operacional)
NR 12 - Máquinas e Equipamentos
Leitura de Componentes
Técnicas de Soldagem Eletrônica
Curso de 5s
Curso de 8s
Curso de 10s
Metrologia Industrial
ESD - Descarga Eletrostática
Almoxarifado
Inspetor da Qualidade
Operador de Produção
Operador de SMD
Ferramentas da Qualidade
ISO 9001
Auxiliar de Produção
Gestão da Qualidade
Operador de Máquina Injetora
Leitura e Interpret. Desenho Técnico
Matemática Aplicada
Analista de Produção
Gestão da Produção
Lean Manufacturing
Seis Sigma
FMEA
MASP
PDCA
Metodologia 8D
Engenharia de Tempos e Métodos
SAP


        """,
        description="Agente que planeja posts",
        tools=[google_search]
    )

    entrada_do_agente_planejador = f"Tópico:{topico}\nLançamentos buscados: {lancamentos_buscados}"
    # Executa o agente
    plano_do_post = call_agent(planejador, entrada_do_agente_planejador)
    return plano_do_post

######################################
# --- Agente 3: Redator do Post --- #
######################################
def agente_redator(topico, plano_de_post):
    redator = Agent(
        name="agente_redator",
        model="gemini-2.0-flash",
        instruction="""
            Você é um Redator Criativo especializado em criar posts para redes sociais com foco em Vendas.
            Você escreve posts para a empresa Capacita Manaus, uma escola que oferece cursos online
            e presenciais na área da Indústria, localizada em Manaus.
            Utilize o tema fornecido no plano de post e os pontos mais relevantes fornecidos e, com base nisso,
            escreva um rascunho de post para Linkedin sobre o tema indicado.
            Você deve relacionar as vagas de emprego com os cursos oferecidos pela empresa.
            O post deve ser engajador, informativo, com linguagem simples e incluir 2 a 4 hashtags no final.
            """,
        description="Agente redator de posts engajadores para Linkedin"
    )
    entrada_do_agente_redator = f"Tópico: {topico}\nPlano de post: {plano_de_post}"
    # Executa o agente
    rascunho = call_agent(redator, entrada_do_agente_redator)
    return rascunho

##########################################
# --- Agente 4: Revisor de Qualidade --- #
##########################################
def agente_revisor(topico, rascunho_gerado):
    revisor = Agent(
        name="agente_revisor",
        model="gemini-2.0-flash",
        instruction="""
            Você é um Editor e Revisor de Conteúdo meticuloso, especializado em posts para redes sociais, com foco no Linkedin.
            O público alvo possui entre 18 e 50 anos, use um tom de escrita adequado.
            Revise o rascunho de post de Linkedin abaixo sobre o tópico indicado, verificando clareza, concisão, correção e tom.
            Lembre-se que estabelecer o gancho entre as vagas de emprego e os cursos é muito importante.
            Se o rascunho estiver bom, responda apenas 'O rascunho está ótimo e pronto para publicar!'.
            Caso haja problemas, aponte-os e sugira melhorias.
            """,
        description="Agente revisor de post para redes sociais."
    )
    entrada_do_agente_revisor = f"Tópico: {topico}\nRascunho: {rascunho_gerado}"
    # Executa o agente
    texto_revisado = call_agent(revisor, entrada_do_agente_revisor)
    return texto_revisado

data_de_hoje = date.today().strftime("%d/%m/%Y")

print("🚀 Iniciando o Sistema de Criação de Posts para Linkedin com 4 Agentes 🚀")

# --- Obter o Tópico do Usuário ---
topico = input("❓ Por favor, digite o TÓPICO sobre o qual você quer criar o post de tendências: ")

# Inserir lógica do sistema de agentes ################################################
if not topico:
  print("Você esqueceu de digitar um tópico!.")
else:
  print(f"Maravilha! Vamos então pesquisar as notícias mais recentes sobre o tópico: {topico}")
  lancamentos_buscados = agente_buscador(topico, data_de_hoje)
  print("\n--- Resultados da Busca ---")
  display(to_markdown(lancamentos_buscados))
  print("--------------------------------------------------------------------")

  plano_de_post = agente_planejador(topico, lancamentos_buscados)
  print("\n--- Resultados do Planejamento ---")
  display(to_markdown(plano_de_post))
  print("--------------------------------------------------------------------")

  rascunho_de_post = agente_redator(topico, plano_de_post)
  print("\n--- Resultados do Rascunho ---")
  display(to_markdown(rascunho_de_post))
  print("--------------------------------------------------------------------")

  post_final = agente_revisor(topico, rascunho_de_post)
  print("\n--- Resultados do Post Final ---")
  display(to_markdown(post_final))
  print("--------------------------------------------------------------------")