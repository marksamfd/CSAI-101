#  s-mark.kirelos@zewailcity.edu.eg
#  12/11/22, 12:01 PM

def myfun1():
    x = input("Enter List x:").split()
    s = 0
    for i in range(len(x)):
        s = s + int(x[i])
    return s
