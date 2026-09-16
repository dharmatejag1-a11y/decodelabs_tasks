"""
Project 1: Rule-Based AI Chatbot

A simple rule-based chatbot that responds to predefined user inputs.
Uses if-elif-else logic and runs in a continuous loop until the user exits.
"""

def chatbot_response(user_input):
    """Return a predefined response based on the user's input."""
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."
    elif "your name" in user_input:
        return "I am a Rule-Based AI Chatbot."
    elif "help" in user_input:
        return "Sure! You can ask me about my name, how I am, or say hello."
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that. Please try another question."


def main():
    """Run the chatbot in a continuous conversation loop."""
    print("===================================")
    print("       Rule-Based AI Chatbot       ")
    print("===================================")
    print("Type 'bye', 'exit', or 'quit' to stop the chatbot.")
    print()

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()
