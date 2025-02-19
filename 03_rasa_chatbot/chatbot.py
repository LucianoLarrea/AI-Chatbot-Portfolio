from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Cargar modelo ajustado
MODEL_PATH = "./custom_gpt_model"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

def chat_with_gpt(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    print("Fine-Tuned GPT Chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chat_with_gpt(user_input)
        print(f"Chatbot: {response}")
