

# values = [1,2,3,4,5]

#WRITE A PROGRAME TO SUM ALL ITEMS IN A LIST
# total = sum(values)
# print(total)

#WRITE A PROGRAME TO MULTIPLY ALL ITEMS IN A LIST

# multiple = 1

# for value in values:
#     # print(value)
#     multiple = multiple * value

# print(multiple)

# PROGRAM TO GET THE LARGEST NUMBER FROM A LIST

# values.sort() 
# print(values)
# print(values[-1])
# #OR
# max(values)

#Q5-WRITE A PROGRAME THAT CAN COUNT THE NUMBER OF STRINGS MORE THAN 2 VALUES AND THAT THEIR FIRST AND LAST CHARACTERS ARE THE SAME

# values = ["e", "q","ade","ada","kunle","axa","hannah","an"]
# for value in values:
#     if len(value) > 1 and value[0] == value[-1]:
#         print(value)
#         count=+1
# print(count)


#Q WRITE A PYTHON PROGRAM TO GET A LIST, SORTED IN INCREASING ORDER BY THE LAST ELEMENT IN EACH TUPLE FROM A GIVEN LIST OF NON-EMPTY TUPLES.

# values = [(2,5), (1,2), (4,4), (2,3), (2,1)]

# sort_by_second_val = lambda value: value[1]

# values.sort(key=sort_by_second_val)
# print(values)

#Q WRITE A PYTHON PROGRAM TO REMOVE DUPLICATES FROM ANY PYTHON LIST


# numbers = [1,2,3,4,1,1,1,1,2,1,3,4,1,5,3,5,6]
# non_dups = set(numbers)    #WE CONVERTED TO A SET BECAUSE SETS DO NOT ACCEPT DUPLICATES SO IT AUTOMATICALLY THROWS THEM OUT

# #OR

# non_dups = list(set(numbers)) # WE HAVE TO CHANGE IT BACK TO A LIST AS WE HAVE BEEN WORKING WITH LISTS
# print(non_dups)

# #OR LET US USE FOR=LOOP

# non_dups = []

# for number in numbers:
#     if number in non_dups:
#         continue
#     else:
#         non_dups.append(number)
# print(non_dups)

#WRITE A PYTHON FUNCTION THAT TAKES TWO LISTS AND RETURNS TRUE IF THEY HAVE AT LEAST ONE COMMON CHARACTER

# a = [1,2,3,4,5]
# b = [9,8,7,6,5]

# set_a = set(a) 
# set_b = set (b)

# intersect = set_a.intersection(set_b)
# print(intersect)

# print("A and B have at least 1 common values: ",bool(intersect))

#Q WRITE A

# numbers = range (1,31)
# squares = map(lambda nums: nums**2, numbers)

#oR

# square_nums = lambda nums: nums **2
# squares = map(square_num)   #correct this

# print(list(squares))

# squares_list = list(squares)
# last5 = squares_list[-5                         :]
# first5 = squares_list[0:5] #CORRECT THIS

# print(first5 = last5)


#WRITE A FUNCTON TO REVERSE A STRING

# string = "my text"

#YOU NEED TO KNOW WHAT YOU WANT TO WRITE IN THW FUNCTION WHICH IS WRITTEN BELOW
# reversed_str = string[::-1]
# print(reversed_str)


string = "my text"
def reverse_text(string):

    reversed_str = string[::-1]
    print(reversed_str)

reverse_text(string)

# WRITE A PYTHON FUNCTION THAT ACCEPTS A STRING AND CALCULATE THE NUMBER OF UPPER CASE LETTERS AND LOWER CASE LETTER




