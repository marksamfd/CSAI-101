#  s-mark.kirelos@zewailcity.edu.eg
#  12/11/22, 1:24 PM

def reverseString(str):
    return str[::-1]
def reverseString2(str):
    arr = []
    for i in range(len(str)-1,-1,-1):
        arr.append(str[i])
    return "".join(arr)


def joinHash(str):
    return "#".join(str)

print(reverseString2("HELLO"))
