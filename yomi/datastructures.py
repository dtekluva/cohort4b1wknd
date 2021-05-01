names = ["john", "slim", "kunle", "ini"]
salaries = [23000, 23000, 50000, 13000]
age = [23, 30,15, 32,60, 19, 32, 25]

# append

names.append("sam")
salaries.append(30000)

print(names, salaries)

new_staff = ["josh", "evelyn", "richy"]
new_staff_salaries = [50000, 50000, 90000]

# for i in range(3):
#     print(i)
#     print(new_staff[i])
#     names.append(new_staff[i]) 
#     salaries.append(new_staff_salaries[i])

# print(names)

# REMOVE

# names.remove("kunle")
# print(names)

# count

ocurrence_count = salaries.count(50000)
print(ocurrence_count)

# EXTEND

names.extend(new_staff)
salaries.extend(new_staff_salaries)

print(names, salaries)

# INSERT

names.insert(2, "talabi")
print(names)

# INDEX

location_of_target = names.index("richy")
print(location_of_target)

# POP 

names.pop(location_of_target) # using pop without a parameter will remove the first value.
print(names)

# COPY

new_names  = names.copy()

# SORT 

names.sort() # sort by default will sort in ascending order
print(names)

names.sort(reverse=True) # sort with reverse True default will sort in descending order
print(names)

names.sort(key= len) # sort by names but using the length of each name hence the key "len"
print(names)

print(new_names)
print(len(names), len(salaries))

# zip

zipped_values = zip(names, salaries) # zip just takes in the two values that need to be combined and must be lists
list_of_zipped_values = list(zipped_values) # zip would return a generator object and must be converted into a list in other too interact with it
print(zipped_values)
print(list_of_zipped_values)

list_of_zipped_values.sort(key=lambda value: value[0], reverse=True)
print(list_of_zipped_values)

sort_by_salary = lambda value: value[0]

list_of_zipped_values.sort(key=sort_by_salary, reverse=True)
print(list_of_zipped_values)


# ZIP MORE THAN 2 LISTS

zipped_values = zip(names, salaries, age) # zip just takes in the two values that need to be combined and must be lists
list_of_zipped_values = list(zipped_values) # zip would return a generator object and must be converted into a list in other too interact with it
print(zipped_values)
print(list_of_zipped_values)