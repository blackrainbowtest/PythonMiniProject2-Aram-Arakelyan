import random


PLAYER_WIN = [7, 11]
CASINO_WIN = [2, 3, 12]
PLAYER_LOSE = [7]


# Rolling Craps
def RollCraps():
    result1 = random.randint(1, 6)
    result2 = random.randint(1, 6)
    return result1, result2


def StepRollResult():
    firstDice, secondDice = RollCraps()
    message = f"The sum of dice is {firstDice} + {secondDice} = {firstDice + secondDice}"
    result = firstDice + secondDice
    return firstDice, secondDice, result, message


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


def GameWinnerLogic(isFirstStep, goal):
    status = False
    player = False
    casino = False
    playerGoal = goal
    firstDice, secondDice, result, message = StepRollResult()
    print(message)
    if isFirstStep:
        if result in PLAYER_WIN:
            status = True
            player = True
        elif result in CASINO_WIN:
            status = True
            casino = True
        else:
            print(f"Now your goal number is {result}")
            playerGoal = result
    else:
        if result in PLAYER_LOSE:
            status = True
            casino = True
        elif result == playerGoal:
            status = True
            player = True
    return status, player, casino, playerGoal


def GameStepLogic():
    isFirstStep = True  # Начинаем с первого шага
    playerGoal = 0
    status, player, casino, goal = GameWinnerLogic(isFirstStep, playerGoal)
    playerGoal = goal

    while not status:
        # Делаем следующий шаг в игре, возможно, здесь должны быть действия игры
        isFirstStep = False  # Следующие шаги уже не являются первыми
        status, player, casino, goal = GameWinnerLogic(isFirstStep, playerGoal)
        playerGoal = goal

    if player:
        print("You wins!")
    elif casino:
        print("You lose!")
    else:
        print("Game continues...")


def GameStart(devMod=False):
    if not devMod:
        Tutorial()
    GameStepLogic()


GameStart()
