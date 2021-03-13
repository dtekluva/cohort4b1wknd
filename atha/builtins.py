# number = -20

# print("Original- :", number)
# print("Abs - ", abs(number))

# numbers = [2,4,1,7,2,2,10]
# print(min(numbers)) # 

# numbers = [2,4,1,7,2,2,10]
# print(max(numbers))

# # print(max("AsholankeP"))
# # print(max("Aa"))

# name = "           Adefarasin Adebayo"
# print(len(name))

# stuff = ["shoe", "bags", "belts", ["rice", "beans", "garri"]]
# print(len(stuff))

file = open("atha/journal.txt", "r")
# print(file) # returns a raw object that has not been read
# # print(file.read())
# print(type(file.read()))

data =  file.read()
print(len(data))

val = "32"
casted_val= int(val) # type casting in this case from string to integer

print(val * 2)
print(casted_val * 2)