import openai

openai.api_key="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"

def chat_gpt(prompt):
    reponse = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
        
    )
    return reponse.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input ("Jn: ")
        if user_input.lower() is ["quit","bye","88","thx"]:
            break

        response = chat_gpt(user_input)
        print("MyBot: ",response)

        
