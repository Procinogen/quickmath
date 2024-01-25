#time bonus score function: m(x) = 2^(-x + 2.5) + 1

class scoreBoard:
    score = 0
    timeAtLastPlay = 0
    questionsSinceLastIncorrect = 0
    bonus = 1
    lastAddedScore = 0
    @classmethod
    def init(cls):
        from time import time
        cls.score = 0
        cls.timeAtLastPlay = time()

    @classmethod
    def addscore(cls, shouldAdd):
        from time import time
        wasCorrect = False
        currentTime = time()
        if shouldAdd:
            # get the score without any multipliers
            rawscore = (5 ** (-(currentTime - cls.timeAtLastPlay) + 1) + 1) 
            cls.questionsSinceLastIncorrect += 1
            
            #Check for streaks
            if cls.questionsSinceLastIncorrect >= 20:
                cls.bonus = 3
            elif cls.questionsSinceLastIncorrect >=10:
                cls.bonus = 2
            elif cls.questionsSinceLastIncorrect >= 5:
                cls.bonus = 1.5
            else:
                #Reset bonus multiplier if there's no streak
                cls.bonus = 1
            #Add score
            cls.lastAddedScore = (round(rawscore * 4)/4)*cls.bonus
            cls.score += cls.lastAddedScore
            wasCorrect = True
        else:
            #Reset streak counter if the user's answer is wrong
            cls.questionsSinceLastIncorrect = 0
            cls.lastAddedScore = 0
        cls.timeAtLastPlay = time()
        return wasCorrect
    
    @classmethod
    def showScore(cls):
        print(f"\n**Current score: {cls.score}**\n")

def compareUserInput(query, comparison):
    if type(comparison) is not int:
        #exit("'comparison' should be numeric - something went wrong!")
        print("ERROR!\n'comparison' should be numeric - something went wrong!")
        return False
    userInput = input(str(query) + '\n')
    #if not userInput.isnumeric():
    #    return False
    # Read somewhere that the python way of doing things to try anyways and ask for forgiveness when it fails
    # Fair enough, works decently well, lol
    try:
        return int(userInput) == comparison
    except ValueError:
        return False

def mainLoop(maxInt):
    from random import randint
    x = randint(1, maxInt)
    y = randint(1, maxInt)
    operator = randint(1, 4)
    match operator:
        case 1: 
            return compareUserInput(f"{x} + {y} = ?", (x + y))
        case 2:
            return compareUserInput(f"{x} - {y} = ?", (x - y))
        case 3:
            return compareUserInput(f"{x} * {y} = ?", (x * y))
        case 4:
            while(x % y != 0):
                y = randint(1, maxInt)
            
            return compareUserInput(f"{x} / {y} = ?", int(x / y))
            
if __name__ == "__main__":
    import sys
    from colorama import Fore, Style, just_fix_windows_console
    just_fix_windows_console()
    playerScore = scoreBoard()
    playerScore.init()
    print("-+-+-+-+ WELCOME TO QUICKMATH +-+-+-+-\n\n")
    try:        
        # Insist on an integer
        maximumCount = input("Please choose a maximum number for the equations.\n")
        while not maximumCount.isnumeric():
            maximumCount = input("Please choose a maximum number for the equations.\n")
        print("\n\n")
        while True:
            if playerScore.addscore(mainLoop(int(maximumCount))):
                print("\n" + Fore.GREEN + "☑ CORRECT ☑" + Style.RESET_ALL + f"  +{playerScore.lastAddedScore}")
                if playerScore.bonus >= 1.5:
                    print(Fore.YELLOW + f"{playerScore.questionsSinceLastIncorrect} streak!" + Style.RESET_ALL)
                    print(Fore.YELLOW + f"{playerScore.bonus}x multiplier!" + Style.RESET_ALL)
            else:
                print("\n" + Fore.RED + "☒ INCORRECT ☒" + Style.RESET_ALL)
            playerScore.showScore()
    except KeyboardInterrupt:
        print(f"\n-+-+-+-+-+-\n\nFINAL SCORE {playerScore.score}")
        print("\nCLOSING...\nTHANK YOU FOR PLAYING")
    sys.exit(0)