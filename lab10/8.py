my_dict = {'item1': 3, 'item2': -5, 'item3': 20}
sums = 0
for key in my_dict:
    sums += my_dict[key]

print(sums,sum([my_dict[key] for key in my_dict]), sum())


