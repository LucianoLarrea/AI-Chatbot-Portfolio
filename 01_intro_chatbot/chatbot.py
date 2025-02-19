from openai import OpenAI

# Configurar el cliente de OpenAI
client = OpenAI(api_key="your-api-key")

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Simple ChatGPT Bot. Escribe 'salir' para terminar.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "exit":
            break
        response = chat_with_gpt(user_input)
        print(f"ChatGPT: {response}")
