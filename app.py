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


# API Configuration for API Key
api_key=input(">")
genai.configure(api_key=api_key)

# Set up the model with certain parameters
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
  prompt = "Gemini: please roleplay as this character. You only send one message at a time. The user will complete the story with you. They will pose potential solutions, and you will evaluate them and react as if you are this character. You are Alice, from Alice in Wonderland. You are stuck in a room, where the door is very small and you will not fit. There is a potion on the table that starts speaking to you. It is a potion that will shrink you possibility, but you are very skeptical. The user will roleplay as the potion. They will try to convince you to drink them. You will be hard to convince, because you don't want to be small forever. You are also worried about the medical side affects, and reference Facebook posts from your mom. Format a variable as [Approval] = value. Set [Approval] = 0. Approval refers to Alice willingness to drink. Format a variable as [Despair] = value. Set [Despair] = 0. Despair refers to Alice's level of despair regarding her situation being stuck. She must start at 0. 10 represents the maximum level of the variables. After every response from the user, change the variables as you see fit. When [Approval] = 10, the user wins.  When user wins announce it."
  print("Gemini will play as Alice. You will play as the potion. Convince her to drink it.")
response = convo.send_message(prompt)
print(response.text)
linebreak()

# Calling API
while True:
  linebreak()
  response = convo.send_message(input(">"))
  print(response.text)
  
