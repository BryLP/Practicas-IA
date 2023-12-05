import nltk
import numpy as np
import random
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords


#pruebas pa español
SW = set(stopwords.words('spanish'))
lemmer = SnowballStemmer('spanish')


f=open('C:/Users/bryan\Documents/IA practicas/minecraftS.txt','r',errors = 'ignore')

raw=f.read()

raw=raw.lower()# convierte mayusculas a minusculas

nltk.download('punkt') # Solo para primera vez
#nltk.download('wordnet') # Solo para primera vez
nltk.download('stopwords')

#

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
# Utilizar ENGLISH_STOP_WORDS de scikit-learn para stop words en inglés
EN_STOP_WORDS = list(ENGLISH_STOP_WORDS)

# Combinar stop words en inglés y español
ALL_STOP_WORDS = EN_STOP_WORDS + SW




sent_tokens = nltk.sent_tokenize(raw)# Convierte a lista de sentencias
word_tokens = nltk.word_tokenize(raw)# Convierte a lista de palabras

#Procesamiento de datos, lemmatizacion, tokens, etc 

#lemmer = nltk.stem.WordNetLemmatizer()
#WordNet es un diccionario Inglés incluido en nltk

def LemTokens(tokens):
 return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
 return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Coincidencia de palabras

GREETING_INPUTS = ("hola", "hi", "greetings", "sup", "what's up","hey",)

GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
        

# Estrucutra para respuesta del chatbot 

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)

    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words= ALL_STOP_WORDS)
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response
    
# 

flag=True
print("Chatsito BOT c: : My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")

while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("ROBO: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: "+greeting(user_response))
            else:
                print("ROBO: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("Chatsito BOT c: : Bye! take care..")