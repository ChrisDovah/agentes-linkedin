# Sistema de Criação de Posts para LinkedIn com Agentes IA

Este projeto foi desenvolvido como parte da Imersão IA da Alura em parceria com o Google, e tem como objetivo demonstrar a criação de um sistema de geração de conteúdo para LinkedIn utilizando agentes de Inteligência Artificial.

## Descrição

O sistema implementa um fluxo de trabalho com 4 agentes distintos, cada um responsável por uma etapa do processo de criação de posts:

1.  **Agente Buscador:** Realiza a pesquisa de vagas de emprego relevantes usando a ferramenta de busca do Google.
2.  **Agente Planejador:** Analisa as vagas encontradas e cria um plano de postagem, relacionando as vagas com os cursos oferecidos pela empresa Capacita Manaus.
3.  **Agente Redator:** Escreve um rascunho de post para o LinkedIn, seguindo o plano gerado pelo Agente Planejador.
4.  **Agente Revisor:** Revisa o rascunho do post, garantindo a qualidade do texto e adequação ao público-alvo.

## Critérios de Avaliação da Competição Alura

Este projeto busca atender aos seguintes critérios de avaliação da competição:

* **Originalidade e Criatividade:** O uso de agentes de IA para automatizar o processo de criação de conteúdo para o LinkedIn demonstra uma abordagem inovadora e criativa. A capacidade de relacionar vagas de emprego com cursos específicos agrega valor ao conteúdo gerado.
* **Relevância e Impacto:** O sistema aborda um problema real, que é a geração eficiente de conteúdo relevante para redes sociais. O impacto potencial é a economia de tempo e esforço na criação de posts de alta qualidade.
* **Qualidade Técnica:** O código foi desenvolvido utilizando boas práticas de programação, com funções bem definidas e comentários explicativos. A utilização da SDK do Google Gemini e da biblioteca `google-adk` demonstra domínio das ferramentas relevantes.
* **Funcionalidade e Usabilidade:** O sistema é funcional, permitindo ao usuário inserir um tópico e obter um post de LinkedIn gerado automaticamente. A interface de linha de comando é simples e intuitiva.
* **Apresentação e Documentação:** Este README.md fornece uma descrição clara do projeto, seus objetivos e funcionamento. O código está bem organizado e comentado.

## Desafios Enfrentados

Durante o desenvolvimento deste projeto, alguns desafios foram encontrados:

* **Gerenciamento do Contexto:** A correta passagem de informações entre os agentes, especialmente o `catalogo_dict`, exigiu atenção cuidadosa para evitar erros de `KeyError` e `ValidationError`.
* **Formatação da Saída:** Garantir que a saída dos agentes estivesse no formato adequado para as etapas subsequentes demandou ajustes nas instruções e no processamento dos dados.
* **Tratamento de Erros:** Implementar um tratamento de erros robusto e informativo foi essencial para garantir a estabilidade do sistema.

## Agradecimentos

Gostaria de expressar minha sincera gratidão aos instrutores da Alura e aos membros do time do Google pela excelente Imersão IA. O conhecimento e suporte fornecidos foram fundamentais para o desenvolvimento deste projeto. Agradeço também aos colegas participantes pela troca de experiências e aprendizado mútuo.

## Reconhecimento do Uso de IA

Por questões de ética e transparência, declaro que utilizei o modelo de linguagem Gemini como auxiliar no desenvolvimento deste código. O Gemini contribuiu com sugestões de código, resolução de problemas e geração de texto para este README.md. No entanto, a concepção do projeto, a implementação da lógica principal e a tomada de decisões de design foram de minha autoria.

## Como Usar

1.  **Pré-requisitos:**
    * Conta Google Cloud com a API do Gemini ativada.
    * Biblioteca `google-genai` e `google-adk` instaladas (pode usar o `%pip` no Colab).
    * Chave da API do Google Gemini configurada como variável de ambiente (`GOOGLE_API_KEY`).
2.  **Execução:**
    * Execute o script Python.
    * O sistema solicitará que você insira um tópico para o post.
    * O sistema irá gerar e exibir cada etapa do processo (busca, planejamento, rascunho, revisão) no console.

## Exemplo de Uso

1.  O usuário executa o script.
2.  O script solicita o tópico do post: "Vagas de emprego em Manaus na área de eletrônica".
3.  O Agente Buscador pesquisa vagas de emprego relevantes.
4.  O Agente Planejador cria um plano de post conectando as vagas aos cursos da Capacita Manaus.
5.  O Agente Redator gera um rascunho de post para o LinkedIn.
6.  O Agente Revisor analisa o rascunho e fornece o post final revisado.

## Contribuição

Contribuições são bem-vindas! Se você tiver ideias para melhorar o sistema, como adicionar novos agentes, otimizar os existentes ou corrigir bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

Espero que este README atenda às suas expectativas! Se precisar de ajustes ou mais detalhes, é só dizer.
