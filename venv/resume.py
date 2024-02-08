import os
import dotenv
import google.generativeai as genai

from file import read_file

dotenv.load_dotenv()

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

generation_config = {
    "temperature": 0.35,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name = "gemini-pro",
                              generation_config = generation_config,
                              safety_settings = safety_settings)

resume = read_file(input("Digite o caminho completo do currículo pdf: "))
descricao_vaga = read_file(input("Digite o caminho completo da descrição da vaga pdf: "))

palavras_chave = input("Digite as palavras-chave a serem utilizadas para a criação do RESUMO PROFISSIONAL: ")
palavras_chave = """desenvolvedor java, java EE, JSF 2, desenvolvimento e manutenção, SQL, dados oracle, tecnologias, 
desenvolvimento de aplicações, MVC, utilizando, EJB, JSP, web, hibernate, spring, JPA, 
desenvolvimento de sistemas, banco de dados """

def listar_habilidades_tecnicas_vaga(cargo, description):
    prompt = f"""Baseado nesta descrição de vaga de emprego: {description}, crie uma lista das principais habilidades técnicas e conhecimentos
    necessários para ser um {cargo} na área mencionada. Não escreva a descrição das tecnologias.
    Evite postar conteúdos diferentes de habilidades técnicas e conhecimentos necessários"

    ### Exemplo:
Habilidades técnicas:
Experiência de pelo menos 3 anos em desenvolvimento Java;
Desenvolvimento WEB (javascript, HTML/CSS);
Banco de Dados Relacional e SQL;
IDE Intellij ou eclipse;
Gerenciador de dependências Maven;
Framework Spring Boot ou JEE;
Versionamento de código GIT;
Experiência em Metodologias Ágeis (scrum ou kanban).

Conhecimentos:
Modelagem de dados e Design de soluções;
Framework Javascript Angular
Arquiteturas modernas baseadas em microserviços e APIs (REST);
Pipelines de CI/CD com Jenkins e Maven;
Containers (Kubernetes/Docker;
Sonar;
Nexus;
Banco de Dados Oracle.
    """

    response = model.generate_content(prompt)
    return response.text

def set_linkedin_about(resume):
    perguntas = """
        Quem você é?
        O que você faz?
        O que você fez?
        O que te faz especial?
        """
    prompt = f"""
    aja como um recrutador profissional de TI;
    avalie este {resume} e procure por informações sobre os empregos anteriores dos candidato, cargos ocupados, responsabilidades e duração de cada experiência;
    Escreva um resumo profissional usando experiências profissionais obtidas para responder as {perguntas}:
    
    cada parágrafo deve ter 3 linhas; 
    não imprima as {perguntas} no texto;
    """
    response = model.generate_content(prompt)
    return response.text

def get_resume(resume):
    return resume

def get_descricao_vaga(descricao):
    return descricao

def get_compatibilidade_vaga(resume, descricao_vaga):
    prompt = f"""
    aja como um recrutador profissional de TI;
    avalie o seguinte {resume} e procure por informações sobre os empregos anteriores dos candidato, cargos ocupados, responsabilidades e duração de cada experiência;
    informe o se nível de expertise do candidato é compativel com a {descricao_vaga};
    """
    response = model.generate_content(prompt)
    return response.text

def create_resumo_profissional(resume, keywords):
    perguntas = """
    Quem você é?
    O que você faz?
    O que você fez?
    O que te faz especial?
    """
    prompt = f"""
    Aja como um recrutador profissional de TI;
    avalie o seguinte {resume} e procure por informações sobre os empregos anteriores dos candidato, cargos ocupados, responsabilidades e duração de cada experiência;
    Escreva um resumo profissional 6 linhas em primeira pessoa usando obrigatoriamente as {keywords} e respondendo as {perguntas}
    
    """
    response = model.generate_content(prompt)
    print("\nGerando resumo...")
    return response.text

def get_competencias(resume):
    prompt = f"""
    aja como um recrutador profissional de TI;
    Leia o {resume} abaixo e com base na FORMAÇÃO COMPLEMENTAR e no RESUMO PROFISSIONAL me informe a lista de competências.
    ### EXEMPLO
            
    Competências:
    - Linux
    - MySQL
    - PostgreSQL
    - SQL
    
    """
    response = model.generate_content(prompt)
    return response.text

print(get_competencias(resume))