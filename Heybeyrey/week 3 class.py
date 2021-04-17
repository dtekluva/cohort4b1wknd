# print (1, end="\n")
# print (1)
info1 = "this is my class"
inf02 = "why are you fine"
print("info1","inf02", end="\n that's all")

print("ade","me","you", sep = ",,")
print("ade","me","you", sep = "/")

message1 = "this is me"
message2= "thanks"
file= open("message.txt", "w")
print(message1,message2,file=file)

message1 = "1,2,3,4"
message2= "5,6,7,8"
file= open("excel.csv", "w")
print(message1,message2,file=file)

# message1 = "1,2,3,4"
# message2= "5,6,7,8"
# file= open("excel.csv", "a")
# print(message1,message2,file=file)

message1 = "1,2,3,4"
message2= "5,6,7,8"
file= open("excel.csv", "w")
print(message1,message2,file=file)

message1 = "1,2,3,4"
message2= "5,6,887,7uy8"
file= open("excel.csv", "a")
print(message1,message2,file=file)

Story= "I see, I saw. \nI saw snake agwo. \nI carry knife nma. \nTo kill snake agwo. \nSnake make ee die \tonwu, \tonwu, \tonwu"
file_story=open("story.txt","w")
print(Story, file=file_story)

Story= "I see, I saw. \nI saw snake agwo. \nI carry knife nma. \nTo kill snake agwo. \nSnake make ee die \tonwu, \tonwu, \tonwu.\nnma gi odikwa nko nawa."
file_story=open("story.txt","a")
print(Story, file=file_story)

# print (1, end="\n")
# print (1)
info1 = "this is my class"
info2 = "why are you fine."

# print(info1, inf02, end="\t that all")
# print(info1)
# print()
# print (inf02)

# print(info1, end = "\n\n")
# print (inf02)

print(info1, info2, sep="\n")
# print (inf02)
# print(info1, info2, end="\n")

x=2
z=4/2
print(x==z)
hprint(x is z)
y=5
numerator = (2*x)+(x**5)/((61**0.5)-18)
denominaator = (20**6)/(4*y)+(x*y)
print(numerator/denominaator)


import datetime
print(datetime.datetime.now())

num= [778,657,7647,874]
# print (abs(num))
print(min(num))


# file = open("atha/journal.txt", "r")
# print(file)
# print(file.read())

val = "32"
casted_val= int(val)
print(val*2)
print(casted_val*2)

# file = open("jojo.txt", "r")
# print(file)
# print(file.read())

file = open("message.txt", "r")
print(file)
print(file.read())