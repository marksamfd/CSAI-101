alphabets = "abcdefghijklmnopqrstuvwxyz"
alphabetsCap = "ABCDEFGHIJKLMOPQRTUZWXYZ"
nums = "0123456789"
chars = "$#@"
passwordNotCorrect = True
message = "Insert the suggested password:"
numsB,charsB,alpaB,alphaCB = False,False,False,False
while(passwordNotCorrect):
    password = input(message)
    if 6<=len(password)<20:
      for c in alphabets:
        if c in password: 
            alpaB = True
            break
      for c in alphabetsCap:
        if c in password:
            alphaCB = True
            break
      for c in nums:
        if c in password:
            numsB = True
            break        
      for c in chars:
        if c in password:
            charsB = True
            break           
      if numsB and charsB and alpaB and alphaCB:
        passwordNotCorrect = False
        print("Password assignment is done! Thanks.")
    else:
         message = "Invalid Password, kindly try again:"
         passwordNotCorrect = True

#Happy$Zewailian20

""" for c in password:
    if c in alphabets: alpaB = True
    if c in alphabets: alpaB = True
    if c in alphabets: alpaB = True
    if c in alphabets: alpaB = True """
    