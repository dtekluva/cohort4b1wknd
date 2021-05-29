# names = ["john", "slim", "kunle", "ini"]
# salaries = [23000, 23000, 50000, 13000]
# age = [23, 30,15, 32,60, 19, 32, 25]

# # append

# names.append("sam")
# salaries.append(30000)

# print(names, salaries)

# new_staff = ["josh", "evelyn", "richy"]
# new_staff_salaries = [50000, 50000, 90000]

# # for i in range(3):
# #     print(i)
# #     print(new_staff[i])
# #     names.append(new_staff[i]) 
# #     salaries.append(new_staff_salaries[i])

# # print(names)

# # REMOVE

# # names.remove("kunle")
# # print(names)

# # count

# ocurrence_count = salaries.count(50000)
# print(ocurrence_count)

# # EXTEND

# names.extend(new_staff)
# salaries.extend(new_staff_salaries)

# print(names, salaries)

# # INSERT

# names.insert(2, "talabi")
# print(names)

# # INDEX

# location_of_target = names.index("richy")
# print(location_of_target)

# # POP 

# names.pop(location_of_target) # using pop without a parameter will remove the first value.
# print(names)

# # COPY

# new_names  = names.copy()

# # SORT 

# names.sort() # sort by default will sort in ascending order
# print(names)

# names.sort(reverse=True) # sort with reverse True default will sort in descending order
# print(names)

# names.sort(key= len) # sort by names but using the length of each name hence the key "len"
# print(names)

# print(new_names)
# print(len(names), len(salaries))

# # zip

# zipped_values = zip(names, salaries) # zip just takes in the two values that need to be combined and must be lists
# list_of_zipped_values = list(zipped_values) # zip would return a generator object and must be converted into a list in other too interact with it
# print(zipped_values)
# print(list_of_zipped_values)

# list_of_zipped_values.sort(key=lambda value: value[0], reverse=True)
# print(list_of_zipped_values)

# sort_by_salary = lambda value: value[0]

# list_of_zipped_values.sort(key=sort_by_salary, reverse=True)
# print(list_of_zipped_values)


# # ZIP MORE THAN 2 LISTS

# zipped_values = zip(names, salaries, age) # zip just takes in the two values that need to be combined and must be lists
# list_of_zipped_values = list(zipped_values) # zip would return a generator object and must be converted into a list in other too interact with it
# print(zipped_values)
# print(list_of_zipped_values)

# values = [2, 3, 1, 4, 5]

# WRITE A PROGRAM TO SUM ALL ITEMS IN LIST
# total = sum(values)
# print(total)

# multiple = 1

# for value in values:
#     # print(value)
#     multiple = multiple * value

# print(multiple)


# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same

# values = ["e", "q", "ade", "z", "as", "ada", "kunle", "axa", "hannah", "an", "malam"]

# count = 0

# for value in values:

#     if len(value) > 1 and value[0] == value[-1]:
#         print(value)
#         count += 1

# print(count)

#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
    
# values = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# remove duplicates from list
# using set datastructure

# numbers = [1,2,3,4,1,1,1,2,1,3,4,1,5,3,5,6]
# non_dups = list(set(numbers))
# print(non_dups)

# # USING A FOR LOOP

# non_dups = []

# for number in numbers:
#     if number in non_dups:
#         continue
#     else:
#         non_dups.append(number)

# print(non_dups)

# Write a Python function that takes two lists and returns True if they have at least one common member.

# a = [1,2,3,4,5]
# b = [9,8,7,6,9]

# set_a = set(a) # convert lists to set in order to use intersect functionlity from sets
# set_b = set(b)

# intersect = set_a.intersection(set_b)
# print(intersect)
# print("A and B a have atleast 1 common values: ", bool(intersect))

# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)

numbers = range(1, 31)
squares = map(lambda nums: nums**2, numbers)

square_nums = lambda nums: nums**2
squares = map(square_nums, numbers)

squares_list = list(squares)
last5 = squares_list[-5:]
first5 = squares_list[0:5]

print(first5 + last5)

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