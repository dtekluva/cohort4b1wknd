# #SOLUTION TO EXHAUSTIVE ENUMERATION
# i = 100
# while i < 1000:
#     print(i)
#     i +=1
#     sumi = i + i +i
#     # print(sumi)
#     # print (i, sumi)
#     # last_character = (sumi[2])........#this is not subscriptable means that we cannot separate 5 alone from 185
#     # last_character = str(sumi[2]).......#still not subscriptable or index-able
#     istr= str(i)
#     lastcharacter = istr[2]
#     lastcha_multiple = lastcharacter*3
#     # print(lastcharacter)
#     if sumi == int(lastcha_multiple):
#         print(i, sumi, lastcharacter, lastcha_multiple)
#         break

# # FOR LOOP
# students = ("ade","ola","val")
# for xyz in students:
#     print(xyz)
#     # print(xyz, end= " ,")        #pls note when to print on the same line and when to print on the next line

# # print(iter(students))         #this is to return the iterator object for the vaariable

# teams = ["liverpool","arsenal","acmillan","juventus"]
# team_iterator = iter(teams)
# print(next(team_iterator))       #so we now see the iter function and the next function
# print(next(team_iterator))          #this repetitng is to print the next and next item, or lass lass we use the while loop or a straight for loop ie line 34. 
# print(next(team_iterator))
# print(teams)

# for x in teams:         #note this
#     print(x)

# for x in reversed(teams):          #this is how to reverse a for loop
#     print(x)


# # DICTIONARY COLLECTION
# d = {"foo":1, "bar":2, "baz":3}       #note the diff btw dict and set of string that the 123 were in quotes and it printed all.
# for x in d:
#     # print(x)
#     print(d[x])       #this gives us the values
# for v in d.values():    #this also gives the value
#     print(v)

# for v in d.items():    #this also gives the items ie both the key and the values
#     print(v)
    

# # BUILT IN RANGE FUNCTION : range must be an integer. 
# # x = range(5)
# # print(x)     #this will just print the highlevel range
# # for n in x:
#     # print(n)

# # or we can do this
# # for x in range(5):   #up to but not includeing the end value
#     # print(x)


# # for x in range(0,5,2):   #this is the start, stop and step values
#     # print(x)

# for x in range(20, 2, -3):   #on a decreasing scale, the step would be negative so to take it backward
#     print(x)


# #SOUTION TO EXHAUSTIVE ENUMERATION USING FOR LOOP
# # for i in range (100, 1000):
# #     print(i)
# #     i +=1
# #     sumi = i + i +i
# #     # print(sumi)
# #     # print (i, sumi)
# #     # last_character = (sumi[2])........#this is not subscriptable means that we cannot separate 5 alone from 185
# #     # last_character = str(sumi[2]).......#still not subscriptable or index-able
# #     istr= str(i)
# #     lastcharacter = istr[2]
#     # lastcha_multiple = lastcharacter*3
#     # # print(lastcharacter)
#     # if sumi == int(lastcha_multiple):
#     #     print(i, sumi, lastcharacter, lastcha_multiple)
#     #     break


# # pls check out the w3resource link for practice

# for num in range (1500, 2701):
#     if num%7==0 and num%5==0:
#         print(num)


# for num in range (1500, 2701):
#     if num%7==0 and num%5==0:
#         print(num)
#         break

number_of_items_found = 0     # this is to get the emumeration of the items found
for num in range (1500, 2701):
    if num%7==0 and num%5==0:
        # print(num)
        number_of_items_found += 1
# print(number_of_items_found)

# for x in "x":         #the nonsense I did
#     print("*")
#     for x in "x":
#         print("**")
#         for x in "x":
#             print("****")

#OR
# for i in range (6):
#     print("* " * i)       #so we can actually do multiply a sign into line by line ranges
#     if i == 5:
#         for i in range (6,0, -1):
#             print("* "*i)
 

 #OR if we dont wanna do the nested for loop
# for i in range (6):
#     print("* " * i)      
# for i in range (6,0, -1):
#     print("* "*i)


# for x in range(100,401):
#     if x%2==0:
#         print (x)
        

# for i in range(100,401):
#     i_str = str(i)
#     i1 = int(i_str[0])
#     i2 = int(i_str[1])
#     i3 = int(i_str[2])
#     if i1 %2 == 0 and i2%2==0 and i3%2==0 and i3!=0:
#         print (i1, i2, i3, sep = " ,")

for i in range(100,401):
    i_str = str(i)
    i1 = int(i_str[0])
    i2 = int(i_str[1])
    i3 = int(i_str[2])
    all_conditions = map(lambda x: x%2==0, [i1,i2,i3])   # pls check out this lambda function and what it does
    if all(all_conditions):
        print (i1,i2,i3, sep =",")


# pls check the questions and solutions on w3resource
# check out jupyter notebook
# check out stak edit
# killing the terminal closes jupyter, so you open another terminal
# jumia page inspect (on the web page)
#coinapi.io......play around with this and get their API, next week we see the application
























