import math
coff = input("please enter coff seprated by space a b c: ").split()
a,b,c = int(coff[0]),int(coff[1]),int(coff[2])
if a==b==c==0:
    print("any x is solution")
elif a==b==0 and math.floor(c) == 0:
    print("no solution")
elif a ==0 and b != 0 and c != 0:
    print(-c/b)
else:
    x1 = (-b+math.sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2 - 4*a*c))/2*a
    print(x1,"\n",x2)
