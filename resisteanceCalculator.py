def resistencia_serie(resistencias):
    """"Calcula la resitencia total de un circuito en serie."""
    return sum(resistencias)
def resistencia_paralelo(resistencias):
    """Calcula la resistencia total de un circuito en paralelo"""
    inversos = [1 / r for r in resistencias]
    return 1/sum(inversos)

tipo_circuito = input("¿El circuito es en serio o paralelo? ")
valores_resistencias = input("Ingrese los valores de las resistencias (separados por comas): ")
resistencias = [float(r) for r in valores_resistencias.split(",")]

if tipo_circuito.lower() == "serie":
    resistencia_total = resistencia_serie(resistencias)
elif tipo_circuito.lower() == "paralelo":
    resistencia_total = resistencia_paralelo(resistenciasis)
else:
    print("Tipo de circuito no válido.")
    exit()

print(f"La resistencia total es: {resistencia_total:.2f} ohms")
