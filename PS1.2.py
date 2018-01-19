#s = 'azcbobobegghakl'

a = 0
b = 3
strlen = len(s)
count = 0
while b <= strlen:
    if s[a:b] == 'bob':
        count += 1
    a += 1
    b += 1

print('Number of times bob occurs is: ' + str(count))
