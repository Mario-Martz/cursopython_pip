import random

OPCIONES = ("Piedra", "Papel", "Tijera", "Lagarto", "Spock")

OP_DIBUJO = {
    "Piedra": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "Papel": """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    "Tijera": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
    "Lagarto": """
    _______
---'   ____)____
          ______)
       __ /      )
      (____)
---.__(___)
""",
    "Spock": """
    _______
---'   ____)____
          ______)
       __/  ____)
      (____)
---.__(___)
"""
}

def obtener_opcion_usuario():
    while True:
        opcion = input("Ingresa la opción con la que vas a jugar: ").capitalize()
        if opcion in OPCIONES:
            return opcion
        else:
            print("Opción no válida. Por favor, elige entre Piedra, Papel, Tijera, Lagarto o Spock.")

def generar_opcion_pc():
    return random.choice(OPCIONES)

def determinar_ganador(opcion_usuario, opcion_pc):
    if opcion_usuario == opcion_pc:
        return "Empate"
    elif ((opcion_usuario == "Piedra" and (opcion_pc == "Tijera" or opcion_pc == "Lagarto")) or
          (opcion_usuario == "Papel" and (opcion_pc == "Piedra" or opcion_pc == "Spock")) or
          (opcion_usuario == "Tijera" and (opcion_pc == "Papel" or opcion_pc == "Lagarto")) or
          (opcion_usuario == "Lagarto" and (opcion_pc == "Spock" or opcion_pc == "Papel")) or
          (opcion_usuario == "Spock" and (opcion_pc == "Tijera" or opcion_pc == "Piedra"))):
        return "Usuario"
    else:
        return "PC"

def mostrar_resultados(contador_ganador, contador_perdedor):
    mensaje_g = "punto" if contador_ganador == 1 else "puntos"
    mensaje_p = "punto" if contador_perdedor == 1 else "puntos"
    print("\nFin de la partida, los resultados son:")
    print(f"PC: {contador_perdedor} {mensaje_p}")
    print(f"Usuario: {contador_ganador} {mensaje_g}")
    if contador_ganador == contador_perdedor:
        print("¡Empate!")
    elif contador_ganador > contador_perdedor:
        print("¡Has ganado!")
    else:
        print("¡La PC ha ganado!")

def main():
    try:
        n_veces = int(input("¿Cuántas veces quieres jugar? "))
    except ValueError:
        print("Por favor, ingresa un número entero.")
        return

    contador_ganador = 0
    contador_perdedor = 0

    for _ in range(n_veces):
        opcion_usuario = obtener_opcion_usuario()
        opcion_pc = generar_opcion_pc()

        print("Tu elección:")
        print(OP_DIBUJO[opcion_usuario])
        print("Elección de la PC:")
        print(OP_DIBUJO[opcion_pc])

        ganador = determinar_ganador(opcion_usuario, opcion_pc)
        if ganador == "Usuario":
            print("¡Has ganado esta ronda!")
            contador_ganador += 1
        elif ganador == "PC":
            print("¡La PC ha ganado esta ronda!")
            contador_perdedor += 1
        else:
            print("Esta ronda es un empate.")

    mostrar_resultados(contador_ganador, contador_perdedor)

if __name__ == "__main__":
    main()