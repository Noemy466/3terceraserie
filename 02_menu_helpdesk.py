tickets = []


def pedir_opcion():
    print("\n=== MENÚ HELPDESK ===")
    print("1. Registrar ticket")
    print("2. Listar tickets")
    print("3. Buscar por solicitante")
    print("4. Resumen por prioridad")
    print("5. Salir")

    return input("Seleccione una opción: ")


def registrar_ticket():
    print("\n=== REGISTRAR TICKET ===")

    numero = int(input("Número de ticket: "))
    solicitante = input("Solicitante: ")
    titulo = input("Título: ")
    descripcion = input("Descripción: ")
    categoria = input("Categoría: ")
    prioridad = input("Prioridad: ")

    ticket = {
        "numero": numero,
        "solicitante": solicitante,
        "titulo": titulo,
        "descripcion": descripcion,
        "categoria": categoria,
        "prioridad": prioridad,
        "status": "Open"
    }

    tickets.append(ticket)
    print("Ticket registrado correctamente.")


def listar_tickets():
    print("\n=== LISTA DE TICKETS ===")

    if len(tickets) == 0:
        print("No hay tickets registrados.")
    else:
        for ticket in tickets:
            print(f"Ticket: {ticket['numero']}")
            print(f"Solicitante: {ticket['solicitante']}")
            print(f"Título: {ticket['titulo']}")
            print(f"Prioridad: {ticket['prioridad']}")
            print(f"Estado: {ticket['status']}")
            print("------------------------")


def buscar_por_solicitante():
    nombre = input("\nIngrese el solicitante a buscar: ")
    encontrado = False

    for ticket in tickets:
        if ticket["solicitante"].lower() == nombre.lower():
            print("\nTicket encontrado:")
            print(f"Número: {ticket['numero']}")
            print(f"Título: {ticket['titulo']}")
            print(f"Prioridad: {ticket['prioridad']}")
            print(f"Estado: {ticket['status']}")
            encontrado = True

    if not encontrado:
        print("No se encontraron tickets para ese solicitante.")


def mostrar_resumen():
    print("\n=== RESUMEN POR PRIORIDAD ===")

    low = 0
    medium = 0
    high = 0
    critical = 0

    for ticket in tickets:
        prioridad = ticket["prioridad"].lower()

        if prioridad == "low":
            low += 1
        elif prioridad == "medium":
            medium += 1
        elif prioridad == "high":
            high += 1
        elif prioridad == "critical":
            critical += 1

    print(f"Low: {low}")
    print(f"Medium: {medium}")
    print(f"High: {high}")
    print(f"Critical: {critical}")
    print(f"Total de tickets: {len(tickets)}")


def ejecutar_menu():
    while True:
        opcion = pedir_opcion()

        if opcion == "1":
            registrar_ticket()
        elif opcion == "2":
            listar_tickets()
        elif opcion == "3":
            buscar_por_solicitante()
        elif opcion == "4":
            mostrar_resumen()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    ejecutar_menu()