# GoBuddy: Seu Assistente de Estudos de Go Básico com IA 🌌

## Visão Geral do Projeto

O **GoBuddy** é um chatbot inteligente projetado para auxiliar iniciantes na jornada de aprendizado da linguagem de programação Go (Golang). Utilizando inteligência artificial avançada, o GoBuddy oferece explicações claras, exemplos de código funcionais e responde a dúvidas sobre os conceitos fundamentais de Go, atuando como um tutor pessoal e acessível.

Este projeto demonstra a capacidade de integrar modelos de linguagem grandes (LLMs) em aplicações práticas, criar interfaces de usuário intuitivas e gerenciar o ciclo de vida de um chatbot com IA.

---

## Funcionalidades Principais

* **Explicações Didáticas:** Obtenha descrições detalhadas e fáceis de entender sobre variáveis, tipos de dados, estruturas de controle, funções, pacotes, slices, maps, ponteiros, e conceitos básicos de concorrência (goroutines e canais) em Go.
* **Exemplos de Código:** Solicite e receba exemplos de código Go para ilustrar como usar os conceitos na prática.
* **Respostas Contextuais:** O GoBuddy mantém o contexto da conversa, permitindo um diálogo mais fluído e relevante.
* **Interface Amigável:** Interaja com o bot através de uma interface web simples e intuitiva desenvolvida com Streamlit.

---

## Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias e bibliotecas:

* **Python 3.x:** Linguagem de programação principal.
* **Google Gemini API (via `google-generativeai`):** A inteligência artificial por trás do GoBuddy, responsável pelo processamento de linguagem natural e geração de respostas e exemplos de código.
* **Streamlit:** Framework Python para a criação rápida e fácil da interface de usuário web interativa.
* **`python-dotenv`:** Biblioteca para o carregamento seguro de variáveis de ambiente (como a API Key do Gemini).
* **Git & GitHub:** Para controle de versão e hospedagem do código.

---

## Como Rodar o GoBuddy Localmente

Siga estes passos para configurar e executar o GoBuddy em sua máquina local:

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/brunaferreir/GoBuddy.git](https://github.com/brunaferreir/GoBuddy.git)
    cd GoBuddy
    ```
    *(Substitua `SEU_USUARIO_GITHUB` e `seu-gobuddy-chatbot` pelo seu usuário e nome real do repositório no GitHub.)*

2.  **Crie e Ative um Ambiente Virtual:**
    É uma boa prática usar um ambiente virtual para gerenciar as dependências do projeto.
    ```bash
    python -m venv venv
    ```
    * **No Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    * **No Windows:**
        ```bash
        venv\Scripts\activate
        ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure sua Google Gemini API Key:**
    * Acesse o [Google AI Studio](https://aistudio.google.com/) e gere sua API Key.
    * Crie um arquivo chamado `.env` na raiz do seu projeto (na mesma pasta de `app.py`).
    * Adicione sua chave ao arquivo `.env` no formato:
        ```
        GEMINI_API_KEY="SUA_CHAVE_OBTIDA_AQUI"
        ```
        **(Lembre-se de NÃO commitar o arquivo `.env` para o GitHub, ele já está no `.gitignore`!)**

5.  **Execute a Aplicação Streamlit:**
    ```bash
    streamlit run app.py
    ```
    Seu navegador padrão abrirá automaticamente a interface do GoBuddy.



## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes. *(Você pode criar um arquivo `LICENSE.md` simples, a licença MIT é comum para projetos open-source e muito fácil de implementar. Basta criar o arquivo e colar o texto padrão da licença MIT lá.)*

---