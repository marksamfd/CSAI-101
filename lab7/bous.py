#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

f = open("text.txt", "r")
sum = 0
for i in f.readlines():
    sum += len(i.split())
