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
x = int(input("Input student's score to get grade?: "))
if x>=70:
    print(f"{nameof} got Grade A in {subject}")
elif x >=50:
    print(f"{nameof} got Grade B in {subject}")
elif x>=30:
    print(f"{nameof} got Grade C in {subject}")

