import openai
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.environ["API_KEY"]

def ask_gpt(prompt: str) -> str:
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 100,
        temperature = 0.5,
        frequency_penalty = 0,
        presence_penalty = 0,
    )
    return response.choices[0].text.strip()


def main() -> None:
    print("Welcome to the Chatbot! Type 'quit' to exit.")
    
    ai_role = "You are a helpful software developer assistant."
    
    user_input = ""
    chat_history = f"{ai_role}\n"
    
    with open("chat_history.txt", "w", encoding="utf-8") as file:
        file.write(f"{ai_role}\n\n")
    
    while user_input.lower() != "quit":
        user_input = input("User: ")
        
        if user_input.lower() == "quit":
            break       
        
        prompt = f"{chat_history}User: {user_input}\nAI:"
        response = ask_gpt(prompt)
        print("AI:", response)
        
        chat_history += f"User: {user_input}\nAI: {response}\n" 
        
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open("chat_history.txt", "a", encoding="utf-8") as file:
            file.write(f"{timestamp}\nUser: {user_input}\nAI: {response}\n\n")
        

if __name__ == "__main__":
    main()