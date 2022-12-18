#  s-mark.kirelos@zewailcity.edu.eg
#  12/11/22, 12:49 PM

def scoreToGrade(score):
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif score < 60:
        return "F"
