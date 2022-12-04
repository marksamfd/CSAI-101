#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

prompt = "y"
numbers = []
while prompt == "y":
    N = int(input("please enter a number: "))
    if N != 0:
        numbers.append(N)
    prompt = input("Do you wish to continue? <Y/N>:")

if len(numbers) > 0:
    sum = 0
    for num in numbers:
        sum += num
    print("the average is", sum // len(numbers))
else:
    print("the average is", numbers[0])
