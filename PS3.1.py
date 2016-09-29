def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i in lettersGuessed:
            pass
        else:
            return False
    return True
