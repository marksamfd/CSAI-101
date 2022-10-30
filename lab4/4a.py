items = input("What did team members bring? ").split()
batteryFound = False
for item in items:
    if item == "battery":
        batteryFound = True
if batteryFound:
    print("I don’t need to bring the battery")
else:
    print("I will need to bring the battery")
