#  s-mark.kirelos@zewailcity.edu.eg
#  12/18/22, 1:34 PM

def multiAll(l):
    if not l:
        return 1
    return l.pop() * multiAll(l)



print(multiAll([1,2,3,4,5]))

