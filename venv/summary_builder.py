import os
import dotenv
import google.generativeai as genai

dotenv.load_dotenv()


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)


# Set up the model
#generation_config = {
#  "temperature": 0.9,
#  "top_p": 1,
#  "top_k": 1,
#  "max_output_tokens": 256,
#    "stop_sequences": [
#        "6",
#    ]
#}

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

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  "você é uma analista senior de RH. Escreva um sumario para curriculo com base nos requisitos de cargo que enviarei abaixo: ",
]

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": "você é uma analista senior de RH. Escreva um sumario para curriculo com base nos requisitos de cargo que enviarei abaixo:"
  },
  {
    "role": "model",
    "parts": "Object-Oriented Programming, SQL/NoSQL, Bug Fixing &amp; Troubleshooting, Front-End Integration, JUnit Test Case Development, Leadership Skills, Team Player"
  }
])

convo.send_message("Analista Java Pleno")

print(convo.last.text)