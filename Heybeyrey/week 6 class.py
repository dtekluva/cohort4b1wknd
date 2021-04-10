# Tenary Operator is a one line conditional assignment operator
# x = 21 if "ade" is "boy" else 32
# print(x)

# Looping Constructs
# for loop = definite loops
# while loop = indefinite loops

a = ["fizz", "baz", "buzz"]
# while a:                     # pls note the colon and indentation same as an if function
    # print(a.pop(-1))      #-1 starts popping from the back while +1 starts popping from the front
    # print(a.pop(1))        # there is no limit to the number of statement and expressions


# print a while loop that can print 1 - 20

# num= 0
# while num<20:
#     num += 1
    # print(num)

# nums= [5,10,30,40]
# total = 0
# while nums:
#     single_num= nums.pop(0)
#     # print(sum1.pop(0)) 
#     total += single_num
# print(total)
# # print(sum(nums))

# import datetime
# import time
# while True:  #run this forever
#     current_time = datetime.datetime.now()
    # print(current_time)
    # print(datetime.datetime.now())    #this while loop continues to infinity. To stop the continous, at the terminal type control+C ie the keyboard interupt
# from time import sleep  #OR
    # time.sleep(3)
    # print (current_time.hour, current_time.minute, current_time.second, sep = ":")

    #OR WE DO:
#after importing datetime and time and stating while true
    # formatted_time = current_time.strftime("%I:%M:%S-%p")  #strftime means string representation of time. Pls check the link for the shortcut of the months, years, seconds, etc
    # print (formatted_time)
    # print (formatted_time, end="\r")       #\r means carriage return ie take the cursur back to the beginning

# break and continue function
ade = 5 
is_ade_married = False

# while ade < 20:
#     print("ade is still a bachelor")
#     ade +=1

#     is_ade_married = input("his age?")
#     if is_ade_married: 
#         print ("ade is now married")
#         break
#     else:
#         print("ade never married")
    
#let's searche with the first number btw 5 and 50 that is divisible by 5 and 3

# number = 0
# max_number = 50
# while number < max_number:
#     if number !=0 and number%3 == 0 and number%5 ==0:
#         print(f"found our number {number}")
#         break      # without this break, we found 15, 30 and 45. But after we used this break, after the first number, it stops. and with the break, the else also would not run unless the chain ends by itself
#     number+=1
# else:
#     print("sorry, try again")


# number = 0
# max_number = 50
# while number < max_number:
#     if number !=0 and number%3 == 0 and number%5 ==0:
#         print(f"found our number {number}")
#         continue      # using continue just keeps repeating itsels ie after the break
#     number+=1
# else:
#     print("sorry, try again")


# number = 500
# max_number = 1000
# while number < max_number:
#     if number !=0 and number%3 == 0 and number%32 ==0:
#         print(f"found our number {number}")
#         break      # so if you wanna see all the numbers, just take out the break
#     number+=1
# else:
#     print("sorry, try again")

# number = 500
# max_number = 1000
# while number < max_number:
#     if number !=0 and number%3 == 0 and number%32 ==0:
#         print(f"found our number {number}")
#     number+=1
# else:
#     print("sorry, try again")     # note the else also shows if nothing breaks it

# nested while
# import time
# minutes = 0
# while minutes < 60:
#     print(f"{minutes} mins")
#     minutes +=1
#     time.sleep(1)      # we used this time.sleep to set the pace coz it was fast

# import time     # note we imported time here
# minutes = 0
# seconds = 0
# while minutes < 60:
#     while seconds < 60:
#         print(f"{minutes} mins : {seconds} secs")
#         seconds +=1
#         time.sleep(1)   
# minutes +=1    #minutes is no more counting after 60 seconds, so therefore


# import time     
# minutes = 0
# seconds = 0
# while minutes < 60:
#     while seconds < 5:
#         print(f"{minutes} mins : {seconds} secs")
#         seconds +=1
#         time.sleep(1) 
#     seconds = 0
#     minutes +=1     #then with this, while loop continues to infinity



# reversing the  time to count from 2 mins to 0 minutes
import time     
minutes = 2
seconds = 0
while minutes > -1:
    while seconds > 0:
        print(f"{minutes} mins : {seconds} secs")
        seconds -=1
        time.sleep(1) 
    seconds = 60        #this is to set back the timer from where it should start from
    minutes -=1 
    
    