import pandas as pd

def obtenerDatosSueno():
    """
    Procesa el archivo CSV de datos de sueño y devuelve un DataFrame.
    """
    # Lee el csv
    df = pd.read_csv("./datos_sueno/datos/datos_sueno1.csv", parse_dates=["fecha"])
    print(df.head(5))

    # Convirtiendo horas a tipo datetime y combinandolas con la fecha

    df["hora_dormir"] = pd.to_datetime(df["fecha"].astype(str) + " " + df["hora_dormir"])
    df["hora_despertar"] = pd.to_datetime(df["fecha"].astype(str) + " " + df["hora_despertar"])

    # Suma un dia a las filas donde la hora_despertar es menor que la hora_dormir
    df.loc[df["hora_despertar"] < df["hora_dormir"], "hora_despertar"] += pd.Timedelta(days=1)

    # Calculando la duracion del suenio

    # Restando las horas dormidas con la hora en la que desperte, 
    # sacando los segundo equivalentes a esa diferencia de horas y
    # dividiendolos para 1 hora en segundos 
    df["horas_dormidas"] = (df["hora_despertar"] - df["hora_dormir"]).dt.total_seconds() / 3600
    # print(df)
    # df df["horas_dormidas"] seria una columna nueva con ese nombre y que me 
    # muestra las horas dormidas por dia

    return df

if __name__ == "__main__":
    df_procesado = obtenerDatosSueno()
    print(df_procesado)
