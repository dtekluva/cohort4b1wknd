# names = ["john", "slim", "kunle", "ini"]
# salaries = [23000, 1000, 23000, 50000, 13000]

# #append

# names.append("sam")
# salaries.append(30000)

# print(names,salaries)

# new_staff= ["josh", "evelyn", "richy"]
# new_staff_salaries = (100000, 120000, 90000)

# for i in range(3):
#     print(i)

#     print(new_staff[i])
#     names.append(new_staff[i])

# print(names)

# for i in range(3):
#     print(i)

#     print(new_staff_salaries[i])
#     salaries.append(new_staff_salaries[i])
#     names.append(new_staff[i])
# print(salaries)
# print(names)

#TO BE CONTINUED
# names = ["john", "slim", "kunle", "ini"]
# salaries = [23000, 1000, 23000, 50000, 13000]
# job_title = ["Manager","Technician","General","CSO","Chef"]


# names.append("sam")
# salaries.append(30000)

# print(names,salaries,job_title)

# new_staff= ["josh", "evelyn", "richy"]
# new_staff_salaries = (100000, 120000, 90000)
# new_job_title = ["Developer", "Auditor","Comptroller"]

# print(new_staff_salaries[i])
#     salaries.append(new_staff_salaries[i])
#     names.append(new_staff[i])
# print(salaries)
# print(names)

# --------------------------------------

names = ["john", "slim", "kunle", "ini"]
salaries = [23000, 23000, 50000, 13000]
# age = 


new_staff= ["josh", "evelyn", "richy"]
new_staff_salaries = (100000, 120000, 90000)

#REMOVE

for i in range(3):
    print(i)
    print(new_staff[i])
    salaries.append(new_staff_salaries[i])
    names.append(new_staff[i])
    

# names.remove("kunle")
# print(names)

#COUNT

occurence_count = salaries.count(23000)
print(occurence_count)

#extend



#INSERT

# names.insert(2,"talabi")
# print(names)

#index - this gets the location of a particular thing

# location_of_target = names.index ("john")
# print(location_of_target)
# I HAVE A QUESTION

#POP

# names.pop(location_of_target)
# print(names)


#SORT

names.sort()
print(names)

names.sort(reverse=True)

names.sort(key=len)


#ZIP

zipped_values = zip(names,salaries)
list_of_zipped_values = list (zipped_values)
print(zipped_values)
print(list_of_zipped_values)

list_of_zipped_values.sort (key=lambda value: value[0]) 
print(list_of_zipped_values)



