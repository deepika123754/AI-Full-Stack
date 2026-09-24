import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"Give me the answer for 5 to 6 years old child in 2-3 lines only"
        },
        {
            "role":"user",
            "content":" Explain ML"
        }
            ]
)
print(response["message"]["content"])
