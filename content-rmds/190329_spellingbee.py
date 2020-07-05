# -*- coding: utf-8 -*-
"""
author: mleary
date: 4/6/2019

"""

import pandas as pd
import numpy as np

""" RIDDLER: 
    
https://fivethirtyeight.com/features/can-you-win-a-spelling-bee-if-you-know-99-percent-of-the-words/

You are playing your first ever game of “Ticket to Ride,” a board game in which 
players compete to lay down railroad while getting so competitive they risk 
ruining their marriages. At the start of the game, you are randomly dealt a set
 of three Destination Tickets out of a deck of 30 different tickets. Each reveals
 the two terminals you must connect with a railroad to receive points. During 
 the game, you eventually pick up another set of three Destination Tickets, so 
 you have now seen six of the 30 tickets in the game.

Later, because you enjoyed it so much, you and your friends play a second game. 
The ticket cards are all returned and reshuffled. Again, you are dealt a set of 
three tickets to begin play. Which is more likely: that you had seen at least 
one of these three tickets before, or that they were all new to you?

"""
# Simulation approach
def generate_games():
    game_1 = np.random.choice(range(30), 6, replace=False)
    game_2 = np.random.choice(range(30), 3, replace=False)
    seen = sum(np.in1d(game_2, game_1))
    
    if seen > 0:
        result = True
    elif seen == 0:
        result = False
    
    return(result)
    
def main():
   df = pd.DataFrame(columns = ["Seen_Previously"])
   for i in range(20000):   
       run = generate_games()
       df = df.append({"Seen_Previously" : run}, ignore_index=True)
   result = sum(df["Seen_Previously"]) /  len(df["Seen_Previously"])
   print(result)
   
main()

# Math Approach

# Change of picking all new cards
all_new = (24/30)*(23/29)*(22/28)

# So the the odds of picking a new previously seen card is 1 - odds of picking 
# all new cards
seen_before = 1 - all_new

print(seen_before)

 """
 Answer: Simuation yield a result of ~50.2%.  Calculating the odds exactly place
it at 50.14%, confirming the simulation approach. 