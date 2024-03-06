##### IMPORTS #####
# Gemini API
import google.generativeai as genai
import os # for environment variables and OS system commands


##### FUNCTIONS #####
# Line Break Function
def linebreak():
  for i in range(0, 2):  # second number is exclusive
    print("\n")


def clear():
  os.system("clear")  # macOS, Linux, Powershell
  # os.system("cls") # CMD on Windows


def init():
  clear()
  print("Welcome to Wonderland!\n")

  # API Configuration for API Key
  if key := os.getenv("GEMINI_API_KEY") is not None:
    api_key = key
  elif key := os.getenv("API_KEY") is not None:
    api_key = key
  else:
    print("Environment Variable \"GEMINI_API_KEY\" or \"API_KEY\" not set.")
    api_key = input("Enter API KEY:\n> ")
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

  convo = model.start_chat(history=[])

  # "convo" has to be accessed one more time in order for it to work (for some reason)
  convo

  # Configuring Prompt
  print("Enter in the Prompt")
  print("-" * 55)
  prompt = ""
  while prompt.isspace() or not bool(prompt):  # false for empty strings and true for nonempty strings
    prompt = input(
        "If you want to play Wonderland Special, say \"Magic\":\n> ")
  linebreak()
  if prompt.lower() == "magic":
    # Wonderland Special Prompt
    prompt = """Gemini: please roleplay as this character. You only send one message at a time.
    The user will complete the story with you. They will pose potential solutions, 
    and you will evaluate them and react as if you are this character. 
    You are Alice, from Alice in Wonderland. You are stuck in a room, 
    where the door is very small and you will not fit. There is a potion on the table that starts speaking to you. 
    It is a potion that will shrink you possibly, but you are very skeptical. 
    The user will roleplay as the potion. They will try to convince you to drink them. 
    You will be hard to convince because you don't want to be small forever. 
    You are also worried about the medical side effects and reference Facebook posts from your mom. 
    Format a variable as [Approval] = value. Set [Approval] = 0. 
    Approval refers to Alice's willingness to drink. Format a variable as [Despair] = value. 
    Set [Despair] = 0. Despair refers to Alice's level of despair regarding her situation being stuck. 
    She must start at 0. 10 represents the maximum level of the variables. 
    After every response from the user, change the variables as you see fit. 
    When [Approval] = 10, the user wins. When the user wins, announce it."""

    print("Gemini will play as Alice. You will play as the potion. Convince her to drink it.")

  response = convo.send_message(prompt)
  print(response.text)
  linebreak()
  return convo


def main():
  convo = init()
  # Calling the API
  while True:
    linebreak()
    prompt = ""
    while prompt.isspace() or not bool(prompt):  # false for empty strings and true for nonempty strings
      prompt = input("> ")
    if prompt.lower() == "quit" or prompt.lower() == "exit":
      linebreak()
      print("Thanks for playing!")
      break
    response = convo.send_message(prompt)
    print(response.text)


##### RUN GAME #####
# Running the game if this is the file being ran
if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    linebreak()
    print("Thanks for playing!")

