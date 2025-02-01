from conductores.Acciones import*

def Menu():
    msg = '''
    **********
    BIENVENIDO
    **********

    1. Agregar bus.
    2. Agregar ruta al bus.
    3. Registrar horario al bus.
    4. Agregar conductor.
    5. Agregar horario al conductor.
    6. Asignar bus al conductor.
    7. Salir. 
    '''
    conductor_lis = []
    
    while True:
        print(msg)
        opcion = int(input('Ingrese una opción: '))
        match opcion:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                agregar_conductor(conductor_lis)
            case 5:
                pass
            case 6:
                pass
            case 7:
                print('Hasta luego.')
                break
            case _:
                print('Ingrese otra opción válida.')