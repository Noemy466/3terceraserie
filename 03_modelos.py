class Usuario:
    def __init__(self, id, nombre, email, rol):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f"Usuario: {self.id} | {self.nombre} | {self.email} | Rol: {self.rol}"


class Ticket:
    estados_validos = ["Open", "In Progress", "Resolved", "Closed", "Cancelled"]

    def __init__(self, id, titulo, categoria, prioridad, solicitante, tecnico=None):
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante
        self.tecnico = tecnico
        self._status = "Open"

    def __str__(self):
        tecnico_nombre = self.tecnico.nombre if self.tecnico else "Sin técnico"

        return (
            f"Ticket: {self.id} | {self.titulo} | "
            f"Categoría: {self.categoria} | Prioridad: {self.prioridad} | "
            f"Solicitante: {self.solicitante.nombre} | "
            f"Técnico: {tecnico_nombre} | Estado: {self._status}"
        )

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in self.estados_validos:
            self._status = nuevo_estado
            print(f"Ticket {self.id}: estado cambiado a {nuevo_estado}.")
        else:
            print(f"Error: '{nuevo_estado}' no es un estado permitido.")

    def asignar_tecnico(self, tecnico):
        if tecnico.rol.lower() == "technician":
            self.tecnico = tecnico
            print(f"Técnico {tecnico.nombre} asignado al ticket {self.id}.")
        else:
            print(f"Error: {tecnico.nombre} no tiene el rol de technician.")


# Crear usuarios
usuario1 = Usuario(1, "Noemy", "noemy@gmail.com", "user")
usuario2 = Usuario(2, "Carlos", "carlos@gmail.com", "technician")

# Crear tres ticketss
ticket1 = Ticket(
    101,
    "Computadora no enciende",
    "Hardware",
    "High",
    usuario1
)

ticket2 = Ticket(
    102,
    "Error en el sistema",
    "Software",
    "Medium",
    usuario1
)

ticket3 = Ticket(
    103,
    "Problema de red",
    "Network",
    "Critical",
    usuario1
)

tickets = [ticket1, ticket2, ticket3]

# Imprimir usuarios
print("=== USUARIOS ===")
print(usuario1)
print(usuario2)

# Imprimir tickets
print("\n=== TICKETS ===")
for ticket in tickets:
    print(ticket)


print("\n=== ASIGNAR TÉCNICO ===")
ticket1.asignar_tecnico(usuario2)


print("\n=== CAMBIAR ESTADO ===")
ticket1.cambiar_estado("In Progress")

# Intentar colocar un estado no permitido
print("\n=== ESTADO NO PERMITIDO ===")
ticket2.cambiar_estado("En espera")

# Mostrar tickets actualizados
print("\n=== TICKETS ACTUALIZADOS ===")
for ticket in tickets:
    print(ticket)