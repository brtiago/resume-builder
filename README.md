# Projeto de gerador de _currículo vitae_ utilizando modelo de aprendizado de máquina(LLM) do  Google Gemini Pro
## Objetivo
Este projeto é uma simulação de _Application Tracking System_(ATS) que avalia currículos com base em uma descrição de emprego. Com base nesta descrição 
e no currículo do candidado a ATS identifica quais palavras chave ficaram ausentes e informa o percentual de compatibilidade com a vaga.

## Instalação
Para instalar dependências do projeto que está no GitHub dentro de um ambiente virtual (venv), você pode seguir estes passos:

1. **Clone o repositório do GitHub:**
   Abra um terminal e navegue até o diretório onde você deseja armazenar o projeto. Em seguida, use o comando `git clone` para clonar o repositório. Por exemplo:

   ```bash
   git clone https://github.com/brtiago/resume-builder.git
   ```

2. **Crie e ative o ambiente virtual:**
   Navegue até o diretório do projeto recém-clonado e crie um ambiente virtual com o comando `python -m venv`:

   ```bash
   cd nome-do-repositorio
   python -m venv venv
   ```

   Em seguida, ative o ambiente virtual:

   - No Windows:
     ```bash
     venv\Scripts\activate
     ```

   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   
3. **Instale as dependências:**
   Agora que o ambiente virtual está ativado, use o `pip` para instalar as dependências do projeto. O arquivo `requirements.txt` geralmente lista essas dependências. Execute o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

4. **Desativar o ambiente virtual (opcional):**
   Quando você terminar de trabalhar no projeto, pode desativar o ambiente virtual. Execute o seguinte comando:

   ```bash
   deactivate
   ```

   Isso retorna ao ambiente global do Python.

## Configuração
Crie um arquivo .env dentro da pasta venv com a sua chave api:
```bash
GOOGLE_API_KEY="sua_chave_API"
```

