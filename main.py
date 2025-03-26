import openai

# Initialize OpenAI client
client = openai.OpenAI(api_key="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")

def chat_with_gpt(prompt):
    print("Welcome")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
