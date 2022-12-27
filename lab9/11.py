#  s-mark.kirelos@zewailcity.edu.eg
#  12/18/22, 1:37 PM
def countList(l):
    if not l:
        return 0
    return 1*(l.pop() % 2 == 0) + countList(l)


print(countList([1,2,3,4,5,6,8]))
