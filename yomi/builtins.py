# # MAP TAKES IN A FUNCTION AND AN ITERABLE AND CARRIES OUT THE FUNCTION ON EVERY MEMBER OF THE ITERABLE

# words = ["salami", "tunde", "salau", "winston", "john"]

# length_of_words = map(len, words)
# mapped_object = length_of_words
# unravelled_object = list(mapped_object)
# print(unravelled_object)

# reversed_words = map(reversed, words)

# def reverse_for_real(value):
#     return list(reversed(value))

# mapped_object = map(reverse_for_real, words)

# unravelled_object = list(mapped_object)
# print(unravelled_object)

# def add_number(name):
#     return name + "->" + str(len(name))

# print(list(map(add_number, words)))
# ab = [2, 5, 7, 3, 7]

# def square_rt(square):
#     return square**2

# print(list(map(square_rt,ab)))

# string = "I am a boy and my name is james"
# string2 = "       Jonah"
# lower_case_version = string.lower()
# print(lower_case_version)

# upper_case_version = string.upper()
# print(upper_case_version)

# print(string2)
# print(string2.strip())

# print("Welcome to my small program \n")
# Date_to_change = input("Please enter date (YYYY-MM-DD) : ")
# DOB = Date_to_change.split("-")

# print(DOB)
# print(DOB[0])
# print(DOB[1])

# year_of_birth = int(DOB[0])
# age = 2021 - year_of_birth
# print("Hello you are", age, "years old")

# num1 = input("Please enter num1 > ")
# num2 = input("Please enter num2 > ")

# print(num1, num2)
# print(int(num1) + int(num2))
# print(int(num1) * int(num2))


# char_count = input("Type Charcter to be counted: ")
# print(len(char_count))

# action = input("what will you like to do no?\n\nA: Simple Interest\nB: Candy Crusher\n\n")

# if action == "A":
#     Principal = input("Please insert The Principal: ")
#     Rate = input("Please input the rate: ")
#     time = input("Please input the time in years: ")

#     Interest = (int(Principal) * float(Rate) * int(time))/100
#     Total_Payable = int(Principal) + int(Interest)
#     print("The Interest for this transaction is", Interest)
#     print("The Total amount Payable would be", Total_Payable)

# if action == "B":
#     Friend1 = input("How Many sweets did friend 1 bring: ")
#     Friend2 = input("How many sweets did friend 2 bring: ")
#     Friend3 = input("How many sweets did friend 3 bring: ")

#     perperson = (int(Friend1) + int(Friend2) + int(Friend3))/3
#     remainder = (int(Friend1) + int(Friend2) + int(Friend3)) % 3
#     # import math
#     # f,i = math.modf(perperson)
#     print("Shared equally, each of you should get", int(perperson), "sweets and probably discard", remainder, "to avoid a fight")

# if action!= "A" or action != "B":
#     print("INVALID SELECTION")

# x = 5
# y = 0

# if x < y:
#     print('yes')
# else:
#     print("no")

# val_a = int(input("Please Enter Value A: "))
# val_b = int(input("Please Enter Value B: "))

# if val_a > val_b:
#     print(val_a, "is Larger than", val_b)
# else:
#     print(val_b,  "is Larger than", val_a)


# word = input("Please type your first and last name: ")

# if len(word) < 6:

#     if word.startswith ("A") and word.endswith ("t"):
#         print("Weldone", word, "starts with 'A' and ends with 't'")
#     else:
#         print("Ehya, not today")
# else:
#     print("Sorry, one or more criterias not met")

# import datetime
# current_time = datetime.datetime.now()
# # print(current_time)

# seconds = current_time.second
# print(seconds)

# if seconds <= 30:
#     print("First Half")
# else: 
#     print("Second Half")

# sugesstion = input ("Type your word: ")
# reversed_suggestion = (list(reversed(sugesstion)))
# join_word = "".join(reversed_suggestion)
# if  sugesstion == join_word:
#     print(sugesstion, "is a palindrome")
# else:
#     print(sugesstion, "is not a palindrome")

# a = ['Fizz', 'baz', 'buzz']
# while a:
#     print(a.pop(1))


# b = 0
# while b < 20:
#     b += 1
#     print(b)


# c = [5, 10, 30, 40]
# added = 0
# while c:
#     d = c.pop()
#     added += d
# print(added)

import datetime
import time

# while True:

#     current_time = datetime.datetime.now()
# # print(current_time)

#     print(current_time.hour, current_time.minute, current_time.second, sep = ":")
#     time.sleep(1)

# num = 500
# max_num = 1000

# while num < max_num:

#     if num != 0 and num %3 == 0 and num %32 == 0:
#         print("Found! Our number is", num)
#         break

#     num += 1

# else:
#     print("Sorry number matches your description")

# mins = 2
# sec = 0

# while mins > -1:
#     while sec > 0:
#         print(mins, "mins:", sec, "secs")
#         sec -= 1
#         time.sleep(1)

#     sec = 60
#     mins -= 1
 
# items_found = 0

# for i in range(1500, 2701):
#     if (i%7 == 0) and (i%5 == 0):
#         # print(i)
#         items_found += 1
# print(items_found)


items = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
print( ",".join(items))
