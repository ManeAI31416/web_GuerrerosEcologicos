import pandas as pd
import random

# Cargar el dataset
df = pd.read_csv('preguntas.csv')

# Convertir el dataframe a una lista
preguntas = df.iloc[:, 0].tolist()

# Inicializar una lista vacía para almacenar las preguntas hechas
preguntas_hechas = []

# Definir una función para hacer una pregunta
def hacer_pregunta():
    # Seleccionar una pregunta aleatoria que no se haya hecho antes
    pregunta = random.choice([q for q in preguntas if q not in preguntas_hechas])
    
    # Añadir la pregunta a la lista de preguntas hechas
    preguntas_hechas.append(pregunta)
    
    # Imprimir la pregunta
    print(pregunta)
    
    # Obtener la respuesta del usuario
    respuesta = input("Tu respuesta: ")
    
    # Verificar si el usuario quiere salir
    if respuesta.lower() == "exit":
        raise SystemExit  # Terminar el programa
    
    # Imprimir la respuesta del usuario
    print(f"Respondiste: {respuesta}")

# Bucle infinito para hacer preguntas
while True:
    hacer_pregunta()
