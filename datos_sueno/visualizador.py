import matplotlib.pyplot as plt

from calculo_horas import obtenerDatosSueno
#Obteniendo los datos
df = obtenerDatosSueno()

# Realizando el grafico de horas dormidas
plt.plot(df["fecha"], df["horas_dormidas"], marker="o")
plt.xlabel("FECHA")
plt.ylabel("HORAS DE SUEÑO")
plt.title("PATRON DE SUEÑO")

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
