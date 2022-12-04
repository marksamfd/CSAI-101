#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

num = input("please enter number ")
for i in range(int(num)+1):
    if i%5 == 0 and i%3 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
