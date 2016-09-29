def getAvailableLetters(lettersGuessed):
    availLetters = ''
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in lettersGuessed:
            availLetters += letter
        else:
            pass
    return (availLetters)
