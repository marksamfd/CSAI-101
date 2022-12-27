dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dictN1= {}
for key in dict1:
    dictN1[key] = dict1[key]
   
for key in dict2:
    dictN1[key] = dict2[key]
   
dictN = dict1.copy()
dictN.update(dict2.copy()) 
print(dictN, dictN1)