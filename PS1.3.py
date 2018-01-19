#s = 'azcbobobegghakl'

s = s + '1'
wordlist = []
word = str(s[0])
x = 0
limit = len(s)
while (x + 1) < limit:
    if s[x] <= s[x+1]:
        word += s[x+1]

    else:
        wordlist.append(word)
        word = s[x+1]

    x += 1

print('Longest substring in alphabetical order is: ' + (max(wordlist, key=len)))
