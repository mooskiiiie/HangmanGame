import random
import time


hangman = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''

words = 'BASTY NIKKI BODIE APPLE BANANA KIWI LAPTOP CHARGER CHOOBS DUTERTE LOCKDOWN VACCINE COVID CEDRIC PILLOW QUICKLINK ELEPHANT NEXTPAY PYTHON INTRODUCTION FUNCTIONS'.split() # list of words for random use
alphabetBig = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split() 
alphabetSmall = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
invalidInputs = '1 2 3 4 5 6 7 8 9 0 - + = [ ] | { } ; : , . > < ? / ! @ # $ % ^ & * ( )'.split() # list of invalid inputs
score1 = 0 # keeps track of user1's score
score2 = 0 # keeps track of user2's score
new = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split() # list of alphabet for unused letters


class color:
   PURPLE = '\033[95m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

def getRandomWord(wordList): # this function generates a random word from the list
    wordIndex = int(random.random() * 21 - 1)
    return wordList[wordIndex]

def swapLetter(guess, alphabetBig, alphabetSmall): # this function converts a small letter to big letter
    result = ''
    for i in range(len(alphabetSmall)):
        if alphabetSmall[i] == guess:
            result += alphabetBig[i]
    return result

def swapLetterTwo(guess, alphabetBig, alphabetSmall): # this function converts a big letter to small letter
    result = ''
    for i in range(len(alphabetSmall)):
        if alphabetBig[i] == guess:
            result += alphabetSmall[i]
    return result

def swap(upperCaseWord, alphabetBig, alphabetSmall): #this function converts the secret word into lowercase
    i = 0
    smallWord = ''
    while i < len(upperCaseWord):
        z = ''
        z += upperCaseWord[i]
        for x in range(len(alphabetBig)):
            if alphabetBig[x] == z:
                smallWord += alphabetSmall[x]
            elif alphabetSmall[x] == z:
                smallWord += alphabetBig[x]
            else:
                None
        i += 1
    return smallWord

def swapTwo(upperCaseWord, alphabetSmall, alphabetBig): # this function converts a lowercase input into an uppercase word
    i = 0
    bigWord = ''
    while i < len(upperCaseWord):
        z = ''
        z += upperCaseWord[i]
        for x in range(len(alphabetSmall)):
            if alphabetSmall[x] == z:
                bigWord += alphabetSmall[x]
                return True
            elif alphabetBig[x] == z:
                bigWord += alphabetBig[x]
                return False
        i += 1
    
def repeated(usedLetters, guess): # this function checks for used letters
    for i in range(len(usedLetters)):
        if usedLetters[i] == guess:
            return True

def dashes(upperCaseWord, lowerCaseWord, blank, guess): # this function updates the blank
    result = ''
    for i in range(len(upperCaseWord)):
        if upperCaseWord[i] == guess:
            result += guess
        elif lowerCaseWord[i] == guess:
            result += swapLetter(guess, alphabetBig, alphabetSmall)
        else:
            result += blank[i]
    return result

def correctGuess(upperCaseWord, lowerCaseWord, guess, usedLetters): # this function checks if the guess is in the word
    for i in range(len(upperCaseWord)):
        if upperCaseWord[i] == guess or lowerCaseWord[i] == guess:
            usedLetters.append(upperCaseWord[i])
            usedLetters.append(lowerCaseWord[i])
            return True

def wrongGuess(upperCaseWord, lowerCaseWord, guess, usedLetters): # this function checks if the guess is not in the word
    for i in range(len(upperCaseWord)):
        if upperCaseWord[i] != guess or lowerCaseWord[i] != guess:
            usedLetters.append(guess) and  usedLetters.append(a)
            a = swapLetterTwo(guess, alphabetBig, alphabetSmall)
            b = swapLetter(guess, alphabetBig, alphabetSmall)
            usedLetters.append(a)
            usedLetters.append(b)

def invalidGuess(invalidInputs, guess): # this function checks if the guess is inside the invalid list
    for i in invalidInputs:
        if i == guess:
            return True
        

def unusedLetters(guess, alphabetSmall, alphabetBig, guesses, new, usedLetters): # this function returns all unused letters
    f = ''
    for i in range(len(alphabetSmall)):
        if alphabetSmall[i] == guess or alphabetBig[i] == guess:
             new[i] = '' #list of alphabet (capital)
        else:
             f += new[i]
    return f
    

print('''
      █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█
      ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█''')
print(color.BLUE + '''
      ██████╗░░█████╗░░██████╗████████╗██╗░░░██╗
      ██╔══██╗██╔══██╗██╔════╝╚══██╔══╝╚██╗░██╔╝
      ██████╦╝███████║╚█████╗░░░░██║░░░░╚████╔╝░
      ██╔══██╗██╔══██║░╚═══██╗░░░██║░░░░░╚██╔╝░░
      ██████╦╝██║░░██║██████╔╝░░░██║░░░░░░██║░░░
      ╚═════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░░░╚═╝░░░'''+color.END)
print('''
                 ▄▀█ █▄░█ █▀▄
                 █▀█ █░▀█ █▄▀''')
print(color.RED + '''
      ███╗░░██╗██╗██╗░░██╗██╗░░██╗██╗██╗░██████╗
      ████╗░██║██║██║░██╔╝██║░██╔╝██║╚█║██╔════╝
      ██╔██╗██║██║█████═╝░█████═╝░██║░╚╝╚█████╗░
      ██║╚████║██║██╔═██╗░██╔═██╗░██║░░░░╚═══██╗
      ██║░╚███║██║██║░╚██╗██║░╚██╗██║░░░██████╔╝
      ╚═╝░░╚══╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░╚═════╝░''' +color.END)
print('''
    █░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█   █▀▀ ▄▀█ █▀▄▀█ █▀▀
    █▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█   █▄█ █▀█ █░▀░█ ██▄''')

time.sleep(1)
print(f'''\n\n LET\'S PLAY HANGMAN! {hangman}''' )
time.sleep(1)

user1 = input('\n \nEnter the name of the player giving the word: ') # name of player giving the word
user2 = input('Enter the name of player guessing the word: ') # name of guesser

def main(score1, score2, new): # hangman game
    print('')
    decision = (input(f'{user1}, would you like us to give {user2} a random word? Yes or No? ')) 

    if decision == 'Yes' or decision == 'yes' or decision == 'YES': # determines if user wants a random word
        wordUpper = getRandomWord(words) # the word to be guessed
        upperCaseWord = list(wordUpper)
        wordLower = swap(upperCaseWord, alphabetBig, alphabetSmall)  # lowercase of word to be guessed
        lowerCaseWord = list(wordLower)
        win = False
        blank = '-' * len(wordUpper)
        print('\nThe word to be guessed by', user2, 'is', color.BOLD + wordUpper + color.END)
        guesses = int(input('Please enter the number of guesses allowed: ')) # no. of guesses
        usedLetters = []
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        print(color.BOLD +f'\nPlease pass the game to {user2}' + color.END)
        time.sleep(1)
        print('\n \n \n \n \n')        
    
    else: # if user does not want a random word
        wordUpper = input(f'Please enter a word for {user2} to guess: ') # the word to be guessed
        upperCaseWord = list(wordUpper)
        wordLower = swap(upperCaseWord, alphabetBig, alphabetSmall) # lowercase or uppercase of word to be guessed
        lowerCaseWord = list(wordLower)

        if swapTwo(upperCaseWord, alphabetSmall, alphabetBig) == True: # only works if user inputted a lowercase word
            wordUpper = wordLower
            upperCaseWord = list(wordUpper)
            wordLower = swap(upperCaseWord, alphabetBig, alphabetSmall) # converts wordUpper into lowercase
            lowerCaseWord = list(wordLower)
            win = False
            blank = '-' * len(wordUpper)
            guesses = int(input('\nPlease enter the number of guesses allowed: '))
            print('\n')
            print(color.BOLD +f'\nPlease pass the game to {user2}' + color.END)
            usedLetters = []
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'       

        elif swapTwo(upperCaseWord, alphabetSmall, alphabetBig) == False: # only works if user inputted a uppercase word
            wordUpper = wordUpper
            upperCaseWord = upperCaseWord
            wordLower = wordLower
            lowerCaseWord = lowerCaseWord
            win = False
            blank = '-' * len(wordUpper)
            guesses = int(input('Please enter the number of guesses allowed: '))
            print('\n')
            usedLetters = []
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'     
           
    print('Choices: ',alphabet)
    print('Guess the word,', guesses, 'guesses left:', blank, '\n')

    while not win and guesses > 0:
        guess = input('Please guess a letter: ')  # this is the guess                 

        if repeated(usedLetters, guess): # checks if guess was repeated
            print(color.BOLD+ f'You already guessed that letter, {guesses} guesses left: {blank} \n' + color.END)
            print('Choices: ', unusedLetters(guess, alphabetSmall, alphabetBig, guesses, new, usedLetters)) # returns unused letters
            
        elif correctGuess(upperCaseWord, lowerCaseWord, guess, usedLetters): # check if guess is correct
            blank = dashes(upperCaseWord, lowerCaseWord, blank, guess)
            print(color.BOLD + f'Good job, {guess} is in the word! {guesses} guesses left: {blank}' + color.END)
            print('')
            print('Choices: ' , unusedLetters(guess, alphabetSmall, alphabetBig, guesses, new, usedLetters))
            
            if blank == wordUpper:
                print(f'''
              *•.¸(*•.¸♥¸.•*´)¸.•*´
 ♥«´¨`•°..Congrats, {user2}, you won Hangman!..°•´¨`»♥
            .¸.•*(¸.•*´♥`*•.¸)`*•.
            
        \n           Better luck next time, {user1}.''')
                win = True
                
                if win == True:
                    score2 += 1 # updates scoreboard
                    print(user1, '-', str(score1))
                    print(user2, '-', str(score2))
                    new = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split() # restart the value of new         

            if win:
                playAgain = input('\nWould you like to play again? Yes or No? \n')

                if playAgain == 'Yes' or playAgain == 'yes' or playAgain == 'YES': # restarts the game
                    main(score1, score2, new)
                else:
                    print('\nThank you for playing', color.BLUE + color.BOLD + 'BASTY' + color.END + color.END, 'and', color.RED +  color.BOLD + 'NIKKI\'S' + color.END + color.END, 'HANGMAN')
                    None
        
        else:
            if len(guess) != 1: # checks if guess is more than 2 letters
                print(color.BOLD + f'Please enter a single letter. {guesses} guesses left: {blank} '+ color.END)
                print('')
                print('Choices: ',unusedLetters(guess, alphabetSmall, alphabetBig, guesses, new, usedLetters))
            
            elif invalidGuess(invalidInputs, guess): # check if guess is invalid
                print(color.BOLD + f'Invalid Input. {guesses} guesses left: {blank}' + color.END)
                print('')
                print('Choices: ', unusedLetters(guess, alphabetSmall, alphabetBig, guesses, new, usedLetters))

            else:
                wrongGuess(upperCaseWord, lowerCaseWord, guess, usedLetters) # checks if guess is incorrect
                guesses -= 1
                print(color.BOLD + f'{guess} is not in the word {guesses} guesses left: {blank}' + color.END)
                print ('')
                print('Choices: ', unusedLetters(guess, alphabetSmall, alphabetBig, guesses, new, usedLetters))
               

    if guesses == 0: # if player ran out of guesses
        print(f'''\n {user2} You ran out of guesses and got hanged! The word was {wordUpper}.''', hangman)
        if win == False and guesses == 0:
            score1 = score1 + 1
            print(f'''
              *•.¸(*•.¸♥¸.•*´)¸.•*´
    ♥«´¨`•°..Congrats, {user1}, you won!..°•´¨`»♥
            .¸.•*(¸.•*´♥`*•.¸)`*•.
            
        \n      Better luck next time, {user2}.''')
            print(user1, '-', str(score1))
            print(user2, '-', str(score2))
            new = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
       
        playAgain = input('\nWould you like to play again? Yes or No? \n')
        if playAgain == 'Yes' or playAgain == 'yes' or playAgain == 'YES':
            unusedLetters(guess, alphabetSmall, alphabetBig, guesses, new, usedLetters)
            main(score1, score2, new)
        else:
            print('\nThank you for playing!', color.BLUE + color.BOLD + 'BASTY' + color.END + color.END, 'and', color.RED +  color.BOLD + 'NIKKI\'S' + color.END + color.END, 'HANGMAN')
            None


main(score1, score2, new)


    

# Sources:
#    - discussions with Sir Albert Medalla
#    - https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python

        

