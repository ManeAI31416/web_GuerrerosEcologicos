from flask import Flask, render_template, request, session
import pandas as pd
import random
import ollama
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key for the session

class PreguntasEcologicas:
    def __init__(self):
        self.df = pd.read_csv('preguntas.csv')
        self.preguntas = self.df.iloc[:, 0].tolist()
        self.preguntas_hechas = []

    def hacer_pregunta(self):
        if not self.preguntas_hechas:
            self.preguntas_hechas = self.preguntas.copy()
        pregunta = random.choice(self.preguntas_hechas)
        self.preguntas_hechas.remove(pregunta)
        return pregunta

    def procesar_respuesta(self, respuesta, pregunta):
        prompt = f'''
                 FROM llama3
                 SYSTEM Eres un experto en ecologia. Donde, la retroalimentacion que des debe ser en español y tu respuesta debes darla en un formato de conversacion natural. Ademas, solo debes responder con la valoracion y la retrroalimentacion, no hagas preguntas al final.
                 
                 Evalua del 1 al 10 si esta es una respuesta correcta: "{respuesta}".

                 Para la pregunta: "{pregunta}".

                 Dicha pregunta fue respondida por un niño/niña de entre 10-15 años.

                 Si consideras la respuesta dada, con una valoración igual o menor a 6 tomando en cuenta la edad del niño/a, da una retroalimentacion de 40 palabras (considerando las edades mencionadas  anteriormente para que sea entendible tu retroalimentacion para su edad), dicha retroalimentacion debe ser la respuesta correcta o la forma correcta.
                 Por otro lado, si consideras la respuesta dada con una valoración mayor a 6 y felicitalo y da una retroalimentacion de 25 palabras sobre algo que no haya mencionado.
                 '''
        response = ollama.generate(model="guecologicos", prompt=prompt)
        return response["response"]

preguntas_ecologicas = PreguntasEcologicas()

@app.route('/')
def index():
    # Store the question in the session
    session['pregunta'] = preguntas_ecologicas.hacer_pregunta()
    return render_template('index.html', pregunta=session['pregunta'])

@app.route('/procesar', methods=['POST'])
def procesar():
    respuesta = request.form['respuesta']
    # Retrieve the question from the session
    pregunta = session.get('pregunta', '')
    retroalimentacion = preguntas_ecologicas.procesar_respuesta(respuesta, pregunta)
    return retroalimentacion

@app.route('/end.html')
def end():
    return render_template('end.html')

if __name__ == "__main__":
    app.run(debug=True)
