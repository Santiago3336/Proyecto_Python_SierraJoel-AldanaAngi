import json

action = str

def nextId(id):
    return id + 1


def coordinador():
    print("A cual menu deseas entrar?\n1 Campers\n2 Trainers\n3 Horarios\n4 Modulos\n5 Salones\n6 Rutas")
    action = input()
    if action == 1:
        print("A continuacion escribe el numero de la opcion a la que deseas ingresar:\n1 Campers en Riesgo Alto\n")
    elif action == 2:
        print()
    elif action == 3:
        print()
    elif action == 4:
        print()
    elif action == 6:
        print()
        print("Que deseas hacer?\n1 Añadir nuevas Rutas\t2 Eliminar una Ruta\t3 Reemplazar una Ruta")