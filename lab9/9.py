#  s-mark.kirelos@zewailcity.edu.eg
#  12/18/22, 12:00 PM

def sumOflist(l):
    if len(l) == 1: return l[0]
    return l.pop() + sumOflist(l)


print(sumOflist([1, 2, 3, 4]))
