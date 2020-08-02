import random
def getSecretNum(numDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return (secretNum)
def getClues(guess,secretNum):
    if guess == secretNum:
        print('You got it!')
    clue = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
        elif guess != secretNum:
            clue.append("Bagel")  
        if len(clue) == 0:
            return 'None'
    return (clue)
def isOnlyDigits(num):
  if num == '':
    print(False)
  for i in num:
    if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
      return False
def playAgain():
    play = input("Do you want to play again? Yes or No?") 
    play.startswith('y')
NUMDIGITS = 3
MAXGUESS = 3
print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  None       No digit is correct.')
def process():
  secretNum = getSecretNum(NUMDIGITS)
  print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
  numGuesses = 1
  print(secretNum)
  while numGuesses <= MAXGUESS:
      print ('Guess' + str(numGuesses))
      guess = input("Guess Again")
      clue = getClues(guess, secretNum)
      print(clue)
      numGuesses += 1
      if guess == secretNum:
        break
  if guess != secretNum:
    print ('You ran out of guesses. The answer was ' + secretNum)
  guess2 = input("you want to play again: y/n :")
  if guess2 == "y":
    process()
process()


