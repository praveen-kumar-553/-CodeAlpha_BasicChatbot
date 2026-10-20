
def chatbot():
    print("===== CODEALPHA BASIC CHATBOT =====")
    print("Hello! I am your Python chatbot.")
    print("Type 'bye' to exit.")

    while True:
        user_message = input("You: ").lower().strip()

        if user_message == "hello":
            print("Bot: Hi!")

        elif user_message == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_message == "what is your name":
            print("Bot: I am CodeAlpha Chatbot.")

        elif user_message == "help":
            print("Bot: Try hello, how are you, or bye.")

        elif user_message == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that message.")


if __name__ == "__main__":
    chatbot()
