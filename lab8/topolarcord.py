#  s-mark.kirelos@zewailcity.edu.eg
#  12/11/22, 12:41 PM
import math


def recpol(x, y):
    r = math.sqrt(x**2+y**2)
    theta = math.atan(y/x)
    return r,theta
