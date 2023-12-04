import nltk

# reflections sirve para escribir las respuestas a determinadas preguntas
from nltk.chat.util import Chat, reflections
pares = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, como estas ?",]
    ],
     [
        r"cual es tu nombre ?",
        ["Mi nombre es Chatbot ?",]
    ],
    [
        r"como estas ?",
        ["Bien, y tu?",]
    ],
    [
        r"disculpa (.*)",
        ["No pasa nada",]
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal",]
    ],
    [
        r"que (.*) quieres ?",
        ["Nada gracias",]

    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",]
    ],
    [
        r"finalizar",
        ["Chao","Fue bueno hablar contigo"]
],
]
reflexions_personal = {
"ir": "fui",
"hola": "hey"
}

# Funcion de chatear

def chatear():
    print("Hola soy un bot, escribe algo para comenzar") #mensaje por defecto
    chat = Chat(pares, reflexions_personal)
    chat.converse()
if __name__ == "__main__":
    chatear()

