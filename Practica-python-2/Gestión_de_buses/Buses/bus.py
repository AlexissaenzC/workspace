class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None
        self.horarios = []
        self.conductor_asignado = None

    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, horario):
        self.horarios.append(horario)

    def asignar_conductor(self, conductor):
        for horario in self.horarios:
            if not conductor.esta_disponible(horario):
                print(f"El conductor {conductor.nombre} no está disponible en el horario {horario}.")
                return False
        self.conductor_asignado = conductor
        for horario in self.horarios:
            conductor.agregar_horario(horario)
        return True