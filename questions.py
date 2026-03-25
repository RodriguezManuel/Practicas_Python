import random

words = {
    "Nombres de Lenguajes de Programación": ["python"],
    "Términos de Programación": ["programa", "variable", "funcion", "bucle"],
    "Tipos de Datos": ["entero", "lista", "cadena"],
}

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

# Pongo todas las palabra de la categoría seleccionada por el usuario en una variable para luego hacer el sample
words_bag = words[chosen_category]

# Seteo el maximo de rondas que se puden jugar en esa categoria, dada las palabras que contiene esta.
max_rounds_to_play = len(words_bag)

# Solicito al usuario que elija cuantas rondas quiere jugar entre 1 y el maximo de rondas que se pueden jugar en esa categoria.
rounds_to_play = int(
    input(
        f"¿Cuántas rondas querés jugar?, Como maximo podes jugar {max_rounds_to_play} rondas "
    )
)
while (
    rounds_to_play < 1 or rounds_to_play > max_rounds_to_play
):  # Me aseguro que el usuario ingrese un numero entre 1 y el maximo de rondas que se pueden jugar en la categorai escogida.
    rounds_to_play = int(
        input(
            f" Entrada no valida!!! Por favor, ingrese un número entre 1 y {max_rounds_to_play}: "
        )
    )
selected_words = random.sample(
    words_bag, rounds_to_play
)  # Elijo las palabras al azar de la categoria seleccionada por el usuario, sin que se repitan, y las guardo en una lista.
final_score = 0
for i in range(rounds_to_play):
    guessed = []
    attempts = 6  # intentos
    round_scoring = 0
    word = selected_words[
        i
    ]  # Seleccion aleatoramiente la palabra a adivinar en esa ronda.
    print(
        f" Comienza la ronda {i + 1} de {rounds_to_play} "
    )  # Informo al usuario que numero de ronda esta jugando y cauntas restan por jugar.
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
            round_scoring += 6
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
            round_scoring -= 1
            print("Esa letra no está en la palabra.")
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        round_scoring = 0
    final_score += round_scoring
print(
    f"Tu puntaje final es: {final_score}"
)  # El score final se calcula sumando la puntuacion de cada ronda.
