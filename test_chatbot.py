from chatbot import FAQChatbot


# Create chatbot
chatbot = FAQChatbot("faqs.json")


print("===================================")
print("       CodeAlpha FAQ Chatbot")
print("===================================")

print("\nType 'exit' to stop the chatbot.\n")


while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    answer = chatbot.get_response(question)

    print("Chatbot:", answer)