from conductores.conductor_ac import Conductor

def lista_conduc(lista_conductores:list):
    if len(lista_conductores)>0:
        for i in lista_conductores:
            print (i)
def agregar_conductor(lista_agregar_conduc:list):
    DNI = int(input('Ingrese el DNI: '))
    nombre = input('Ingrese los nombres completos: ')
    horario_asignado = input('Ingrese el horario asigando ejemplo (hh:mm / am o pm): ')
    pr1 = Conductor(DNI,nombre,horario_asignado)
    lista_agregar_conduc.append(pr1)