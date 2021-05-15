

# x=[1,2,3,4,5]
# while x:
#     print(x.pop(-1))


# a= ['fizz', 'baz', 'buzz']
# while a:
#     print(a.pop(-1))


# x=21
# while x > 0:
#     x -= 1
#     print(x)

# x=0
# while x < 20:
#     x += 1
#     print(x)

# WRITE A PROGRAM  USING 'WHILE' AND 'POP' THAT WILL SHOW THE SUM OF THE LIST
# nums =[5,10,30,40]
# total = 0

# while nums:

#     sinle_num = nums.pop()
#     total += sinle_num

# print(total)


# CREATE A WHILE LOOP THAT PRINTS THE TIME ACCURATE TO THE SECOND AND MAKE IT UPDATE TIME WHILE ON THE SAME LINE
# import datetime
# import time
# THIS PRINTING TOO FAST WE NEED TO SLOW IT DOWN SO LETS USE SLEEP
# from datetime import datetime
# from time import sleep

# while True: #RUN THIS FOREVER
#     print(datetime.datetime.now()) 
#     time.sleep(1)
# THIS IS GIVING US MORE INFORMATION THAN WE NEED 

# import datetime
# import time
# while True: #RUN THIS FOREVER
#     current_time = datetime.datetime.now()
    
#     print(current_time.hour, current_time.minute, current_time.second, sep =":") 
#     time.sleep(10)

# STRING REFERENCE OF TIME- CONVER TO HUMAN READEABLE TIME IN XXX FORMAT-strftime
# STRING REPRESENTATION OF TIME =CONVERT TIME TO MACHINE FORMAT -strptime


# import datetime
# import time
# while True: #RUN THIS FOREVER

#     current_time = datetime.datetime.now()
#     formatted_time = current_time.strftime("%I:%M.%S-%p")

#     print(formatted_time, end= "\r")
#     # IN THIS CASE \r MEANS CARRIAGE RETURM- TAKE THE CURSOR BACK TO THE BEGINNING
#     time.sleep(1)

# n = 5
# while n > 0:
#     n-=1
#     if n == 2:
#         continue
#     print(n)


# n = 5
# while n > 0:
#     n-=1
#     if n == 2:
#         break
#     print(n)

# print('Loop ends')

# BREAK CONTINUE AND ELSE

# ade = 5
# is_ade_married_now = False
# while ade < 20:
#     print ("Still a bachelor")
#     ade +=1
# else: 
#     print ("Ade never married")

# ade = 5
# is_ade_married_now = False
# while ade < 20:
#     print ("Still a bachelor" ,ade)
#     ade +=1

#     is_ade_married_now = input("is ade married now? : ")

#     if is_ade_married_now:
#         print ("Ade is now married.")
#         break

# else: 
#     print ("Ade never married")


# LET'S SEARCH FOR THE FIRST NUMBER BETWEEN 0 AND 50 THAT IS DIVISIBLE BY 5 AND 3

# number = 0
# max_number = 50

# while number < max_number:
    # if number % 3 == 0 and number % 5 == 0: 
        # THIS GAVE US 0 IN THE RESULT. WE NEED TO TAKE IT OUT
#         print(f"Found, our number is {number}")
    
#     number += 1

# else:
#     print("Sorry, no number matches your description.")



# number = 0
# max_number = 50

# while number < max_number:
#     if number !=0 and number % 3 == 0 and number % 5 == 0: 
#         # THIS DOES NOT INCLUDE 0 IN OUR RESULT
#         print(f"Found, our number is {number}")
    
#     number += 1

# else:
#     print("Sorry, no number matches your description.")


# number = 0
# max_number = 50

# while number < max_number:
#     if number !=0 and number % 3 == 0 and number % 5 == 0:
#         print(f"Found, our number is {number}")
#         break

#     number += 1

# else:
#     print("Sorry, no number matches your description.")

# CHECK BETWEEN 500 AND 1000, GET THE FIRST NUMBER THAT IS DIVISIBLE BY 3 AND 32


# number = 500
# max_number = 1000

# while number < max_number:
#     if number !=500 and number % 3 == 0 and number % 32 == 0:
#         print(f"Found, our number is {number}")
        
#         break

#     number += 1

# else:
#     print("Sorry, no number matches your description.")
    

# import time
# minutes = 0

# while minutes < 60:
#     print(f"{minutes}mins")
#     minutes +=1

# import time
# minutes = 0
# seconds = 0
# while minutes < 60:

#     while seconds < 60:

#         print(f"{minutes}mins: {seconds}secs")
#         seconds +=1
#         time.sleep(1)

# #         minutes +=1
# # HOW DO WE MAKE OUR MINUTES COUNTS AND WHAT HAPPENS WHEN THE MINUTES GET TO 60
# import time
# minutes = 0
# seconds = 0
# while minutes < 60:

#     while seconds < 60:

#         count = f"{minutes}mins: {seconds}secs"
#         print(count)
#         seconds +=1
#         time.sleep(1)
    
#     seconds = 0
#     minutes += 1

#     minutes +=1

# import time
# minutes = 4
# seconds = 0
# while minutes > -1:

#     while seconds >0:

#         count = f"{minutes}mins: {seconds}secs"
#         print(count)
#         seconds -=1
#         time.sleep(1)
    
#     seconds = 60
#     minutes -=1
    






# Please find the corrsponding number that when multiplied by 3 gives a sum whos value is the same as 
# the last value of the original number

# i.e

# > 301 + 301 + 301
# >> 111

# > 214 + 214 + 214
# >> 444

# i = 100

# while i < 1000:
#     sum_i = i + i + i
#     # last_char = sum_i[2] THIS GAVE AN ERROR MESSAGE INT IS NOT SUBSCRIPTABLE
#     i_str = str(i)
#     last_char = i_str[2] 
#     last_char_multiple = last_char * 3


#     if sum_i == int(last_char_multiple):
#         print(i, sum_i, last_char, last_char_multiple)
#         break
#     i+=1

        

    
