#  s-mark.kirelos@zewailcity.edu.eg
#  12/11/22, 1:05 PM

def getInput():
    angle = 0
    validAngle = False
    msg = "Please enter angle: "
    while not validAngle:
        angle = int(input(msg))
        if 0 < angle <= 360:
            validAngle = True
            return angle
        else:
            msg = "Incorrect, Please enter angle: "
