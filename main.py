# if 7 or 11 PLAYER win
# if 2 or 3 or 12 CASINO win
# if in first roll 4, 5, 6, 8, 9, 10 is GOAL
# if roll 7 PLAYER loes
# if roll GOAL PLAYER win

import random


# Rolling Craps
def RollCraps():
    result1 = random.randint(1, 6)
    result2 = random.randint(1, 6)
    return result1, result2


def StepRollResult():
    firstDice, secondDice = RollCraps()
    return {'message': f"The sum of dice is {firstDice} + {secondDice} = {firstDice + secondDice}",
            'first': firstDice,
            'second': secondDice,
            'result': firstDice + secondDice}


def StepWinLogic(rollData, isFirstBool=True):
    print(rollData, isFirstBool)


def GameRooles():
    print()


def Tutorial():
    answer = input("Did you know game rules? Y/N ")

    if answer.lower() == "y":
        print("Game starting...")
    elif answer.lower() == "n":
        print("The player should roll two dice. If the sum of both of them is 7 or 11 the player wins.\nIf the sum "
              "is 2, 3 or 12 (craps) the casino wins. If during the first roll the sum is 4, 5, 6, 8, 9 or 10, tha"
              "t number becomes the “goal” number.\nTo win, the player should roll the dice till they roll the goal"
              " number again. If the player rolls a 7 before rolling the goal number, they lose.")
    else:
        answer = input("Choose one of answers Y/N")


def GameStart(devMod=False):
    if not devMod:
        Tutorial()


GameStart()
