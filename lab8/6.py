#  s-mark.kirelos@zewailcity.edu.eg
#  12/11/22, 12:57 PM

from scoreToGrade import scoreToGrade
# 74 82 41 55 68 98
scores = input("please enter grades").split()

grade = [scoreToGrade(int(score)) for score in scores]

print(grade)
