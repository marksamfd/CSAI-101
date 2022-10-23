value = int(input('Enter a value:'))
L = input('Enter list of values:').split()
c = 0
for i in L:
    if int(i) >= value:
        c = c + 1

if c == len(L):
    print('All item are greater')
else:
    print(c)
