"""
1. Se necesitan 2 jugadores, cada uno con un nombre y una elección de "piedra", "papel" o "tijeras".
2. Se necesita ver el ganador de la partida, y si hay empate.
3. Se necesita que maneje el error de que el jugador ingrese una opción que no sea "piedra", "papel" o "tijeras".
4. Que se pueda jugar varias veces, y que al final se muestre el puntaje de cada jugador.
5. Se debe usar las elecciones en minusculas.

"""
import sys

gamer1 = input("ingresa el nombre del jugador 1: ")
gamer2 = input("ingresa el nombre del jugador 2: ") 
marcador1 = 0
marcador2 = 0
for i in range(3):
    selecion1 = input(f"{gamer1} ingresa tu eleccion (piedra, papel o tijeras): ").lower()
    selecion = False
    i = i + 1
    while selecion == False:
        if selecion1 == "piedra" or selecion1 == "tijeras" or selecion1 == "papel":
            selecion = True
            
        else:
            print("ingresa una opcion valida")
            decision = input("quieres volver a jugar? (si/no): ").lower()
            
            if decision == "si":
                selecion1 = input(f"{gamer1} ingresa tu eleccion (piedra, papel o tijeras): ").lower()
                
            else:
                print("gracias por jugar")
                sys.exit()
        
        
    selecion2 = input(f"{gamer2} ingresa tu eleccion (piedra, papel o tijeras): ").lower()
    selecion = False
    while selecion == False:
        if selecion2 == "piedra" or selecion2 == "tijeras" or selecion2 == "papel":
            selecion = True
        else:
            print("ingresa una opcion valida")
            decision2 = input("quieres volver a jugar? (si/no): ").lower()
            
            if decision2 == "si":
                selecion2 = input(f"{gamer2} ingresa tu eleccion (piedra, papel o tijeras): ").lower()
                
            else:
                print("gracias por jugar")
                sys.exit()
                
    if selecion1 == selecion2:
        print("empate")
    elif selecion1 == "piedra" and selecion2 == "tijeras" or selecion1 == "papel" and selecion2 == "piedra" or selecion1 == "tijeras" and selecion2 == "papel":
        print(f"el ganador es {gamer1}")
        marcador1 = marcador1 + 1
    else:
        print(f"el ganador es {gamer2}")
        marcador2 = marcador2 + 1
print(f"el marcador final es {gamer1}: {marcador1} - {gamer2}: {marcador2} ")
if marcador1 > marcador2:
    print(f"el ganador final es {gamer1}")
else:
    print(f"el ganador final es {gamer2}")