num="300"
print(num*4)
converted_num=int(num)
print(converted_num)

num="300.565"
print(num*4)
converted_num=float(num)
print(converted_num*6)

my_number= range(10,20)
print(my_number)

leapyears=range(1980,2020,5)
print(list(leapyears))

leapyears=range(1980,2020,5)
print(tuple(leapyears))

leapyears=range(1980,2020,5)  #this is called a generator
print(set(leapyears))

myname="ebere"
Reversing_my_name=reversed(myname)
print(list(Reversing_my_name))

pi=22/7
print(pi)
rounded=round(pi,3)
print(rounded)

number=(7,76,90,3,0,2)
print(sorted(number))
print(sum(number))

students=[["ade,90"],["sam,66"],["john,99"],["lisa,77"]]
print(sorted(students))     #it has sorted it by names. To sort by the figures, we'll get there later

# students=dict(["ade,90"],["sam,66"],["john,99"],["lisa,77"]]
# print(students)
# print(students["ade"])

print(bool(1))
print(bool(-1))
print(bool( ))
print(bool(0))
print(bool(["ade"]))
print(bool(""))
print(bool(" "))

words=("salami","ade","tunde","ayo")
lenght_of_words= map(len,words)
print(list(lenght_of_words))

words=("salami","ade","tunde","ayo")
lenght_of_words= map(len,words)
mapped_object=lenght_of_words
unravelled_obj=list(mapped_object)
print(unravelled_obj)
reversed_words=map(reversed,words)

def reverse_for_real(value):
    return list(reversed(value))

mapped_object=map(reverse_for_real, words)
unravelled_obj=list(mapped_object)
print(unravelled_obj)

print(list(lenght_of_words))

# words=("salami","ade","tunde","ayo")
# lenght_of_words= map(len,words)
# print(reversed(lenght_of_words))     #TypeError: 'map' object is not reversible. with this error message, that is why we started building in a new function on python to help solve this. In building a new function, we use "def" and "return"
# so now, we wanna create a new function that can use map to add "Mr" to all the iterative item in words.


words=("salami","ade","tunde","ayo")
def add_salutation(name):
    name_plus_salutation= "Mr " + name
    return name_plus_salutation
saluted_name = add_salutation("name")
print(saluted_name) 
print(list(map(add_salutation,words)))


#classwork on creating a new function using map
namess=("salami","ade","tunde","ayo")
def add_lenght(namess):
    name_plus_lenght= namess + "->" + "(len(namess))"
    return name_plus_lenght
print(list(map(add_lenght, namess)))

names=("salami","ade","tunde","ayo")
def addlenght(names):
    name_plus_lenght= names + "->" + str(len(names))
    return name_plus_lenght
print(list(map(addlenght, names)))      

# names=("salami","ade","tunde","ayo")
# def add_lenght(names):
#     name_plus_lenght= names + "->" + str(len(names))
#     return name_plus_lenght
# print(list(map(names,add_lenght)))        #this will give you an error, coz all functions first before the names)

# mylist= [2,5,7,3,7]
# def raisedtopowerof2(mylist):
#     mylist_plus_power= mylist + str(**2)    this will give an error coz we are adding a string to an integer/list
#     return mylist_plus_power
# print(list(map(raisedtopowerof2, mylist)))


mylist= [2,5,7,3,7]
def raisedtopowerof2(mylist):
    mylist_plus_power= mylist ** 2        #note, we did not add the + str( **2) coz we expect to see just the end product of the operation. moreso, since adding it will give you an error.
    return mylist_plus_power
print(list(map(raisedtopowerof2, mylist)))

string ="I am a nuy and a boy and a girl"
lower_case_version= string.lower()
print(string.lower())
print(lower_case_version)

upper_case_version= string.upper()
print(string.upper())
print(upper_case_version)

string2= "      jonh    "
print(string2.strip())

replaced_version = string.replace("boy","girl")
print(replaced_version)


Splitted_string = string.split(" ")
print(Splitted_string)

csv="a,b,c,d,e,f"
splitted_csv = csv.split(",")
# print(splitted_csv)
# print(",".join(splitted_csv))

# # age =32
# # print("your age is", age)
# # age = input("please insert your age : ")
# # print("your age is ", age)

# wordss= "welcome to my string splitter"
# print("welcome to my string splitter \n")

# # input function
# # wordsss= input("please enter the word to be inputted : ")          #N/B: this is the input message you would like to see the terminal
# # print("you are", wordsss)

# date_of_birth=input("enter your DOB : ")    #the : is just what you wanna see beneath. mmeans nothing
# print("my date of birth is", date_of_birth)

# splitted_value = date_of_birth.split("-")
# print(splitted_value)
# print(splitted_value [0])
# print(splitted_value [1])
# print(splitted_value [2])

# YOB=int(splitted_value[0])
# age=2022-YOB
# month=int(splitted_value[1])
# print("Hello, you are", age, "years old. And you are born on the", month, "month")


num1=input("pls insert num1 here > ")          #num 1=2 and num2=3
num2=input("pls insert num2 here > ")
print(num1,num2)
print(int(num1)+int(num2))
print(int(num1)*int(num2))

input()          #this is to call up the interactive script from the system folder




































