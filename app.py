# Import statement for Gemini API
import google.generativeai as genai

# Line Break Function
def linebreak():
  i = 0
  while i <=1:
    print("\n")
    i=i+1

linebreak()
print("Welcome to Wonderland!")
print("Enter API KEY")


# API Configuration
api_key=input()
genai.configure(api_key=api_key)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])
convo

# Configuring Prompt
linebreak()
print("Enter in the Prompt")
print("If you want to play Wonderland Special, say Magic")
prompt = input(">")
linebreak()
if prompt == "Magic":
  prompt = ""
response = convo.send_message(prompt)
print(response.text)
linebreak()

# Calling API
while True:
  response = convo.send_message(input(">"))
  print(response.text)
  linebreak()