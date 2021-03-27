# if 'foo' in ['bar', 'baz', 'qux', 'foo']:
#     print('Expression was true')
#     print('Executing statement in suite')
#     print('...')
#     print('Done.')
# print('After conditional')

# action = "A"

# if action == "A":
#     # QUESTION 1

#     principal = float(input("PLease enter principal collected : "))
#     rate      = float(input("PLease enter rate : "))
#     time      = float(input("PLease enter duration : "))

#     interest = (principal * rate *  time) / 100

#     print(interest)

#     total_repayment = principal + interest

#     # print(f"Principal obtained : {principal}")
#     # # print(f"Repayment amount : {total_repayment}")
#     # # print(f"Interest accrued : {interest}")

#     print("Principal obtaned :", principal)
#     print("Repayment amount  :", total_repayment)
#     print("Interest accrued  :", interest)
#     input("Please press enter if you are done.!!")

# if action == "B":
#     # QUESTION 2

#     FRIEND1_SWEETS = int(input("How many sweets from friend 1 : "))
#     FRIEND2_SWEETS = int(input("How many sweets from friend 2 : "))
#     FRIEND3_SWEETS = int(input("How many sweets from friend 3 : "))

#     total_sweets = FRIEND1_SWEETS + FRIEND2_SWEETS + FRIEND3_SWEETS
#     share = total_sweets//3 # GET FLOOR DIVISION VALUE
#     remainder = total_sweets%3 # GET REMAINDER OR MODULUS

#     print(f"HELLO GUYS, EACH OF YOU SHOULD GET {share}SWEETS AND {remainder} SHOULD BE DISCARDED")


# action = input("Please what would you like to do ?\n\nA: (simple interest)\nB: (candy crusher)\n\n> ")

# if action == "A":
#     # QUESTION 1

#     principal = float(input("PLease enter principal collected : "))
#     rate      = float(input("PLease enter rate : "))
#     time      = float(input("PLease enter duration : "))

#     interest = (principal * rate *  time) / 100

#     print(interest)

#     total_repayment = principal + interest

#     print("Principal obtaned :", principal)
#     print("Repayment amount  :", total_repayment)
#     print("Interest accrued  :", interest)
#     input("Please press enter if you are done.!!")

# if action == "B":
#     # QUESTION 2

#     FRIEND1_SWEETS = int(input("How many sweets from friend 1 : "))
#     FRIEND2_SWEETS = int(input("How many sweets from friend 2 : "))
#     FRIEND3_SWEETS = int(input("How many sweets from friend 3 : "))

#     total_sweets = FRIEND1_SWEETS + FRIEND2_SWEETS + FRIEND3_SWEETS
#     share = total_sweets//3 # GET FLOOR DIVISION VALUE
#     remainder = total_sweets%3 # GET REMAINDER OR MODULUS

#     print(f"HELLO GUYS, EACH OF YOU SHOULD GET {share}SWEETS AND {remainder} SHOULD BE DISCARDED")

# # if not action == "A" or not action == "B":
# #     print("INVALLID SELECTION.")

# if action != "A" or action != "B":
#     print("INVALLID SELECTION.")

# a = int(input("PLease enter a value for A : "))
# b = int(input("PLease enter a value for B : "))

# if a > b:
#     print(f"{a} is larger than {b}.")
# else:    
#     print(f"{b} is larger than {a}.")

# # test for words that startwith a and end with t
# word = input("PLease enter your name : ")

# if word.startswith("a") and word.endswith("t"):
#     print(f"Weldone {word} starts with 'a' and ends with 't'")
# else:
#     print("Sorry please try again.")

# test for words that startwith a and end with t
# word = input("PLease enter your name : ").lower()

# if len(word) <= 6: # check that name is not too long
#     if word.startswith("a") and word.endswith("t"):
#         print(f"Weldone {word} starts with 'a' and ends with 't'")
#     else:
#         print("Sorry please try again.")
# else:
#     print("Sorry your name might be too long.!!")


# program to check if seconds hand is in the first or second half of the clock
import datetime

current_datetime = datetime.datetime.now()
print(current_datetime)

seconds = current_datetime.second
print(seconds)

if seconds < 30:
    print(f"You are in the first half of the minute. {seconds}seconds.")
else:
    print(f"You are in the second half of the minute. {seconds}seconds.")