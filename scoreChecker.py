# Joshua Schoonmaker
# Week 11 Assignment
# CIS_125
# Tests the Imputed Game to see if the score is correct

# Read in the text file and BowlingGame
from BowlingGame import Game

file = open("testscores.txt", "r")

# Calculate Correct score using BowlingGame.py
# Loop through each line of the file

for line in file:
    line = line.strip()
    lineList = line.split(",")
    lineList = [int(i) for i in lineList]
    endScore = lineList.pop()
    game = Game()
    for roll in lineList:
        game.roll(roll)
    score = game.score()
   

# Print correct and incorrect score with snarky comment

    print("Calculated score = {}. The provided score was {}.".format(score, endScore))
    if score == endScore:
        print("Hooray you gave me a correct input for once.  Congratulations.")
    else:
        print("Someone doesn't know how to score bowling.  Had it been correct, you would have gotten:", score)

# Close files

file.close