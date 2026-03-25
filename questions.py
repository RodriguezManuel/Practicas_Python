import random

words = {
    "Nombres de Lenguajes de Programación": ["python"],
    "Términos de Programación": ["programa", "variable", "funcion", "bucle"],
    "Tipos de Datos": ["entero", "lista", "cadena"],
}
guessed = []
attempts = 6  # intentos
score = 0
print("¡Bienvenido al Ahorcado!")
print()

# Solicito al usario que elija una categoría.

category = int(
    input(
        "Ingrese una cateogoria: 1. Nombres de Lenguajes de Programación, 2. Términos de Programación, 3. Tipos de Datos: "
    )
)
if category == 1:
    chosen_category = "Nombres de Lenguajes de Programación"
elif category == 2:
    chosen_category = "Términos de Programación"
else:
    chosen_category = "Tipos de Datos"

# Elijo una palabra al azar de la categoría seleccionada por el usuario
word = random.choice(words[chosen_category])
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
        score += 6
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
        score -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    score = 0
print(f"Tu puntaje final es: {score}")
