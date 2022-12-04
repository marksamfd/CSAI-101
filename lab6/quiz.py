num = int(input("Please enter a number: "))
fact = 1
c = 1
while (fact <= 1_000_000) and (c <= num):
    fact *= c
    c += 1
if fact <= 1_000_000:
    print(fact)
else:
    print("Factorial excedes the limit")
