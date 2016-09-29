#secretWord = 
global lettersGuessed

def isWordGuess(secretWord, lettersGuessed):
    for i in secretWord:
        if i in lettersGuessed:
            pass
        else:
            return False
    return True

def isLetter(secretWord, lettersGuessed):    
    if guess in lettersGuessed:
        return ("Oops! You've already guessed that letter: " + getGuessWord(secretWord, lettersGuessed))

    elif guess in secretWord:        
        return ('Good guess: ' + getGuessWord(secretWord, lettersGuessed))

    else:
        global guessesLeft
        guessesLeft -= 1
        return ('Oops! That letter is not in my word: ' + getGuessWord(secretWord, lettersGuessed))
    
def getGuessWord(secretWord, lettersGuessed):
    lettersGuessed += guess
    value = ''
    string = ''
    for i in secretWord:
        if i in lettersGuessed:
            value = i + ' '
        else:
            value = "_ " 
        string = string + value        
    return string


def getAvailLetters(lettersGuessed):
    availLetters = ''
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in lettersGuessed:
            availLetters += letter
        else:
            pass
    return (availLetters)
    
def hangman(secretWord):
    global guessesLeft
    guessesLeft = 8    
    lettersGuessed = []
    
    print ('Welcome to the game Hangman!')
    print ('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print ('-------------')
    while guessesLeft > 0:
        availableLetters = getAvailLetters(lettersGuessed)
        
        print ('You have ' + str(guessesLeft) + ' guesses left.')
        print ('Available letters: ' + (availableLetters))

        global guess
        guess = input('Please guess a letter: ').lower()

        print (isLetter(secretWord, lettersGuessed))

        print ('------------')
        
        if isWordGuess(secretWord, lettersGuessed) == True:
            print ('Congratulations, you won!')
            return
        else:
            pass
