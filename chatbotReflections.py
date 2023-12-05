import nltk
import datetime as dt

# reflections sirve para escribir las respuestas a determinadas preguntas
from nltk.chat.util import Chat, reflections
pares = [
    [
        r"mi nombre es (.*)",
        ["Hola, mucho gusto !! c: \n",]
    ],
     [
        r"cual es tu nombre ?",
        ["Mi nombre es JARVIS JR\n",]
    ],
    [
        r"como estas ?",
        ["Bien jeje, y tu?\n",]
    ],
    [
        r"disculpa (.*)",
        ["No te preocupes c:\n",]
    ],
    [
        r"hola|hoa|buenas|hellou|ey|saludos|que onda",
        ["Hola\n", "Que tal\n","Que hay!\n","Hoaa c:\n", "Buen dia c:","Que tal ! :D\n"]
    ],
    [
        r"estoy cansado",
        ["Lo siento :C, espero puedas descansar \n",]

    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy :D\n",]
    ],
    [
        r"(.*) fecha y hora hoy?",
        ["Hoy es -> "+str(dt.datetime.now())+"\n",]
    ],
    [
        r"gracias",
        ["No hay de que !","Fue un gusto ayudarte :D","Denada :D\n",]
    ],
    [
        r"que es el lenguaje c",
        ["C es un lenguaje de programación de propósito general originalmente desarrollado por Dennis Ritchie entre 1969 y 1972 en los Laboratorios Bell,como evolución del anterior lenguaje B, a su vez basado en BCPL.\n Al igual que B, es un lenguaje orientado a la implementación de sistemas operativos, concretamente Unix. \n",]
    ],
    [
        r"quien es spiderman",
        ["Spider-Man, traducido en ocasiones como el Hombre Araña, es un personaje creado por los estadounidenses Stan Lee y Steve Ditko, \n e introducido en el cómic Amazing Fantasy n.° 15, publicado por Marvel Comics en agosto de 1962.\n Se trata de un superhéroe que emplea sus habilidades sobrehumanas, reminiscentes de una araña, para combatir a otros supervillanos que persiguen fines siniestros.\n",]
    ],
    [
        r"que es la ingenieria en computacion",
        ["La ingeniería en computación estudia el desarrollo de sistemas automatizados y el uso de los lenguajes de programación; de igual forma se enfoca al análisis,\n diseño y la utilización del hardware y software para lograr la implementación de las más avanzadas aplicaciones industriales, telemáticas y científicas\n",]
    ],
    [
        r"que es la unam",
        ["La Universidad Nacional Autónoma de México es una universidad pública mexicana. \nSe destaca como una de las mejores universidades del mundo debido a su excelencia en materia artística, tecnológica y de investigación.\n",]
    ],
    [
        r"cuando se fundo la unam",
        ["La Universidad Nacional Autónoma de México, se funda en 1910, durante el gobierno presidencial de Porfirio Díaz y auspiciada por Justo Sierra Méndez\n",]
    ],
    [
        r"cuantas carreras hay en la unam",
        ["Actualmente la UNAM cuenta con 133 carreras a nivel superior, a las que cada año ingresan miles de estudiantes.\n",]
    ],
    [
        r"cuentame un chiste",
        ["¿Cuál es el último animal que subió al arca de Noé? El del-fin\n","¿Qué le dice un gusano a otro gusano? Voy a dar una vuelta a la manzana.\n","¿Cuál es el colmo de Aladdín? Tener mal genio.\n","¿Por qué las focas miran siempre hacia arriba? ¡Porque ahí están los focos!\n","¿Cómo se llama el primo de Bruce Lee? Broco Lee.\n","¿Cómo queda un mago después de comer? Magordito.\n",]
    ],
    [
        r"cuanto vale una decada",
        ["Una década es un período de 10 años\n",]
    ],
    [
        r"cuanto vale un lustro",
        ["Período de cinco años.\n",]
    ],
    [
        r"que es un evento canonico",
        ["Es un evento crucial que cambia el rumbo de la vida, que no puede ser evitado.\n",]
    ],
    [
        r"que tipo de tamal soy",
        ["Jmmm, creo que pareces un tamal de dulce :D\n",]
    ],
    [
        r"cual es la pelicula con mas oscars",
        ["Tres películas comparten el récord de mayor número de estatuillas, Ben-Hur (1959), Titanic (1997) y El Señor de los Anillos: El Retorno del Rey (2003)\n",]
    ],
    [
        r"que es la inteligencia artificial",
        ["La inteligencia artificial (IA), en el contexto de las ciencias de la computación, es una disciplina y un conjunto de capacidades cognoscitivas e intelectuales expresadas \npor sistemas informáticos o combinaciones de algoritmos cuyo propósito es la creación de máquinas que imiten la inteligencia humana para realizar tareas, y que pueden mejorar conforme recopilen información\n",]
    ],
    [
        r"que es un chatbot",
        ["Los bot de charla o bot conversacional, son aplicaciones software que surgen en los años 60, y que simulan mantener una conversación con una persona al proveer respuestas automáticas, las cuales son previamente establecidas por un conjunto de expertos a entradas realizadas por el usuario.\n",]
    ],
    [
        r"quien es superman",
        ["Superman es un superhéroe ficticio que apareció por primera vez por Action Cómics, perteniciente al grupo de cómics estadounidenses publicados por DC Comics,\n Bajo la identidad de Clark Kent, Superman vive en medio de los humanos como un -tímido reportero- del diario Daily Planet de Metrópolis\n",]
    ],
    [
        r"quien es batman",
        ["Batman es la identidad secreta de Bruce Wayne, un empresario multimillonario, galán y filántropo. Presenció el asesinato de sus padres cuando era niño lo marcó profundamente y lo llevó a entrenarse en la perfección física e intelectual para ponerse un disfraz de murciélago con el fin de combatir el crimen.\n",]
    ],
    [
        r"bye",
        ["Chao c:\n","Fue bueno hablar contigo\n"]
    ],
    [
        r"(.*)",
        ["Lo siento, no pude entenderte :c\n",]
    ],
]
reflexions_personal = {
"ir": "fui",
"hola": "hey",
"bye" : "chao",
"vale": "equivale",
"gracias" : "te agradezco",
"cansado" : "agotado",
"disculpa": "perdon"
}

# Funcion para chatear

def chatear():
    print("Hola, soy JARVIS JR, escribe algo para comenzar el chat :D\n") #mensaje inicial
    chat = Chat(pares, reflexions_personal)
    chat.converse()
if __name__ == "__main__":
    chatear()

