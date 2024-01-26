import os
import dotenv
import google.generativeai as genai

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



def get_job_description(cargo, description):
    prompt = f"""
    "Baseado nesta descrição de vaga: {description}, crie uma lista  das principais habilidades técnicas e conhecimentos 
    necessários para ser um {cargo} na área mencionada. Crie também uma lista com as tecnologias ou princípios 
    relacionadas ao {cargo}. Não escreva a descrição das tecnologias. Apenas me informe a lista. Evite postar 
    conteúdos relacionadas a responsabilidades, beneficios e observações"
    """

    response = model.generate_content(prompt)
    return response.text

def set_linkedin_about(resume):
    prompt = f"""
    aja como um recrutador profissional de TI;
    avalie este {resume} e procure por informações sobre os empregos anteriores dos candidato, cargos ocupados, responsabilidades e duração de cada experiência;
    Escreva um resumo profissional usando experiências profissionais obtidas para responder as {perguntas}:
    
    perguntas: '
    Quem você é?
    O que você faz?
    O que você fez?
    O que te faz especial? '
    
    cada parágrafo deve ter 3 linhas; 
    não imprima as perguntas no texto;
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

def create_resumo(resume, keywords):
    prompt = f"""
    Aja como um recrutador profissional de TI;
    avalie o seguinte {resume} e procure por informações sobre os empregos anteriores dos candidato, cargos ocupados, responsabilidades e duração de cada experiência;
    Escreva um resumo profissional 6 linhas em primeira pessoa usando obrigatoriamente as {keywords} e respondendo as {perguntas}
    
    perguntas: '
    Quem você é?
    O que você faz?
    O que você fez?
    O que te faz especial?'
    
    """
    response = model.generate_content(prompt)
    return response.text
