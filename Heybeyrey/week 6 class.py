# Tenary Operator is a one line conditional assignment operator
# x = 21 if "ade" is "boy" else 32
# print(x)

# Looping Constructs
# for loop = definite loops
# while loop = indefinite loops as long as the condition remains true

a = ["fizz", "baz", "buzz"]
# while a:                     # pls note the colon and indentation same as an if function
    # print(a.pop(-1))      #-1 starts popping from the back while 0 starts popping from the front
    # print(a.pop(1))        # there is no limit to the number of statement and expressions


# print a while loop that can print 1 - 20

# num= 0
# while num<20:
#     num += 1
    # print(num)

#OR 
number = 0
while number < 21:  # rem the start, stop and step model. It'll keep numberign till it reaches this condition of 21
        print (number)
        number = number + 1    #so either you do num = num + 1 OR num increamental by 1 ie num +=1.


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
# from time import sleep  #OR once you have imported time above just do time.sleep(secs)
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

number = 0
max_number = 50
while number < max_number:
    if number !=0 and number%3 == 0 and number%5 ==0:
        print(f"found our number {number}")
        break      # without this break, we found 15, 30 and 45. But after we used this break, after the first number, it stops. and with the break, the else also would not run unless the chain ends by itself. If we replace the break with continue, then the result of the break continues repeating itself. and also, else function will not print since the continue function runs till infinity. Pls also note that the indentation of the print, break and continue are the same while that of number +=1 is one tab behind.
    number+=1
else:
    print("sorry, try again")


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


# num =  500
# while num < 1000:
#     if num%3!=0 and num %32!=0:
#         print(num)
#         continue
#     num+=1
    
# nested while: 
minutes = 0
seconds = 0
while minutes < 60:
    while seconds < 60:
        print(f"{minutes} : {seconds} mins", end= "\r")
        seconds+=1
    seconds =0
    minutes+=1








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
# minutes = 0           #recall, this is the start
# seconds = 0           #recall, this is the stop
# while minutes < 60:
#     while seconds < 5:
#         print(f"{minutes} mins : {seconds} secs")
#         seconds +=1
#         time.sleep(1) 
#     seconds = 0         #so we will reset the seconds
#     minutes +=1         #recall, this is the step



# reversing the  time to count from 2 mins to 0 minutes
# import time     
# minutes = 2
# seconds = 0
# while minutes > -1:
#     while seconds > 0:
#         print(f"{minutes} mins : {seconds} secs")
#         seconds -=1
#         time.sleep(1) 
#     seconds = 60        #this is to set back the timer from where it should start from
#     minutes -=1 
    

    
#to replace multiple words if we dont wanna use the . replace . replace . replace
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