from Buses.gestor_buses import *
from conductores.gestor_conductore import *
def Menu():
    msg = '''
    **********
    BIENVENIDO
    **********

    1. Agregar bus.
    2. Agregar conductor.
    3. Asignar ruta al bus
    4. Registrar horario del bus
    5. Agregar horario al conductor.
    6. Asignar bus al conductor.
    7. Salir. 
    '''
    
    while True:
        print(msg)
        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                placa = input("Ingrese la placa del bus: ")
                print(agregar_bus(placa))
            case 2:
                nombre = input("Ingrese el nombre del conductor: ")
                print(agregar_conductor(nombre))
                pass
            case 3:
                placa = input("Ingrese la placa del bus: ")
                ruta = input("Ingrese la ruta del bus: ")
                print(asignar_ruta_a_bus(placa, ruta))
                pass
            case 4:
                placa = input("Ingrese la placa del bus: ")
                horario = input("Ingrese el horario del bus (ej: 08:00-10:00): ")
                print(registrar_horario_a_bus(placa, horario))
                pass
            case 5:
                nombre = input("Ingrese el nombre del conductor: ")
                horario = input("Ingrese el horario (ej: 08:00-10:00): ")
                print(asignar_horario_a_conductor(nombre, horario))
            case 6:
                placa = input("Ingrese la placa del bus: ")
                nombre = input("Ingrese el nombre del conductor: ")
                print(asignar_bus_a_conductor(placa, nombre, buses))
                pass
            case 7:
                print('Hasta luego.')
                break
            case _:
                print('Ingrese otra opción válida.')