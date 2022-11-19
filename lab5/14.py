alphabets = "abcdefghijklmnopqrstuvwxyz"
alphabetsCap = "ABCDEFGHIJKLMOPQRTUZWXYZ"
nums = "0123456789"
chars = "$#@"
passwordNotCorrect = True
message = "Insert the suggested password:"
checks = 0
while(passwordNotCorrect):
    password = input(message)
    if 6<=len(password)<20:
        if any(c in alphabets for c in password) and any(c in alphabetsCap for c in password) and any(c in nums for c in password) and any(c in chars for c in password):
            passwordNotCorrect = False
            print("Password assignment is done! Thanks.")
        else:
            message = "Invalid Password, kindly try again:"  

    else:
         message = "Invalid Password, kindly try again:"
         passwordNotCorrect = True

#Happy$Zewailian20