from Buses.bus import Bus

buses = {}

def agregar_bus(placa):
    buses[placa] = Bus(placa)
    return f"Bus {placa} agregado."

def asignar_ruta_a_bus(placa, ruta):
    if placa in buses:
        buses[placa].agregar_ruta(ruta)
        return "Ruta asignada."
    return "Bus no encontrado."

def registrar_horario_a_bus(placa, horario):
    if placa in buses:
        buses[placa].registrar_horario(horario)
        return "Horario registrado."
    return "Bus no encontrado."