import pickle
# cargar el modelo y el vectorizador

with open("IA_detector_emociones\\vctrs_mtrcs_guardados\\vectorizador.pkl","rb") as f:
    vectorizador = pickle.load(f)

with open("IA_detector_emociones\modelos_entrenados\modelo_nb.pkl", "rb") as f:
    modelo = pickle.load(f)

# funcion para predecir emociones en nuevas frases
def predecirEmocion(frase):
    # vectorizar la frase nueva
    frase_vectorizada = vectorizador.transform([frase])
    # predecir
    prediccion = modelo.predict(frase_vectorizada)[0]

    return prediccion

# probando con frases nuevas
while True:
    entrada = input("Escribe una frase (o 's' para terminar): ")
    if entrada.lower() == "s":
        break
    emocion = predecirEmocion(entrada)
    print(f"Emocion detectada: {emocion}" )