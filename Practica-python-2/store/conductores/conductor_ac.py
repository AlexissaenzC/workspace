class Conductor:
    def __init__(self,DNI,Nombre,horario_asignado:list):
        self.DNI = DNI
        self.nombre = Nombre
        self.horario_asignado = horario_asignado
        pass
    def esta_disponible(self,horario):
        return horario not in self.horario_asignado
    def agregar_horario_conduc(self,horario):
        if self.esta_disponible(horario):
            self.horario_asignado.append(horario)
        else:
            print(f'El conductor {self.nombre} ya tiene horario {horario}.')
    def __str__(self):
        return f'El conductor con DNI: {self.DNI} de nombre: {self.nombre}'
