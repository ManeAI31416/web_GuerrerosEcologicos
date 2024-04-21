import pandas as pd
import random
import ollama

class PreguntasEcologicas:
    def __init__(self):
        self.df = pd.read_csv('preguntas.csv')
        self.preguntas = self.df.iloc[:, 0].tolist()
        self.preguntas_hechas = []

    def hacer_pregunta(self):
        pregunta = random.choice([q for q in self.preguntas if q not in self.preguntas_hechas])
        self.preguntas_hechas.append(pregunta)
        respuesta = input(f"{pregunta}\nTu respuesta: ")
        if respuesta.lower() == "exit":
            return None
        return pregunta, respuesta

    def procesar_respuesta(self, pregunta, respuesta):
        prompt = f'''
                 FROM llama3
                 SYSTEM Eres un experto en ecologia. Donde, la retroalimentacion que des debe ser en español y tu respuesta debes darla en un formato de conversacion natural. Ademas, solo debes responder con la valoracion y la retrroalimentacion, no hagas preguntas al final.
                 
                 Evalua del 1 al 10 si esta es una respuesta correcta: "{respuesta}".

                 Para la pregunta: "{pregunta}".

                 Dicha pregunta fue respondida por un niño/niña de entre 10-15 años.

                 Si consideras la respuesta dada, con una valoración igual o menor a 7 tomando en cuenta la edad del niño/a, da una retroalimentación de 15 palabras (considerando las edades mencionadas  anteriormente para que sea entendible tu retroalimentacion para su edad), dicha retroalimentacion debe ser la respuesta correcta o la forma correcta.
                 Por otro lado, si consideras la respuesta dada con una valoración mayor a 7 y felicitalo y da una retroalimentacion de 15 palabras sobre algo que no haya mencionado.
                 '''
        response = ollama.generate(model="guecologicos", prompt=prompt)
        return response["response"]

    def comenzar_juego(self):
        while True:
            pregunta_respuesta = self.hacer_pregunta()
            if pregunta_respuesta is None:
                break
            pregunta, respuesta = pregunta_respuesta
            retroalimentacion = self.procesar_respuesta(pregunta, respuesta)
            print(retroalimentacion)


if __name__ == "__main__":
    juego = PreguntasEcologicas()
    juego.comenzar_juego()
