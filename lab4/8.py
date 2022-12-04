#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

naderMind = input("what is in nader's mind?: ")
naderFriends = input("Who are nader's Friens?: ").split(",")
naderPresents = input("What did they bring?: ").split(",")
presentFound = False
for i in range(len(naderPresents)):
    if naderMind == naderPresents[i]:
        print("Oh", naderFriends[i],"Thank you Friend :)")
        presentFound = True
        break

if not presentFound:
    print("Oops, Sorry none")
