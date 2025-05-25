import random
from nltk.tokenize import word_tokenize

responses = {
    'hello': ['Hi there!', 'Hello!', 'Hey!'],
    'how are you': ['I’m doing great, thanks!', 'All good! What about you?'],
    'bye': ['Goodbye!', 'See you later!', 'Bye! Have a nice day!'],
    'name': ['I am CodeAlphaBot!', 'Just call me Bot!'],
    'default': ['Sorry, I didn’t understand that.', 'Can you say that again?']
}

def get_response(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses['default'])

print(" CodeAlpha Chatbot: Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if 'bye' in user_input.lower():
        print("Bot:", random.choice(responses['bye']))
        break
    response = get_response(user_input)
    print("Bot:", response)
