import openai

# Replace 'your-api-key' with your actual OpenAI API key
OPENAI_API_KEY = "your-api-key"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        api_key=OPENAI_API_KEY
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("Simple ChatGPT Bot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chat_with_gpt(user_input)
        print(f"ChatGPT: {response}")
