# first_3_letters = 'ABC'
# print(first_3_letters)
# print(type(first_3_letters))

# fruit = "apple"
# fruit = 'apple'


# print(fruit)
# print(type(fruit))

# sentence = 'she said "that is a great tasting apple"'
# sentence = "she said that is a great tasting apple"
# sentence = "she said 'that is a great tasting apple'"
# print(sentence)
# print(type(sentence))


# principal = float(input("Please enter principal collected : "))
# rate      = float(input("Please enter rate : "))
# time      = float(input("Please enter duration : "))

# interest = (principal * rate * time) / 100

# print(interest)

# total_repayment = principal + interest

# print(f"Principal obtained : {principal}")
# print(f"Repayment amount   : {total_repayment}")
# print(f"Interest accrued   : {interest}")

# print(f"Principal obtained :", principal)
# print(f"Repayment amount   :", total_repayment)
# print(f"Interest accrued   :", interest)
# input()
# input("please press enter if you are done. !!")

# Question 2

FRIEND1_SWEETS = int(input("How many sweets from friend 1 : "))
FRIEND2_SWEETS = int(input("How many sweets from friend 2 : "))
FRIEND5_SWEETS = int(input("How many sweets from friend 3 : "))

total_sweets = FRIEND1_SWEETS + FRIEND2_SWEETS + FRIEND5_SWEETS 
share = total_sweets//3 # GET FLOOR DIVISION VALUE
remainder = total_sweets%3 # GET REMAINDER OR MODULUS

print(f"HELLO GUYS, EACH OF YOU SHOULD GET {share} SWEETS AND {remainder} SHOULD BE DISCARDED")

