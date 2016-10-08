def getWordScore(word, n):
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES.get(letter)
    score = score * len(word)
    if len(word) == n:
        score += 50
    return score
