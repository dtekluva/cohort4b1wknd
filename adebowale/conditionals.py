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

# if action != 'A' or action != 'B':
#     print('Invalid Input')

# A = int(input('Enter value A:'))
# B = int(input('Enter value B:'))

# if A > B:
#     print(f'{A} is larger than {B}.')

# else:
#     print(f'{B} is larger than {A}.')

# word = input('Enter a word from ur mind:')

# if len(word)<=7:
#     if word.startswith('a') and word.endswith('t') :
#         print(f'You try {word} starts with "a" and ends with "t"')
#     else:
#         print('Mumu name')
# else:
#     print('Your mumu long name')


#program to check if seconds hand is in ist or 2nd half of clock
import datetime

current_datetime = datetime.datetime.now()
print(current_datetime)

seconds = current_datetime.second
print(seconds)