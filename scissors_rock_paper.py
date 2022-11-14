import random

scissors = "s"
rock = "r"
paper = "p"

Tie = "Tie"
win = "YOU WIN!"
lose = "YOU LOSE!"

def compare_moves(you, Computer):
    if you == Computer:
        return Tie
    elif you == scissors and Computer == paper:
        return win
    elif you == rock and Computer == scissors:
        return win
    elif you == paper and Computer == rock:
        return win
    else:
        return lose


you = ""


while you not in [scissors, paper, rock]:
    you = input("(s)cissors, (r)ock, or (p)aper? > ")


Computer = random.choice([scissors,rock,paper])
result = compare_moves(you, Computer)


print(f"You: {you}, Computer: {Computer}. {result}")
   
