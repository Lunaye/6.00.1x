def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand_copy = dict(hand)
    if word not in wordList:
        return False           
    for char in word:            
        if char not in hand:
            return False
        elif hand_copy[char] == 0:
            return False
        else:
            hand_copy[char] = hand_copy[char] - 1
    return True
