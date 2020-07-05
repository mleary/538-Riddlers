"""
author: matt leary
date: October 2, 2019
link: https://fivethirtyeight.com/features/which-baseball-team-will-win-the-riddler-fall-classic/
"""
import numpy as np

'''
Riddler Express:

If a baseball team is truly .500, meaning it has a 50 percent chance of winning each game, what’s the probability that
it has won two of its last four games and four of its last eight games?
'''


def simulate_game():
    result = np.random.choice(2, 1)
    return result


def generate_8_games():
    gameResults = np.array([])
    for games in range(8):
        gameOutcome = simulate_game()
        gameResults = np.append(gameResults, gameOutcome)
    return gameResults


def check_results(iterationarray):
    first_4_games = np.sum(iterationarray[0:3]) == 2
    all_games = np.sum(iterationarray) == 4
    result = first_4_games == True & all_games == True
    return result


def record_overall_results():
    finalResults = np.array([])
    for trial in range(1000000):
        trialGames = generate_8_games()
        trialResult = check_results(trialGames)
        finalResults = np.append(finalResults, trialResult)
    percent_truly_500 = np.sum(finalResults) / sum(finalResults.shape)
    return percent_truly_500


'''
What is the result?
'''
record_overall_results()
