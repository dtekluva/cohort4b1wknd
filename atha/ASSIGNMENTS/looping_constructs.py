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

while True: # RUN THIS FOREVER

    current_time = datetime.datetime.now()
    formated_time = current_time.strftime("%I:%M:%S-%p")

    print(formated_time, end=" \r")
    
    time.sleep(1)
