

'''
Using OpenAI

OpenAI doc: https://github.com/openai/openai-python
'''

# from openai import OpenAI

# openai_key = "openai_key"

# messages = []

# client = OpenAI(
#     api_key = openai_key,
# )

# def completion(message):
#     global messages
#     messages.append(
#             {
#                 "role": "user",
#                 "content": message,
#             }
#         )
#     chat_completion = client.chat.completions.create(
#         messages = messages,
#         model = "gpt-4o",
#     )
#     # print(chat_completion)
#     message = {
#         "role": "assistant",
#         "content": chat_completion.choices[0].message.content
#     }
#     messages.append(message)
#     print(f"Bot: {message["content"]}")

# if __name__ == "__main__":
#     print("Bot: How may I help you?\n")
#     while True:
#         user_question = input()
#         print(f"User: {user_question}")
#         completion(user_question)


import os
from openai import OpenAI

class ChatBot:
    def __init__(self, model: str = "gpt-4o"):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY environment variable not set")

        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.messages = []

    def chat(self, user_input: str) -> None:
        self.messages.append({
            "role": "user",
            "content": user_input,
        })

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
            )
        except Exception as e:
            print(f"Bot: ⚠️ Error: {e}")
            return

        assistant_message = response.choices[0].message.content
        self.messages.append({
            "role": "assistant",
            "content": assistant_message,
        })

        print(f"Bot: {assistant_message}")


def main():
    print("Bot: How may I help you?")
    print("(type 'exit' or 'quit' to stop)\n")

    bot = ChatBot()

    while True:
        try:
            user_input = input("User: ").strip()
        except KeyboardInterrupt:
            print("\nBot: Goodbye 👋")
            break

        if user_input.lower() in {"exit", "quit"}:
            print("Bot: Goodbye 👋")
            break

        if not user_input:
            continue

        bot.chat(user_input)


if __name__ == "__main__":
    main()