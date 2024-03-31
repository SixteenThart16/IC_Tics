from flask import Flask, request, render_template
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

app = Flask(__name__)

# Descarga de recursos necesarios para NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Palabras clave para determinar si el vehículo necesita reparación
repair_keywords = {"ruidos", "humo", "fuga", "temperatura", "luces", "freno", "aceite"}

def preprocess(text):
    # Tokenización
    tokens = word_tokenize(text.lower())
    
    # Eliminación de stopwords y signos de puntuación
    stop_words = set(stopwords.words('spanish') + list(string.punctuation))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    
    return tokens

def check_repair(tokens):
    for word in tokens:
        if word in repair_keywords:
            return True
    return False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["user_message"]
    processed_message = preprocess(user_message)
    needs_repair = check_repair(processed_message)
    if needs_repair:
        response = "Es recomendable llevar tu vehículo a revisión."
    else:
        response = "Tu vehículo parece estar en buen estado, pero si tienes dudas, es mejor llevarlo a revisar."
    return render_template("index.html", user_message=user_message, response=response)

if __name__ == "__main__":
    app.run(debug=True)
