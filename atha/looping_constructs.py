# nums = [5, 10, 30, 40]
# total = 0

# while nums:

#     sinle_num = nums.pop()
#     total += sinle_num

# print(total)
# # print(sum(nums))

import datetime
import time
# import time

# while True: # RUN THIS FOREVER

#     current_time = datetime.datetime.now()
#     print(current_time)

#     time.sleep(1)

# while True: # RUN THIS FOREVER

#     current_time = datetime.datetime.now()
#     print(current_time.hour, current_time.minute, current_time.second, sep = ":")
    
#     time.sleep(1)

# while True: # RUN THIS FOREVER

#     current_time = datetime.datetime.now()
#     print(current_time.hour, current_time.minute, current_time.second, sep = ":")
    
#     time.sleep(1)

# while True: # RUN THIS FOREVER

#     current_time = datetime.datetime.now()
#     formated_time = current_time.strftime("%I:%M:%S-%p")

#     print(formated_time, end=" \r")
    
#     time.sleep(1)


# Break continue and else

# ade = 5
# is_ade_married_now = False

# while ade < 20:

#     print("Still a bachelor")
#     ade += 1

#     is_ade_married_now = input("is ade married now? : ")

#     if is_ade_married_now == "True":
#         print("Ade is now married.")
#         break

# else:
#     print("Ade never married")

# FIND NUMBER WITHIN A RANGE THAT IS DIVISIBLE BY TWO OTHER NUMBERS
# number = 0
# max_number = 50

# while number < max_number:
    
#     if number != 0 and number % 3 == 0 and number % 5 == 0:
#         print(f"Found, our number is {number}")
#         break
    
#     number += 1
    
# else:
#     print("Sorry number matches your description.")

# COUNT UP IN 1SEC INTERVALS

# import time

# minutes = 0

# while minutes < 60:

#     print(f"{minutes}mins")
#     minutes += 1
#     time.sleep(1)

import time

# NESTED WHILE LOOP

# minutes = 0
# seconds = 0

# while minutes < 60:
    
#     while seconds < 5:
        
#         count = f"{minutes}mins:{seconds}secs"
#         print(count)
#         seconds +=1
#         time.sleep(1)
    
#     seconds = 0
#     minutes += 1

# NESTED WHILE LOOP COUNT DOWNWARD

# minutes = 2
# seconds = 0

# while minutes > -1:
    
#     while seconds > 0:
        
#         count = f"{minutes}mins:{seconds}secs"
#         print(count)
#         seconds -=1
#         time.sleep(1)
    
#     seconds = 60
#     minutes -= 1

# a = ['foo', 'bar', 'baz', 'qux', 'corge']
# while a:

#     condition = len(a) < 3

#     if condition:
#         break
#     print(a.pop())

# print('Done.')

# a = ['foo', 'bar', 'baz', 'qux', 'corge']
# while a:
#     print("while top")
#     if len(a) < 3:
#         continue
#     print(a.pop())
# print('Done.')

# def travel_back_in_time():
#     pass

text = "ali was a boy but he went to the room last time to spend alone time"

replacements = [("ali", "Simbiat"),
                ("he", "she"),
                ("boy", "girl"),
                ("room", "church"),
                ("alone", "together")
                ]

while replacements:
    replacement = replacements.pop()
    text = text.replace(replacement[0], replacement[1])

print(text)