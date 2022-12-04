#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

sal = input('Enter salaries:').split()
tax = float(input('enter tax:'))
salAfterTax=[]
for v in sal:
    x = int(v) - (int(v) * tax)
    salAfterTax.append(x)
print(salAfterTax)
