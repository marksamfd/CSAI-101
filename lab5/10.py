#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

num = int(input("please enter number:"))
factorial = 1

while num>=1:
    if factorial <1_000_000:
        factorial *= num
        num-=1
    else:
        print("factorial exceeds 1,000,000")
        break

print(factorial)
