#  s-mark.kirelos@zewailcity.edu.eg
#  12/4/22, 12:35 PM

s = "Hello. My name is ahmed. I am from Cairo"
a = s.split()
b = s.split(",")
c = s.split(".")
d = s.split(". ")
print(s)  #
print(a)  # ["Hello.","My","name","is","ahmed.","I","am","from","Cairo"]
print(b)  # ["Hello My name is ahmed. I am from Cairo"]
print(c)  # ['Hello', ' My name is ahmed', ' I am from Cairo']
print(d)  # ['Hello', 'My name is ahmed', 'I am from Cairo']
