# principal = float(input ("pls insert principal amount : "))
# rate = float(input ("pls insert rate : "))
# time = float(input ("pls insert time amount : "))
# interest = (principal*rate*time)/100           
# print(interest)
# total_repayment = principal + interest

# print(f"principal obtained : (principal)")           #f here means format all the variables into a single string...additional string using curly braces. Try this print(f"principal obtained : (principal){ade}{moi}")
# print(f"total_repayment : (total_repayment)")
# print(f"interest accrued : (interest accrued)")       since we have already divided by 100, we use 0.05 as rate
# input("pls press enter when done")       with this opened, you can go to the file extenstion .ext file on your system folder and call it up to fun and save.

# print("principal obtained : ", principal)
# print("repayment amount : ", total_repayment)
# print("interest accrued : ", interest)
ade=32
olu=56
moi=87
myname=f"{ade} {olu} {moi}"
print(myname)

# # Question2
# friend1= int(input("how many sweet for friend 1 : "))
# friend2= int(input("how many sweet for friend 2 : "))
# friend3= int(input("how many sweet for friend 3 : "))     #run this here to input the number of sweet for each person
# total_sweet=friend1 + friend2 + friend3
# share= total_sweet/3
# remainder= total_sweet%3
# print(f"hello all, each of you should get (share) sweets and the remainder (remainder) should be discarded") 
# print(f"hello all, each of you should get {share} sweets and the remainder {remainder} should be discarded")
# print("hello all, each of you should get", share, "sweets and the remainder", remainder, "should be discarded")
# note how to adopt with f or without the f

#CONDITIONAL STATEMENTS
#pls check the URL Link for conditional statements under README
x=0
y=5
# if x < y:         #pls note the colon after the if command and the indentation before the print
#     print("yes")
#     print('all is well')
#     print('this is the class')
# print('admin block')
if x>y:
    # print("yes")     # runing this would give an empty result coz it is false and we have not give additional commands for the false. If yes has been defined earlier, we do print(yes), if not we do print("yes"). This is why we insert a quotation mark before and after the yes.
#check the URL...still the same URL
    print("yes")
    print('all is well')
    print('this is the class')
else:             #else is for one alternative; elif is for more that one alternative.
    print("no")
print('admin block')                   #python witll respond to all print command in the block before moving the next off-side function. Remember the off-side rule in the URL

#next example: The if function can be longer.
# action = input("pls what would you like to do? \nA:(simple interest) \nB:(candy question)\n>")
# if action == "A":
# #question1
#     principal = float(input ("pls insert principal amount : "))    #to group indent, highlight and press tab
#     rate = float(input ("pls insert rate : "))
#     time = float(input ("pls insert time amount : "))
#     interest = (principal*rate*time)/100           
#     print(interest)
#     total_repayment = principal + interest

#     print("principal obtained : ", principal)
#     print("repayment amount : ", total_repayment)
#     print("interest accrued : ", interest)

# if action =="B":
#     # # Question2
#     friend1= int(input("how many sweet for friend 1 : "))
#     friend2= int(input("how many sweet for friend 2 : "))
#     friend3= int(input("how many sweet for friend 3 : "))     
#     total_sweet=friend1 + friend2 + friend3
#     share= total_sweet/3
#     remainder= total_sweet%3
#     print(f"hello all, each of you should get {share} sweets and the remainder {remainder} should be discarded")
#     print("hello all, each of you should get", share, "sweets and the remainder", remainder, "should be discarded")

# if not action =="A" or not action =="B":
#     print("INVALID SELECTION")

# if action !="A" or action !="B":
#     print("INVALID SELECTION")

# still on the URL, check for the nested if functions ie identing another if function inside another if function

# x=int(input("what value is x : "))
# y=int(input("what value is y : "))
# sum=x+y
# print(f"{x} {y}")
# print(sum)

# if x > y:
#     print(x, "is larger than", y)       #recall you can use this or the f format
# else:
#     print(y, "is larger")


#test of words that start with a and end with t
# word = input("pls enter the word : ").lower()         #note how to use .lower() and .upper()
# # if word.startswith("a") and word.endswith("t"):
# #     print(f"{word} starts with 'a' and ends with 't'")
# # else:
# #     print("pls try again")


# #another nested example
# if len(word)<=6:
#     if word.startswith("a") and word.endswith("t"):
#         print(f"{word} starts with 'a' and ends with 't'")
#     else:
#         print("pls try again")
# else:
#     print("your name is longer that 6")

# DATETIME FUNCTION
import datetime
current_datetime = datetime.datetime.now()  #note, datetime is a fuction inside datetime.
print(current_datetime)
seconds= current_datetime.second
print(seconds)




