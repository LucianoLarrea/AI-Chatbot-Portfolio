import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load fine-tuned model
model_name = "./custom_gpt_model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Chat loop
print("🤖 Fine-Tuned GPT Chatbot. Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! 👋")
        break

    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200, pad_token_id=tokenizer.eos_token_id)
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Chatbot: {response}")
