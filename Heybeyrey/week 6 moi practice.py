# num = 9                                      #let the loop start from here
# while num < 20:                              #let the loop end here
#     print (f"the count is: {num}")           #output this
#     num = num + 1                            #steps to output
# # With the break statement we can stop the loop even if the loop condition is true:

# animals = ("goat","sheep","dog")
# for x in animals:              # note the diff in the output for line 8&9 Vs line 10
#     print(x)
# print (animals)

# animals = ("goat","sheep","dog")
# for x in animals:
#     if x == "goat":
#         break               #break means stop
        # print(x)


# x = 21 if "ade" is "boy" else 32          # I dont like itenary operators
# print(x)

# import time
# a = ["fizz", "baz", "buzz"]
# while a:    
#         for x in a:
#                 print(x)
#         time.sleep(5)   # if the speed of output is too fast, just import time and use time.sleep(secs) below your print command to moderate

#POP FUNCTION:
# import time
# a = ["fizz", "baz", "buzz"]
# while a:   
#     print(a.pop(-1))       # the pop function is just to remove and print out a function step by step at the identifiable index starting with 0 from the front and -1 from the back. It is also used to interupt the while function  

#   # random examples of the while loop function:  
# number = 0
# while number < 21:  # rem the start, stop and step model. It'll keep numberign till it reaches this condition of 21
#         print (number)
#         number = number + 1

# num= 0
# while num<20:
#         print(num)
#         num += 1


# numm = (5,10,30,40)
# print (sum(numm))

# numm = [5,10,30,40]
# total = 0           # because we wanna increament it that's why we had to define total again
# while numm:
#         singlenumm = numm.pop(0) #this pop is seeing this list as one index item unlike the string of diff indexes
# total =total + singlenumm    #this indentation = 0+5, 0+10, 0+30 and 0+40
# print(total)                    #hence total = 0+40 =40
# print(sum(total))

#HOWEVER:    #see HOW ORDINARY INDENTATION CAN CHANGE THE MEANING OF YOUR CODES
# numm = [5,10,30,40]
# total = 0           
# while numm:
#         singlenumm = numm.pop(0) 
#         total =total + singlenumm    #this indentation = 0+5, 5+10, 15+30 and 45+40
#         print(total)                    #hence total = 5, 15, 45 and 85
# print(total)                          #hence total = 45+40 =85

# import datetime
# import time
# while True:
#         current_time = datetime.datetime.now()
#         print(current_time.year, current_time.month, current_time.day, current_time.second, sep=":", end= "\r")
#         print(current_time.strftime("%Y-%M-%d-%p"))  # this is string rep of time ie the short codes for representing time formats...refer to link in read me
        # time.sleep(3)

#N/B: \r means BACKWARD CARRIAGE ie retain the recurring output ON THE SAME LINE


# BREAK AND CONTINUE FUNCTION:
# ade = 5
# while ade < 20:
#         print ("ade is still a bachelor")
#         ade = ade+1
#         break               # break means stop looping
# else:
#         print("yeap stop")   # also once it breaks, else and everyother thing beneath the while loop STOPS


# other break examples to play with
#let's search for the first number btw 5 and 50 that is divisible by 5 and 3 then break the loop:


# number = 0
# max_number = 50
# while number < max_number:
#     if number !=0 and number%3 == 0 and number%5 ==0:
#         print(f"found our number {number}")
#         continue      # without this break, we found 15, 30 and 45. But after we used this break, after the first number, it stops. and with the break, the else also would not run unless the chain ends by itself
#     number+=1
# else:
#     print("sorry, try again")

# num =  500
# while num < 1000:
#     if num%3!=0 and num %32!=0:
#         print(num)
#         continue
#     num+=1
    
# nested while: 
# minutes = 0
# seconds = 0
# while minutes < 60:
#     while seconds < 60:
#         print(f"{minutes} : {seconds} mins", end= "\r")
#         seconds+=1    # pls note the indentation of the step of the inner nest (seconds)
#     seconds =0       #so we had to rese the seconds again for the minutes to run to 60
#     minutes+=1        # pls note the indentation of the step of the outer nest (minutes)

# Word REPLACEMENT:
word = " I am a boy and a girl"
rep = word.replace("boy", "obi"). replace ("girl", "ada")
print(rep)

 # OR!

word = " I am a boy and a girl and we both go to church"
replacements = [("boy", "obi"),
                ("girl","ada"),
                ("church","mosque")
                ]

while replacements:
        replaced_action = replacements.pop(0)          #we popped them first
        # print(replaced)
        word = word.replace(replaced_action[0],replaced_action[1])  # then used the replace function
        print(word)    # this indentation duplicates the output by the number of while loop next line per next word
print(word)                                #pls take not of the indentation of the print and the various impacts




















