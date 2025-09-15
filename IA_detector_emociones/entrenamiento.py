from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

import pandas as pd 
import pickle

# 1. cargamos el vectorizador y la matriz
with open("IA_detector_emociones\\vctrs_mtrcs_guardados\\vectorizador.pkl", "rb") as f:
    vectorizador = pickle.load(f)

with open("IA_detector_emociones\\vctrs_mtrcs_guardados\\matriz.pkl", "rb") as f:
    matriz = pickle.load(f)

# 2. cargamos los datos del dataset limpio
df = pd.read_csv("IA_detector_emociones\datos_emociones\dataset_emociones_limpio.csv")
# filtrando y elmininando los registros nulos de la culomna de texto limpio
df = df.dropna(subset=["texto_limpio"])
col_emocion = df["emocion"] # columan de etiquetas de emociones

# 3. dividir en train/test
X_train, X_test, y_train, y_test = train_test_split(matriz, col_emocion, test_size=0.2, random_state=42)

# 4. entrenar modelo
modelo = MultinomialNB()
modelo.fit(X_train, y_train)

# 5. evaluamos
y_prediccion = modelo.predict(X_test)
print("Precision: ", accuracy_score(y_test, y_prediccion))
print("\nReporte de clasificacion: \n", classification_report(y_test, y_prediccion))

# 6. guardar modelo entrenando
with open("IA_detector_emociones\modelos_entrenados\modelo_nb.pkl", "wb") as f:
    pickle.dump(modelo, f)

print("Modelo entrenado y guardado")
