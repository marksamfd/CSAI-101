#  s-mark.kirelos@zewailcity.edu.eg
#  12/18/22, 11:57 AM

def sumofPower(n):
    if n==0:
        return 0
    else:
        return n**2 + sumofPower(n-1)

print(sumofPower(5))
