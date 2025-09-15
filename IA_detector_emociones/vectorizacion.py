import pandas as pd
# Instalar la biblioteca scikit-learn y luego importar el vectorizador
from sklearn.feature_extraction.text import TfidfVectorizer

# 1. Cargando el CSV limpio
df = pd.read_csv("IA_detector_emociones\datos_emociones\dataset_emociones_limpio.csv")

# Paso importante. Eliminar filas con valores nulos de la colmna "texto_limpio"
df_limpio_sin_nulos = df.dropna(subset=["texto_limpio"])

# 2. Inicializamos el vectorizador TF-IDF
vectorizador = TfidfVectorizer()

# 3. Ajustamos y transformamos los textos
matriz = vectorizador.fit_transform(df_limpio_sin_nulos["texto_limpio"])

# Mostrando informacion
print("Froma de la matriz TF-IDF: ", matriz.set_shape)
print("Ejemplo de caracteristicas: ", vectorizador.get_feature_names_out()[:20])

# guardando el vector y la matriz
import pickle

# vector
with open("vectorizador.pkl", "wb") as f:
    pickle.dump(vectorizador, f)

with open("matriz.pkl", "wb") as f:
    pickle.dump(matriz, f)

# Para cargarlos en otro script se hace asi:
"""
with open("vectorizador.pkl", "wb") as f:
    vectorizador = pickle.load(f)

with open("matriz.pkl", "wb") as f:
    matriz = pickle.load(f)
"""

