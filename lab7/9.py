file = open("./covid19.txt")
cases = []
infected = []
sum = 0
statsFile = ""
maxInfect,minInfect = 0,0
for line in file:
    cases.append(line.split(" "))
file.close()
for iC in range(1, len(cases)):
    for i in range(1, len(cases[iC])):
        """cases[iC][i] = cases[iC][i].split(",")
        cases[iC][i] = "".join(cases[iC][i])
        cases[iC][i] = int(cases[iC][i])"""
        cases[iC][i] = cases[iC][i].replace(",", "")
        cases[iC][i] = int(cases[iC][i])

for iC in range(1, len(cases)):
    percentInfect = (cases[iC][3] / (cases[iC][1] - cases[iC][2])) * 100
    infected.append(percentInfect)
    print(f"{cases[iC][0]} \t %5.2f%% \t\n" % percentInfect)
    statsFile += f"{cases[iC][0]} \t %5.2f%% \t\n" % percentInfect
    sum += (cases[iC][1])

avg = sum / (len(cases) - 1)
statsFile += f"avarge => {avg} sum={sum}"
file = open("covid19Stats.txt", "w")
file.write(statsFile)
print(cases, sum, avg, end="\t")

char="ATCGA"
     #TAGCT
i ={"A":"T","C":"G","T":"A","G":"C"}
new = ""
for c in char:
    char.replace(c,i[c])
print(new)

"Hello".replace(" ",",")