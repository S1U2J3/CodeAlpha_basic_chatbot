import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you!",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no need to apologize!",]
    ],
    [
        r"i'm (.*) doing good",
        ["Glad to hear it!", "That's great to hear!"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created to chat with you!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a nice day."]
    ]
]

# Create Chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hello! I am your chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        response = chatbot.respond(user_input)
        print("Bot:", response)
