# # # APPEND:
# # names = ["john", "slim", "kunle", "ini"]
# # salaries = [23000, 1000, 23000, 50000, 13000]
# # names.append("sam")
# # salaries.append(30000)

# # print(names, salaries)

# # new_staff = ["josh", "evelyn", "richy"]
# # new_staff_salaries = [100000, 120000, 90000]

# # # for i in range(3):
# #     # print(i)
# #     # print(new_staff[i])
# #     # names.append(new_staff[i])

# # # print(names)

# # for i in range(3):
# #     print(new_staff_salaries[i])
# #     salaries.append(new_staff_salaries[i])

# # print(salaries)


# # for i in range(3):
# #     print(new_staff_salaries[i])
# #     names.append(new_staff[i])
# #     salaries.append(new_staff_salaries[i])

# # print(names, salaries)


# # # names.remove('john')
# # # print(names)


# # salary_count = salaries.count(50000)
# # print(salary_count)

# # # .extend is a shorter form for the whole for loop we used above
# # names.extend(new_staff)
# # salaries.extend(new_staff_salaries)
# # print(names, salaries)


# # names.insert(2, "talani")
# # print(names)

# # # to find the index location from a list
# # target_location =names.index('josh')
# # print(target_location)

# # # names.pop(2)
# # # print(names)


# # # names.pop(target_location)
# # # print(names)


# # names.sort()    # sort by default
# # print(names)

# # names.sort(reverse=True)    # to sortby reverse
# # print(names)


# # names.sort(key=len)    # to sort by lenght
# # print(names)


# # ZIP FUNCTION

# names = ["john", "slim", "kunle", "ini"]
# salaries = [23000, 23000, 50000, 13000]
# Ages = [34,65,57,90]
# zipped_value = zip(names,salaries,Ages)       # so we can zip more than 2 line items, you can also zip tuples 
# print(list(zipped_value))

# list_of_zipped_values = list(zipped_value)    #omo, me I dinnor understand this one
# list_of_zipped_values.sort(key=lambda names:names[1], reverse=True)
# print(list_of_zipped_values)


# # WRITE A PROGRAM TO SUM AND MULTIPLY

# # SUM:
# values = [2,3,1,4,5]
# total = sum(values)
# print(total)

# multiple = 1 
# for x in values:
#     print(x)
#     multiple = multiple * x
# print (multiple)

# print(max(values))


# # pls copy Atha's note on the exercise on list line 111 ie on the count of string whose index[0] == index[-1]
# # pls copy Atha's note on the exercise on list line 125 ie on sorting in increasign order by the index [-1] element

# values = [(2,5), (1,2), (4,4), (2,3), (2,1)]
# values.sort(key= lambda values:values[-1])     # lambda is used to create an analymous function
# print(values)


# values = [(2,5), (1,2), (4,4), (2,3), (2,1)]       
# values.sort(key= lambda values:values[-1], reverse=True)    # note the difference
# print(values)


numbers = [1,1,2,2,3,3,34,4,4,5,5,5,6,6,6,7,7,7,8,8,8]
remove_duplicate = set(numbers)        # set does not entertain duplicates. note this
print(remove_duplicate)
print(list(remove_duplicate))          # you can also convert to list if you wanna
print(set(numbers))                  # you can also do this directly

non_dups = [ ]
for i in numbers:
    if numbers in non_dups:
        continue
    else: 
        non_dups.append(numbers)
print(non_dups)


a = [1,2,3,4,5]
b = [9,8,7,6,5]

set_a = set(a)
set_b = set(b)
intersect = set_a.intersection((set_b))    # so we have used the .intersect, .union function
print(intersect)
print(bool(intersect))


# windows+V = get out all items in your clip  board

numbers = range(1, 31)
squares = map(lambda nums:nums**2, numbers)
# ORRRR
square_num = lambda nums:nums**2
squares = map(square_num, numbers)

square_list = list(squares)
last5 = square_list[-5:]
first5 = square_list[0:5]
print(first5, last5)
print(first5 + last5)






















































































