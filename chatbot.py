def chatbot():
    print("Hello! I am your chatbot. How can I help you?")
    
    while True:
        user_input = input("You:: ").lower()
        
        if 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hi there! How can I help you?")
        
        elif 'how are you' in user_input:
            print("Chatbot: I'm doing well, thank you! How about you?")
        
        elif 'bye' in user_input or 'goodbye' in user_input:
            print("Chatbot: bye! Have a great day!")
            break
        
        elif 'your name' in user_input:
            print("Chatbot: I am a simple chatbot with no name, but you can call me Chatbot!")
        
        elif 'help' in user_input:
            print("Chatbot: Sure! I can assist you with basic information. Ask me questions like: 'How are you?', 'What is your name?', or 'Goodbye'.")
        
        else:
            print("Chatbot: Sorry, I didn't quite understand that. Can you repeat?")
        
if __name__ == "__main__":
    chatbot()
