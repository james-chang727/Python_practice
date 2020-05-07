import random

## Checks the two guesses entered by the user against the two randomly generated numbers.
# @params answerA the first answer
# @params answerB the second answer
# @params guessA the first guess
# @params guessB the second guess
# @return True or False
#
def guessesOk(answerA, answerB, guessA, guessB):
    okSameOrder = guessA == answerA and guessB == answerB
    okOtherOrder = guessA == answerB and guessB == answerA
    return okSameOrder or okOtherOrder

def outputYes():
    print("\tCorrect - well done!\n")

def outputNo(firstAnswer, secondAnswer):
    print(f'\tNo, the answers were {firstAnswer} and {secondAnswer}.\n')


def main() :
    MIN = 1
    MAX = 3
    
    firstAnswer = random.randrange(MIN, MAX + 1)
    secondAnswer = random.randrange(MIN, MAX + 1)
    
    firstGuess = int(input("\n\tGuess the first number between {} and {}: ".format(MIN, MAX)))
    secondGuess = int(input("\n\tGuess the second number between {} and {}: ".format(MIN, MAX)))

    if guessesOk(firstAnswer, secondAnswer, firstGuess, secondGuess):
        outputYes()
    else:
        outputNo(firstAnswer, secondAnswer)

# Start the program
if __name__ == "__main__":
    main()