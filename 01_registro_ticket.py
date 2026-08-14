# 01_registro_ticket.py

print("=== REGISTRO DE TICKET ===")

# Número de ticket
while True:
    try:
        numero = int(input("Número de ticket: "))
        break
    except ValueError:
        print("Error: el número de ticket debe ser un número entero.")

# Campos obligatorios
while True:
    solicitante = input("Solicitante: ").strip()
    if solicitante:
        break
    print("Error: el solicitante es obligatorio.")

while True:
    titulo = input("Título: ").strip()
    if titulo:
        break
    print("Error: el título es obligatorio.")

while True:
    descripcion = input("Descripción: ").strip()
    if descripcion:
        break
    print("Error: la descripción es obligatoria.")

# Categoría
categorias = ["General", "Hardware", "Software", "Network"]

while True:
    categoria = input("Categoría (General/Hardware/Software/Network): ").strip()
    if categoria in categorias:
        break
    print("Error: categoría no válida.")

# Prioridad
prioridades = ["Low", "Medium", "High", "Critical"]

while True:
    prioridad = input("Prioridad (Low/Medium/High/Critical): ").strip()
    if prioridad in prioridades:
        break
    print("Error: prioridad no válida.")

# Diccionario del ticket
ticket = {
    "numero": numero,
    "solicitante": solicitante,
    "titulo": titulo,
    "descripcion": descripcion,
    "categoria": categoria,
    "prioridad": prioridad,
    "status": "Open"
}

# Resumen
print("\n=== RESUMEN DEL TICKET ===")
print(f"Número: {ticket['numero']}")
print(f"Solicitante: {ticket['solicitante']}")
print(f"Título: {ticket['titulo']}")
print(f"Descripción: {ticket['descripcion']}")
print(f"Categoría: {ticket['categoria']}")
print(f"Prioridad: {ticket['prioridad']}")
print(f"Estado: {ticket['status']}")