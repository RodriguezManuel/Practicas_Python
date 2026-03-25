import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]
word = random.choice(words)  # Elige una palabra al azar de la lista de palabras
guessed = []
attempts = 6  # intentos
print("¡Bienvenido al Ahorcado!")
print()
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""  # por cada intento borra el progreso anterior, para luego comprobar atraves de si se agrega o no el guion, si adivino la palabra
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")
    if (
        len(letter) != 1 or not letter.isalpha()
    ):  # Me aseguro que el usuario ingrese solo una letra y que sea alfabética
        print("Entrada no válida")
        continue
    if (
        letter in guessed
    ):  # evaluo si la letra esta en la lista de las letras ya ingresadas
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
