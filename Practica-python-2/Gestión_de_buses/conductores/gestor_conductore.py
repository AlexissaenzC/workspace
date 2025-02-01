from conductores.conductor import Conductor

conductores = {}

def agregar_conductor(nombre):
    conductores[nombre] = Conductor(nombre)
    return f"Conductor {nombre} agregado."

def asignar_horario_a_conductor(nombre, horario):
    if nombre in conductores:
        conductores[nombre].agregar_horario(horario)
        return "Horario asignado."
    return "Conductor no encontrado."

def asignar_bus_a_conductor(placa, nombre, buses):
    if placa in buses and nombre in conductores:
        if buses[placa].asignar_conductor(conductores[nombre]):
            return "Conductor asignado con éxito."
        return "El conductor no está disponible."
    return "Bus o conductor no encontrado."