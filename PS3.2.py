def getGuessedWord(secretWord, lettersGuessed):
    value = ''
    guess = ''
    for i in secretWord:
        if i in lettersGuessed:
            value = i + ' '
        else:
            value = "_ " 
        guess = guess + value        
    return guess
