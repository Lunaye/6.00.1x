def updateHand(hand, word):
    new_hand = hand.copy()
    for key in hand:
        for letter in word:
            if letter == key:
                new_hand[letter] -= 1
    return new_hand
