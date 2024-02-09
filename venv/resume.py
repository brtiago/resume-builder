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
def get_resume(filename):
    prompt = f"""
        aja como um recrutador profissional de TI;
        Leia o seguinte curriculo {filename} 
        """
    response = model.generate_content(prompt)
    return response.text
def get_descricao_vaga(descricao):
    return descricao
def get_palavras_chave(palavras):
    return nnull


resume = get_resume(read_file(input("Digite o caminho completo do currículo pdf: ")))
# descricao_vaga = read_file(input("Digite o caminho completo da descrição da vaga pdf: "))

# palavras_chave = input("Digite as palavras-chave a serem utilizadas para a criação do RESUMO PROFISSIONAL: ")
palavras_chave = """
    desenvolvedor java, java EE, JSF 2, desenvolvimento e manutenção, SQL, dados oracle, tecnologias, 
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
def criar_curriculo(cargo, descricao, resume):
    prompt = f"""
    Crie um currículo para a posição de {cargo} com base na seguinte descrição de trabalho {descricao} destacando as habilidades, 
    experiências e qualificações mais relevantes do {resume} para esta oportunidade, o resultado deve me destacar como o candidato ideal para 
    esta posição e impressionar os recrutadores.
    
    
    ### EXEMPLO
    JOÃO DA SILVA
    Fortaleza/CE
    (85) 98770-0088 
    tgribeiro@gmail.com 
    https://www.linkedin.com/in/tgribeiro 
    https://github.com/brtiago

    OBJETIVO
    Desenvolvedor Java Jr

    RESUMO PROFISSIONAL
    Desenvolvedor Java com mais de 13 anos de experiência na área de suporte técnico e redes, em transição de carreira para a área de desenvolvimento.

    FORMAÇÃO ACADÊMICA
    Bacharelado em Ciência da Computação (Faculdade Integrada da Grande Fortaleza)

    EXPERIÊNCIA PROFISSIONAL 
    LUMUS TECH
    Desenvolvedor Java
    jun/2023 até atual
    ● Desenvolvi APIs REST em Java 17, Hibernate, JPA, Spring Boot e banco de dados PostgreSQL
    ● Utilizei minhas habilidades em GPT, Python e Angular 17 para criar ferramentas e desenvolver um CRUD completo, aplicando boas práticas de programação e refatoração de código.
    ● Atuei na criação e manutenção de APIs REST em Java 17, utilizando Spring Boot 3 e JPA para desenvolver e otimizar consultas avançadas, lidar com persistência de dados e garantir a documentação, teste e segurança das APIs.
    ● Apliquei os princípios SOLID com Java para desenvolver soluções robustas e escaláveis, garantindo a qualidade do código e a aderência aos padrões de projeto estabelecidos.
    ● Implementei testes automatizados em Java, utilizando boas práticas de programação para garantir a qualidade e a integridade do software, especialmente em APIs desenvolvidas com Spring Boot.

    AVON COSMÉTICOS 
    Analista de Redes Pleno 
    fev/2012 até jan/2017 
    Analista de Redes Jr
    out/2007 a fev/2012
    ● Instalação, configuração e administração de Windows Server e de softwares para PCs e Notebooks;
    ● Instalação e configuração de roteadores, switches e outros ativos de rede da marca Cisco;
    ● Administração de antivírus corporativo, firewall, DHCP e DNS;
    ● Administração da central de telefonia Definity One (Avaya) e do servidor de e-mail corporativo Lotus Notes;
    ● Treinamentos e workshops para colaboradores com temas ligados à tecnologia da informação;
    Principais resultados:
    ● Aprimorei a qualidade da rede do centro de distribuição da Avon Cosméticos alcançando a disponibilidade de 99,81% através de controle de tráfego e monitoramento contínuo com BMC Remedy ITSM e Cacti
    ● Elaborei novos procedimentos para realização, registro e recuperação de dados de backups garantindo que os dados fossem gravados em fitas e estas armazenadas em empresas externas
    ● Planejei manutenção, instalação e administração de servidores viabilizando assim o acesso de 300 usuários à rede

    IDIOMAS
    ● Inglês - Fluente

    FORMAÇÃO COMPLEMENTAR
    ● GPT e Python: criando ferramentas com a API (Alura) - 10h;
    ● Angular 14: aplique os conceitos e desenvolva seu primeiro CRUD (Alura) - 10h;
    ● Java: consumindo API, gravando arquivos e lidando com erros (Alura) - 10h;
    ● Boas práticas de programação: melhore o código de uma API Java (Alura) - 10h;
    ● Java e refatoração: melhorando códigos com boas práticas (Curso Alpha) - 10h;
    ● Spring Boot 3: desenvolva uma API Rest em Java (Alura) - 10h;
    ● Java e JPA: consultas avançadas, performance e modelos complexos (Alura) - 10h;
    ● Persistência com JPA: Hibernate (Alura) - 8h;
    ● Java e JDBC: trabalhando com um banco de dados (Alura) - 10h;
    ● Design Patterns em Java I: boas práticas de programação (Alura) - 8h;
    ● Spring Boot 3: documente, teste e prepare uma API para o deploy (Alura) - 10h;
    ● SOLID com Java: princípios da programação orientada a objetos (Alura) - 10h;
    ● Spring Boot 3: aplique boas práticas e proteja uma API Rest (Alura) - 10h;
    ● Boas práticas de programação: automatizando testes com Java (Alura) - 10h;
    ● Responsive Web Design Certification (freeCodeCamp) - 300h
        
    """
    response = model.generate_content(prompt)
    return response.text

print(set_linkedin_about(resume))