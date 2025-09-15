import pandas as pd
import nltk 
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Descargar recursos NLTK (solo la primera vez)

nltk.download("punkt")
nltk.download("stopwords")
nltk.download('punkt_tab')
# 1. Cargar el CSV
df = pd.read_csv("IA_detector_emociones\datos_emociones\dataset_emociones.csv")
# print(df)

# 2. Definimos la funcion de limpieza de textos
def limpiar_texto(texto):
    # convertirlo a tipo string y pasar a minusculas 
    texto = str(texto).lower()

    # quitando puntuacion
    texto = texto.translate(str.maketrans("","", string.punctuation))

    # tokenizando
    tokens = word_tokenize(texto)

    # Eliminar las stopwords en espanol
    stop_words = set(stopwords.words("spanish"))
    tokens = [palabra for palabra in tokens if palabra not in stop_words]

    # (Opcional) volver a unir en una sola cadena
    texto_limpio = " ".join(tokens)

    return texto_limpio

# 3. Aplicar la limpieza a toda la columna "texto"
df["texto_limpio"] = df["texto"].apply(limpiar_texto)

# 4. Guardar el nuevo CSV
df.to_csv("dataset_emociones_limpio.csv", index=False)

print("El archivo CSV se limpio correctamente y se creó 'dataset_emociones_limpio.csv' con la limpieza de datos")