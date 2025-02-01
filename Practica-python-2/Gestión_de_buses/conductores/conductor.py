class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios_asignados = []

    def agregar_horario(self, horario):
        if self.esta_disponible(horario):
            self.horarios_asignados.append(horario)
        else:
            print(f"El conductor {self.nombre} ya tiene asignado el horario {horario}.")

    def esta_disponible(self, horario):
        return horario not in self.horarios_asignados