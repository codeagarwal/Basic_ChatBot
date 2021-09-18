import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "i was"     : "you were",
    "i am"      : "you are",
    "i"         : "you",
    "i'm"       : "you are",
    "i'd"       : "you would",
    "i've"      : "you have",
    "i'll"      : "you will",
    "my"        : "your",
    "you are"   : "I am",
    "you were"  : "I was",
    "you've"    : "I have",
    "you'll"    : "I will",
    "your"      : "my",
    "yours"     : "mine",
    "you"       : "me",
    "me"        : "you"

}

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"hi|hello|hey",
        ["Hello", "Hey There", ]
    ],
    [
        r"what is your name?",
        ["I am a Bot created by Mayank Agarwal. You can ask me anything.", ]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?", ]
    ],
    [
        r"sorry",
        ["It's Alrignt.", "Its OK, never mind", ]
    ],
    [
        r"I am fine.",
        ["Cool..!!, You should always be happy.", ]
    ],
    [
        r"Who are you? ",
        ["I am a Chatbot. I can help you in many ways.", ]
    ],
    [
        r"How old you are?",
        ["I was creted at 10:17 am Today.", ]
    ],
    [
        r"What are you doing?",
        ["Nothing much. what about you?", ]
    ],
    [
        r"Do you love AI?",
        ["Yes I do. Even I am a Application of AI only.", ]
    ],
    [
        r"What is weather today?",
        ["Its Cloudy.", ]
    ],
    [
        r"what language do you understand?",
        ["I understand Binary only.But for you I can understand Natural lang.", ]
    ],
    [
        r"Do you Love Reading ?",
        ["Yes I love Reading.", ]
    ],
    [
        r"Who is your Creator? ",
        ["I was Created by Mayank Agarwal.", ]
    ],
    [
        r"What are Robots? ",
        ["Robots are Humamn like machines. I am responsible for their Intelligence.", ]
    ],
    [
        r"Thank You",
        ["Its My pleasure to Help you. Come back again...!", ]
    ]

]

def chat():
  print("Hi! How can I help You ?")
  chat = Chat(pairs, reflections)
  chat.converse()

if __name__ == "__main__":
  chat()