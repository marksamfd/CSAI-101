#  s-mark.kirelos@zewailcity.edu.eg
#  12/11/22, 12:08 PM

def angleType(A):
    if A == 0:
        return "zero"
    elif 0 < A < 90:
        return "acute"
    elif A == 90:
        return "right"
    elif 90 < A < 180:
        return "obtuse"
    elif A == 180:
        return "straight"
    elif 180 < A < 360:
        return "reflex"
    elif A == 360:
        return "complete"


def generalAngleType(B):
    if B < 0:
        return "negative"
    elif 0 <= B <= 360:
        return angleType(B)
    elif B > 360:
        return angleType(B % 360)


print(generalAngleType(810))
