from transformers import pipeline
generator = pipeline('text-generation', model='openai-community/gpt2')
promt = input("Escribe una frase para que el modelo la complete: ")
result = generator(promt, max_length=50, num_return_sequences=1, pad_token_id=50256)
print(f"{result[0]['generated_text']}")  

