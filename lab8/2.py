#  s-mark.kirelos@zewailcity.edu.eg
#  12/11/22, 12:05 PM
def foo1(x):
    a = foo2(x * 2)
    return a
print(foo1(5))


def foo2(x):
    y = x + 5
    return y
# 15
# print(foo1(5))
