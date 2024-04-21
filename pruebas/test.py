import ollama

modelfile='''
FROM llama3
SYSTEM Eres un experto en ecologia. Donde, la retroalimentacion que des debe ser en español y tu respuesta debes darla en un formato de conversacion natural. Ademas, solo debes responder con la valoracion y la retrroalimentacion, no hagas preguntas al final.
'''

response = ollama.create(model='guecologicos', modelfile=modelfile)

response

response = ollama.generate(model="guecologicos",
                           prompt='''
                            Evalua del 1 al 10 si esta es una respuesta correcta: "Es una manera para ayudar al planeta para reducir cambios climaticos".
                            Para la pregunta: "¿Que es la ecologia?".
                            Dicha pregunta fue respondida por un niño/niña de entre 10-15 años.
                            Si consideras la respuesta dada, con una valoración igual o menor a 5 da una retroalimentación de 15 palabras (considerando las edades mencionadas anteriormente para que sea entendible tu retroalimentacion para su edad), dicha retroalimentacion debe ser la respuesta correcta o la forma correcta.
                            ''')

print(response["response"])