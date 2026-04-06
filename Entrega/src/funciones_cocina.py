def beginning_round(round_actual, number_of_rounds):
    print(
        f"Ronda {number_of_rounds}: {round_actual['theme']}"
    )  # Indica que ronda se juega y el tipo de plato
    scores = round_actual["scores"]  # Me traigo todo los puntajes
    round_winner = ""
    highest_score = -1  # Por cada ronda se resetea
    return scores, round_winner, highest_score


def score_max(round_score, highest_score, participant, round_winner):
    if round_score > highest_score:  # Entra si tiene el mayor puntaje en la ronda
        highest_score = round_score  # Actualizo el maximo
        round_winner = participant  # Actualizo al ganador parcial de la ronda
    return highest_score, round_winner


def update_maxscore(Standings, round_score, participant):
    if round_score > Standings[participant]["Mejor ronda"]:
        Standings[participant]["Mejor ronda"] = round_score


def update_average(Standings, participant, number_of_rounds):
    Standings[participant]["Promedio"] = (
        Standings[participant]["Puntaje"] / number_of_rounds
    )


def print_standings(Standings):
    print("Tabla de posiciones:")
    for participant, stats in Standings:
        print(
            f"{participant}: Puntaje total: {stats['Puntaje']}, Mejor ronda: {stats['Mejor ronda']}, Promedio: {stats['Promedio']:.2f}\n"
        )
