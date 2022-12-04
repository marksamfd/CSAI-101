f = open("text.txt", "r")
sum = 0
for i in f.readlines():
    sum += len(i.split())
