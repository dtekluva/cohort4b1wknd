# numbers = 900000
# print(numbers)


# new_word = "My father's Car, whose brand is the same as Wole's Dad's"
# print(type(new_word))

# tricky_string = "900000"
# print(type(tricky_string))


# new_float = 7.98
# print(type(new_float))



# new_bool = False
# print(type(new_bool))



# my_list = [False, "False", True, 5, 6.2, 6.2, 6.2, True]
# print(my_list)



# my_tuple = (6.3, 6.3, "My Father's Car", False)
# print(type(my_tuple))


# my_set = {"Lagos", "Kebbi", True, 99, True, 99}
# print(my_set) 



# my_dictionary = {"Name": ("Biden", "Trump"), "Age": [77, 74], "Country": ["USA", "USA"]}
# print(my_dictionary)



# first_number = 1.0
# second_number = 1

# output = first_number + second_number
# print(output)




# x = 108
# print(x)

# x %= 13
# print(x)


# out = 10.0 != -10
# print(out)


# the_list = [100, 101, 102, "farm"]

# check1 = "farm" in the_list
# check2 = 

# print(check)


# brink = "Oesophagus"
# output = brink[-5: -2]

# print(output)



# rockstar = "Manchester United finished top"
# wallpaper = "this season with Bruno having the most goals scored with a total of"
# nutjob = 23


#using .format
# workspace1 = rockstar + " " + wallpaper + " " + "{}".format(nutjob)
# print(workspace1)

#using  f
# workspace2 = rockstar + " " + wallpaper + " " + f"{nutjob}"
# print(workspace2)



place = "Seattle"
month = "July"
duration = "forever"

full_string1 = "I would be in {} by the end of {} and I would stay {}.".format(place, month, duration)
# print(full_string1)


# full_string2 = f"I would be in {place} by the end of {month} and I would stay {duration}."
# print(full_string2)


#.title()
# new_output = full_string1.title()
# print(new_output)


#.startswith()
# new_output = full_string1.startswith("I w")
# print(new_output)


#.endswith()
# new_output = full_string1.endswith("R.")
# print(new_output)


#.index()
# new_output = full_string1.index("france")
# print(new_output)


#len()
# print(len(full_string1))


#.find()
# new_output = full_string1.find("sea")
# print(new_output)


# print(full_string1)

# mod_string = full_string1.replace("Seattle", "New York City")
# print(mod_string)

# mod_string2 = full_string1.replace(" ", "#")
# print(mod_string2)


# print(full_string1)
# print("\n")
# con_list = full_string1.split(" ")
# print(con_list)
# print("\n")

# joint_list = "#".join(con_list)
# print(joint_list)

# stripped_string = full_string1.rstrip(". ")
# print(stripped_string)

# temp = "word7."
# print(temp.isalnum())







#LISTS!
my_list = [35, "Lampard", 100, 3000, "Nathaniel", "Demilade!", True, 0.5]
# desired_output = my_list[1 : 8: 2]
# print(desired_output)


my_list[1] = "Thomas"
my_list[2 : 5] = [101, 1500, "NYC"]

# print(my_list)

my_list.append("Lagos")
# print(my_list)


temp_list = [1, 2, 3, 4, 5]

my_list.extend(temp_list)
# print(my_list)

my_list.remove("Thomas")
# print(my_list)



copied_list = my_list.copy()
# print(copied_list)

my_list.pop(0)
# print(my_list)

my_list.insert(0, 35)
# print(my_list)

my_list.insert(5, False)
# print(my_list)

occ = my_list.count("NYC")
# print(occ)

ind_pos = my_list.index(5)
# print(ind_pos)


l1 = ["me", "you", "us"]
l1.clear()
# print(l1)


# my_tuple = ("Kebbi", "Kogi", "Lagos", "Akwa Ibom", "Imo")
# desired_state = my_tuple[1]
# print(desired_state)







# one = [1, 2, 3]
# two = [1, 2, 3]
# check_one = one == two
# check_two = one is two

# print(check_one)
# print(check_two)



# one = [1, 2, 3]
# one = (1, 2, 3)
# check_one = one == one
# check_two = one is one

# print(check_one)
# print(check_two)




#Sets
grocery_cart1 = {"Milk", "Bread", "Biscuit", "Cookies", "Milo", "Eggs"}
check_bread = "bread" in grocery_cart1
# print(check_bread)


grocery_cart1.add("Coke")
grocery_cart1.add("Peanuts")
# print(grocery_cart1)


grocery_cart2 = {"Cookies", "Sweets", "Yoghurt", "Poundo", "Milk", "Bread", "Butter", "Ice cream"}
# print(grocery_cart2)


unique_cart1 = grocery_cart1.difference(grocery_cart2)
# print(unique_cart1)


backup_cart1 = grocery_cart1.copy()
backup_cart2 = grocery_cart2.copy()

# print(backup_cart1)


grocery_cart1.difference_update(grocery_cart2)
# print(grocery_cart1)


grocery_cart1.pop()
# print(grocery_cart1)

# grocery_cart1.remove("Building")
grocery_cart1.discard("Building")
# print(grocery_cart1)



# print(backup_cart1)
# print(backup_cart2)


check_unique = backup_cart1.isdisjoint(backup_cart2)
# print(check_unique)

common_grocery = backup_cart1.intersection(backup_cart2)
# print(common_grocery) 

all_groceries = backup_cart1.union(backup_cart2)
# print(all_groceries)


# backup_cart1.update(backup_cart2)
# print(backup_cart1)

sym_grocery = backup_cart1.symmetric_difference(backup_cart2)
# print(sym_grocery)

backup_cart1.symmetric_difference_update(backup_cart2)
# print(backup_cart1)

backup_cart2.clear()
# print(backup_cart2)




#Dictionaries
cust_info = {
    "Name" : ["Charlotte", "Ngozi", "Putin", "Arteta", "Chan"],
    "Nationality" : ["USA", "Nigeria", "Russia", "Spain", "China"],
    "Gender" : ["Female", "Female", "Male", "Male", "Male"],
    "Age" : [19, 21, 76, 38, 51],
    "Weight" : [55.0, 80.5, 70.3, 75.9, 62.6]
}

# print(cust_info)

name_entries = cust_info["Name"]
# print(name_entries)


name_entries[1] = "Amaka"
# print(cust_info)


name_entries_get = cust_info.get("Name")
# print(name_entries_get)

cust_info_items = cust_info.items()
print(cust_info_items)





















