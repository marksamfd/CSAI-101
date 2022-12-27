#  s-mark.kirelos@zewailcity.edu.eg
#  12/18/22, 11:25 AM
"f".lower()
def isequi(str1,str2):
    if len(str1) == len(str2):
        str1 = str1.lower()
        str2 = str2.lower()
        if str1 == str2: return True
    else:
        return False

#print(isequi("MohaMed AhMed","mohamed ahmed"))
#print(isequi("Mohamed AhMed","Muhammad Ahmed"))
