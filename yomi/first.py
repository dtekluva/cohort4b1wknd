# print("hello")

# values = [2, 3, 1, 4, 5]

# sorted_values = values.sort(reverse=True)

# print(values)
# print(max(values))

# values = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# values.sort(key = lambda values: values[1])
# print(values)


# def check_them (lista, listb):
    
#     set_a = set(lista)
#     set_b = set(listb)

#     intersect = set_a.intersection(set_b)
#     print(intersect)
#     print("A and B a have atleast 1 common values: ", bool(intersect))

# check_them([2,3,4,5,6], [3,4,5,6,7])


# def case_counter(string):
#     uppercase = 0
#     lowercase = 0

#     for char in string:
#         if char.islower():
#             lowercase += 1
#         elif char.isupper():
#             uppercase += 1
#     print("Lower Case", lowercase, "Upper Case", uppercase)


# case_counter("The Quick Brown Fox")




# a= input("Math score: ")
# d = input("English score: ")
# e = input("French score: ")
# b = "Mk scored the following;"
# c = " and his cummulative is;"
# f = int(a) + int(d) + int(e)
# print(b, a, d, e, c, f)

# a=int(input("sweet set A:"))
# b=int(input("sweet set B:"))
# c=int(input("sweet set C:"))
# Total_sweet=int(a)+int(b)+int(c)
# Each_person_gets=(Total_sweet//3)  # get floor division
# sweet_remaining=(Total_sweet%3)  
# print ("Total sweet=",Total_sweet)

# print ("Each gets=", Each_person_gets)
# print("Remainder=", sweet_remaining)
f= 10
# f+=80
# print(f)
# a=[1,5,"girl","python",3.40,"she", "like"]
# print(1 is not a)
# y=10
# z=30
# # print(f = z)

# a=[2,4,6,8,10]
# # print(max(a))

# b = " Oyin is a girl"
# print(b)
# newb = b.replace("Oyin","Yomi")
# newb1=newb.replace("girl", "boy")
# print(newb1) 
# y= "oyin is a 10 Years Old girl"
# print (y.swapcase())
# print(y.title())
# print(y.capitalize())
nameof= input("Input Student name: ")
subject= input("Input student's Subject: ")
g1 = "Grade A"
g2 = "Grade B"
g3 = "Grade C"
g4 = "Ungraded"
x = int(input("Input student's score to get grade?: "))


students = {}

def determine_grade(x): # TAKE SCORE AND CREATE CORRESPONDING GRADE USING IF STATEMENT

    grade = False

    if x>=70:
        print(f"{nameof} got {g1} in {subject}")
        grade = g1
    elif x >=50:
        print(f"{nameof} got {g2} in {subject}")
        grade = g2
    elif x>=30:
        print(f"{nameof} got {g3} in {subject}")
        grade = g3
    elif x==0:
        print(f"{nameof} got {g4} in {subject} because e be mumu ")
        grade = g4

    return grade


check = { # CREATE A SMALLER DICTIONARY FOR SCORE AND GRADE
    "score":x,
    "grade":determine_grade(x)
}

students[nameof] = check # CREATE A KEY IN THE MAIN DICTIONARY WITH THE CORRESPONDING USER'S NAME AS REQUIRED
print(students)

file = open("file.csv", "a") # OPEN FILE THAT WE WOULD WRITE OUR CALUES INTO
file.write(f"{nameof},{x},{determine_grade(x)}\n") # WRITE VALUES INTO THE FILE AS COMMA SEPERATED VALUES.

# dict={'name':'Yomi','age':'30','sex':'male'}
# print (dict['name'])
# print(dict['sex'])