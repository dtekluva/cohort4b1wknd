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
number = 0
max_number = 50

while number < max_number:
    
    if number != 0 and number % 3 == 0 and number % 5 == 0:
        print(f"Found, our number is {number}")
        break
    
    number += 1
    
else:
    print("Sorry number matches your description.")