vowels = ["a","e","i","o","u"]
str = input("enter a word: ")
c = 0
#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

# for v in str:
#     for cv in vowels:
#         if v == cv:
#             c = c+1
# if c == 0:
#     print("no vowels found")
# else:
#     print(c)
#

for v in str:
    if v in vowels:
        c+=1
if c == 0:
    print("no vowels found")
else:
    print(c)
