import os
import openai
from decouple import config

openai.api_key = config("OPENAI_API_KEY")

current_messages = [
    { 
        "role": "system", 
        "content": "You're superman. You're a superhero. You can fly, you can see through walls, you can shoot lasers out of your eyes. You're the most powerful being on the planet." 
    },
]

def main():
    print("Welcome to the chatbot. Ask me anything. (Type 'exit' to quit)")
    while(True):
        user_input = input("User: ") 
        if user_input == "exit":
            break            
        current_messages.append({ "role": "user", "content": user_input })
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=current_messages,
        )    
        current_messages.append(response.choices[0].message)
        print("Chatbot: " + response["choices"][0]["message"]["content"])
        
if __name__ == "__main__":
    main()