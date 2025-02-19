from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset

# Cargar dataset (Ejemplo: dataset de diálogos)
dataset = load_dataset("daily_dialog")

# Tokenizador y modelo base
MODEL_NAME = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Tokenizar datos
def tokenize_function(examples):
    return tokenizer(examples["dialog"], truncation=True, padding="max_length", max_length=128)

tokenized_datasets = dataset.map(tokenize_function, batched=True)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Configurar entrenamiento
training_args = TrainingArguments(
    output_dir="./gpt_model",
    evaluation_strategy="epoch",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    save_steps=500,
    save_total_limit=2,
    logging_dir="./logs",
)

# Iniciar entrenamiento
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    tokenizer=tokenizer,
    data_collator=data_collator,
)

trainer.train()
model.save_pretrained("./custom_gpt_model")
tokenizer.save_pretrained("./custom_gpt_model")
