#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM
N = int(input("Please enter a number"))
for i in range(1,N+1):
    for l in range(1,i+1):
        print(i*l, end="\t")
    print("")
