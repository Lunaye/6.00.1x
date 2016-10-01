def dotProduct(listA, listB):
    total = 0
    x = 0
    for each in listA:
        total += each * listB[x]
        x += 1

    return (total)
