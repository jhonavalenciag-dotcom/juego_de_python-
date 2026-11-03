import random

numero_a_adivinar = random.randint(0,101)
adivino = False
intentos = 0
while not adivino: 
    if intentos >= 5: 
        print("ya no tienes mas intentos, el numero a adivinar era: ", numero_a_adivinar)
        break
    numero_ingresado = int(input("Ingresa el numero que vas a adivinarentre el 0 y el 100:  "))
    intentos += 1
    if numero_ingresado == numero_a_adivinar: 
        print("numero adivinado muy bieen")
        adivino = True 
    elif numero_ingresado > numero_a_adivinar:
        print("el numero ingresado es mayor al numero a adivinar")
    else: 
        print("el numero ingresado es menor al numero a adivinar")
    