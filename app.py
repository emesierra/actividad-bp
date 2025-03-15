import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    computadora = random.choice(opciones)
    usuario = input("Elige piedra, papel o tijera: ").lower()

    if usuario not in opciones:
        print("Opción no válida. Intenta de nuevo.")
        return

    print(f"Computadora eligió: {computadora}")

    if usuario == computadora:
        print("¡Empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
        (usuario == "papel" and computadora == "piedra") or \
        (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

if __name__ == "__main__":
    jugar()