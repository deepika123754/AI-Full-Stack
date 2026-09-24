import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"Defination of AI and the 3 mains tyoes of ai in bullet points "
        }
            ]
)
print(response["message"]["content"])
