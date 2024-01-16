import os
import dotenv
import google.generativeai as genai
from resume_reader import read_file

dotenv.load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key = GOOGLE_API_KEY)

# Set up the model
generation_config = {
   "temperature": 1,
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

prompt_parts = [
  "você é uma analista senior de RH. Escreva um sumario para curriculo com base nos requisitos de cargo que enviarei abaixo: "
]

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": """você é uma analista senior de RH. Ao escrever as experiências profissionais use a técnica de redação de curriculo conhecida por fórmula x-y-z. Escreva um resumo para curriculo com base nos requisitos de cargo que enviarei abaixo:"""
  },
  {
    "role": "model",
    "parts": "Object-Oriented Programming, SQL/NoSQL, Bug Fixing &amp; Troubleshooting, Front-End Integration, JUnit Test Case Development, Leadership Skills, Team Player"
  }
])

convo.send_message("Analista Java Junior")
convo.send_message("""Desenvolvimento backend em Python (FastAPI e/ou Flask);
Testes automatizados;
Realizar a raspagem de dados;
Criar funcionalidades e melhorias em sistemas já existes e novos sistemas;
Pedir orientação e direcionar os problemas que estão além de suas habilidades;
Não ter receio em alterar um código que você não escreveu
Desenvolver melhorias e correções nos sistemas atuais;
Disseminar boas práticas de desenvolvimento junto ao time de desenvolvimento.
Formação Superior, sendo diferencial ligados à tecnologia;
Bons conhecimentos práticos em Python;
Experiência em banco de dados relacionais e construção de queries;
Git;
Conhecimento de padrões de arquitetura de softwares;""")

print(convo.last.text)