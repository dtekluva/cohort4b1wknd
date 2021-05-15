# x = 0
# y =  5

# if x < y :
#     print("yes")

# if x > y :
#     print("yes")



# if 'foo' in ['bar', 'baz', 'quix', 'foo']  
#     print ('Expression was true')

# # WRITE A PROGRAME THAT WILL GIVE A SOLUTION TO THE 2 ASSIGNMENTS DONE TODAY

# action = input (" Please what would you like to do ? \n\nA: (simple interest)\nB: (candy crusher)\n\n> ")

# if action == "A":
#     principal = float(input ("Please enter principal collected : "))
#     rate = float(input ("Please enter rate : "))
#     time = float(input ("Please enter duration : "))

#     interest = (principal * rate * time) / 100 *12


#     print(interest)

#     total_repayment = principal + interest


#     print("Principal obtained :", principal)
#     print("Repayment amount : ", total_repayment)
#     print("Interest_accrued :", interest)
#     input()




# if action == "B":
#     FRIEND1_SWEETS = int(input("How many sweets from friend 1: "))
#     FRIEND2_SWEETS = int(input("How many sweets from friend 2: "))
#     FRIEND3_SWEETS = int(input("How many sweets from friend 3: "))

#     total_sweets = FRIEND1_SWEETS + FRIEND2_SWEETS + FRIEND3_SWEETS 
#     share = total_sweets // 3
#     remainder = total_sweets%3

#     print(f"HELLO GUYS, EACH OF YOU SHOULD GET {share} SWEETS AND {remainder} SHOULD BE DISCARDED")



# if not action == "A" or not action == "B":
#     print("INVALID SELECTION.")
     
# if action != "A" or action != "B":
#     print("INVALID SELECTION,")

# if "foo" in [ 'foo', 'bar', 'baz']:
#     print( "outer conditiion is true")


# a = input ("Please enter a value for A")
# b = input ("Please enter a value for B")

# if a > b:
#     print(f"{a} is greater than {b}.")
# else:
#     print(f"{b} is greater than {a}.")

# TEST FOR A WORD THAT STARTS WITH A AND ENDS WITH T:
    

# word = input ("Please enter your name")
# if word.startswith("a") and word.endswith("t"):
#     print(f"Weldone {word} starts with 'a' and ends with 't'")
# else:
#     print("Sorry please try again.")

# TEST FOR A WORD THAT STARTS WITH A AND ENDS WITH T IF THE LENGTH DOES NOT EXCEED 6 CHARACTERS

# word = input ("Please enter your name")


# if len(word) <=6:
#     if word.startswith("a") and word.endswith("t"):
#         print(f"Weldone {word} starts with 'a' and ends with 't'")
#     else:
#         print("Sorry please try again.")
# else:
#     print("Sorry your name might be too long")



# import datetime
# current_datetime = datetime.datetime.now()
# print(current_datetime)

# seconds = current_datetime.second
# print(seconds)

# if seconds < 30:
#     print(f"You are in the first half of the minute. {seconds}seconds.")
# else:
#     print(f"You are in the second half of the minute. {seconds}seconds.")

 

word = input ("Please enter your name")
reversed_word = "".join(reversed(word)) 


# print(reversed_word)

if reversed_word == word:
    print(f"Weldone. {word} is a palindrome")
else:
    print(f"Sorry please try again")

