# CONCATENATING>>>REPLACING>>>SLICING>>>INDEXING

word1 = "ebere"
word1 = "      ebere".strip()          # this is stripping ie stripping off white spaces
word1= "E" + word1[1:]         #this is both replacement, concatenating and slicing
word2= "opara"
concat = word1 + " " + word2       #this is concatenating
# print(concat)
word1[2:5]          # this is slicing
word1[-3]             #this is indexing (+ve and -ve indexing is permissible)
print(word1[2:5])
print(word1.lower())      #string methods = .lower(), .upper(), .now(), .rstrip(), .lstrip(), .strip(), .startswith(), .endswith(), .find(), .replace(),
print(word1.endswith("re")) 
print(word1.endswith("re"))


#HOW TO DEFINE NEW FUNCTION USING MAPPING
word= "salewa"
print(len(word))
words=("salami","ade","tunde","ayo")
# print(list(map(len,words)
# print(list(list((map(revds)))


def newfunction(response):                 #create a new function known as response
    return list(reversed(response))        #command is to return the list of the reversed of that response
mapping = map(newfunction, words) #since you cannot directly print return,you map the titles"newfunction" to "words"
print(list(mapping))                       #then you print the mapping as a list.


words= ("salami","ade","tunde","ayo")
def newfunction(new_name):
    return "Mr." + new_name     #we are not using brackets here because these are not inbuilt functions
mapping= map(newfunction,words)
print(list(mapping))


words= ("salami","ade","tunde","ayo")
def newfunction(add_lenght):
    what_to_return = add_lenght + "->" + str(len(add_lenght))
    return  what_to_return                               #pls note, return does not have any sigh but def has this :
    # return str(add_lenght) + "=" + str(len(add_lenght))   #or you can delete the first 2lines above and run this
mapping= map(newfunction,words)
print(list(mapping))

# string ="I am a nuy and a boy and a girl".upper()
# print(string)

string ="I am a nuy and a boy and a girl".replace("boy","nuy").replace("girl","nuy")    
print(string)     #this is how to replace multiple words with one word, just keep doing the .replace("","").replace("","")


# DOB=input("insert your year: ")   #first thing is to define your variable(s) as input(s)
# print("I was born in", DOB)

#simple interest assignment
# P= float(input("what is your principal?: "))
# R=float(input("what is your rate?: "))
# T=float(input("what is your time?: "))
# Simpleinterest= (P*R*T)/36000
# totalamount= Simpleinterest + P
# print("Simpleinterest = ", Simpleinterest)
# print("totalamount = ", totalamount)


#candy assignment
# friend1 = float(input("friend1 candy? : "))        #to convert all lines to float at the sametime, just highlight all, place your cursor where you wanna make change then and start typing, all will change.
# friend2 = float(input("friend2 candy? : "))
# friend3 = float(input("friend3 candy? : "))
# shareeach = round((friend1 + friend2 + friend3)/3,1)
# print(shareeach)
# print(round(shareeach,1))
# Modulus_remainder= round(shareeach%3,1)
# print(Modulus_remainder)
# print(f"you guys should take {shareeach} sweets each, and throw the remaining {Modulus_remainder} away.")


# DICT TAKES KEYWORD ARGUMENTS AND CREATES A DICTIONARY OUT OF THEM
my_students = dict(ali = 1000, kunle = 22111, sam = 90000, sola = 320100)
print(my_students)
print(my_students["kunle"])
