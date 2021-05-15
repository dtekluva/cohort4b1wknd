
# x=50

# def ordinary(): #a function has been created but won't run until it is called. This function can have parameters added
#     x = 30
#     print(x)


# ordinary() #here, the function created above has been called
# print(x)



# def ordinary(y): #a function has been created but won't run until it is called. This function can have parameters added-This is called FUNCTION
#     x = 30
#     print(x,y)


# ordinary("y") #here, the function created above has been called- This is called ARGUMENT
# print(x)


# def ordinary(y): #a function has been created but won't run until it is called. This function can have parameters added
#     x = 30
#     print(x * y)


# ordinary(10) #here, the function created above has been called
# print(x)


# def ordinary(y): 
#     x = 30
#     print(x * y)


# y=2
# ordinary(y+3) 
# print(x)

#Create a function that takes 2 arguments (x & y) which must be lists, check if they have anything in common,if yes, print TRUE

# x = ["ada","ojo","bimbo","cletus"]
# y = ["ben","angel", "bimbo", "dan","paul"]

# set_x = set(x)
# set_y = set(y)

# def intersect():


#     intersect = set_x.intersection(set_y)
# #     intersect()

# print("X and Y have at least 1 common values: ",bool(intersect))


# #CORRECTION

# def check_intersect(list_x, list_y):
#     intersect = set_x.intersection(set_y)
#     print(intersect)
#     print("X and Y have at least 1 common values: ",bool(intersect))

# # check_intersect(x,y)

# #IDEALLY
# check_intersect(["ada","ojo","bimbo","cletus"],["ben","angel", "bimbo", "dan","paul"])


#WRITE A FUNCTON TO REVERSE A STRING

# string = "my text"

#YOU NEED TO KNOW WHAT YOU WANT TO WRITE IN THW FUNCTION WHICH IS WRITTEN BELOW
# reversed_str = string[::-1]
# print(reversed_str)


# string = "my text"
# def reverse_text(string):

#     reversed_str = string[::-1]
#     print(reversed_str)

# reverse_text(string)

# WRITE A PYTHON FUNCTION THAT ACCEPTS A STRING AND CALCULATE THE NUMBER OF UPPER CASE LETTERS AND LOWER CASE LETTER


# tHE Boy iS GooD


    # word = "tHE Boy iS GooD"
    # for char in word: #WE FOLLOWED THESE STEPS WHEN WE WERE TRYING TO UNDERSTAND WHAT NEEDS TO BE DONE.
        # print(char)
        # print(char.isupper())
        # print(char.islower()
        # print(char,char.isupper(), char.islower())

#NOW WE KNOW WHAT TO DO, LETS DEFINE THE FUNCTION 

# def case_counter(string):

#     lowercase = 0
#     upcase = 0

#     for char in string:
#         print(char)
#         print(char,char.isupper(), char.islower())

#         if char.islower():
#             lowercase += 1
#             pass
#         elif char.isupper():
#             upcase +=1

#     print(upcase, lowercase)

# case_counter("How Are you Bolade.")

# Q-LETS OPEN A CSV FILE 
#     
# TO NEGATE ANY / OR \ JUST ADD r IN FRONT

##TO GET THE FILE PATH,YOU RIGHT CLICK ON THE FILE  IF IN VS CODE OTHERWISE,GET THE FILE PATH AND SLASH THE FILE NAME.TYPE OF DOC EG .csv, .xls,.docx  REMEMBER TO ADD TH
# file_path = r"C:\Users\hp\Desktop\MY CODES\cohort4b1wknd\materials\statement2.csv"

# statement_file = open(file=file_path, mode = "r") ##calling open built in function using keyword argument
# ##statement_file = open(file_path,"r")##

# ## statement = file.readlines() . 'readlines' reads the lines but if you use 'read', it reads each character 

# statement = statement_file.readlines()

# print(statement)

# for line in statement:
#     print(line)
#     print("\n\n")

###WE WANT TO GET ONLY THE LODGEMENTS FROM THE FILE WHICH IS A STATEMENT OF ACCOUNTS
###LETS SPLIT IT
# for line in statement:
#     print(line.split(",")[4])
#     print("\n\n")


# for line in statement:

#     splitted_line = line.split(",")
#     lodgement = splitted_line[4]
#     description = splitted_line [6]
    
#     print(lodgement,description, sep= "      ")


###LETS PRINT THE WITHDRAWALS AND DESCRIPTION

# for line in statement:

#     splitted_line = line.split(",")
#     withdrawal = splitted_line[3]
#     description = splitted_line [6]
    
#     print(withdrawal,description, sep= "      ")

###LETS PRINT THE WITHDRAWALS THAT ARE 500AND DESCRIPTION

# count_500 = 0

# for line in statement:

#     splitted_line = line.split(",")
#     withdrawal = splitted_line[3]
#     description = splitted_line [6]


#     if withdrawal =="500.00":
#         print(description)
#         count_500 +=1

###LETS CREATE THIS AS A FUNCTION


# file_path = r"C:\Users\hp\Desktop\MY CODES\cohort4b1wknd\materials\statement2.csv"

# def get_count_of_transaction(file_path, target_amount, target_column, description_col):



#     statement_file = open(file_path, "r") 
#     count_500 = 0
#     for line in statement_file:

#         splitted_line = line.split(",")
#         withdrawal = splitted_line[target_column]
#         description = splitted_line [description_col]


#         if withdrawal ==target_amount:
#             print(description)
#             count_500 +=1

#         print(f"Total {target_amount}: ", count_500)

# get_count_of_transaction(file_path, "500.00", 3, 6)

##CONVERT TO A FUNCTION AND GET THE SUM OF A TARGET TRANSACTION VALUE


# file_path = r"C:\Users\hp\Desktop\MY CODES\cohort4b1wknd\materials\statement2.csv"

# def get_count_of_transaction(file_path, target_amount_min, target_amount_max, target_column, description_col):



#     statement_file = open(file_path, "r").readlines()
#     statement_file.pop(0) 
#     count_500 = 0

#     for line in statement_file:

#         splitted_line = line.split(",")
#         withdrawal = splitted_line[target_column]
#         float_withdrawal = float(withdrawal) ##CONVERT TO FLOAT 

#         description = splitted_line [description_col]


#         if float_withdrawal <=target_amount_max and float_withdrawal >= target_amount_min:
#             print(float_withdrawal, description, sep ="         ")
#             count_500 +=1

#     print(f"Total target: ", count_500)

# get_count_of_transaction(file_path, 500, 7000,3, 6)

#### Q SUM UP THE 

         

# file_path = r"C:\Users\hp\Desktop\MY CODES\cohort4b1wknd\materials\statement2.csv"

# def get_count_of_transaction(file_path, target_amount_min, target_amount_max, target_column, description_col):



#     statement_file = open(file_path, "r").readlines()
#     statement_file.pop(0) 
#     count_500 = 0
#     sum_of_target = 0

#     for line in statement_file:

#         splitted_line = line.split(",")
#         withdrawal = splitted_line[target_column]
#         float_withdrawal = float(withdrawal) ##CONVERT TO FLOAT 

#         description = splitted_line [description_col]


#         if float_withdrawal <=target_amount_max and float_withdrawal >= target_amount_min:
#             print(float_withdrawal, description, sep ="         ")
#             count_500 +=1
#             sum_of_target += float_withdrawal

#     print(f"Total target: ", count_500)
#     print(f"Sum of target : ", sum_of_target)

# get_count_of_transaction(file_path, 500, 7000,3, 6)   

####RETURN-how do we transfer the result ofthis function into another file ??
### MAKE CREATED FUNCTION RETURN THE ROWS FOUND THAT MATCH THE COUNDRIES SET SO THAT WE CAN WRITE THEM INTO ANOTHER FILE


# file_path = r"C:\Users\hp\Desktop\MY CODES\cohort4b1wknd\materials\statement2.csv"

# def get_count_of_transaction(file_path, target_amount_min, target_amount_max, target_column, description_col):



#     statement_file = open(file_path, "r").readlines()
#     statement_file.pop(0) 
#     count_500 = 0
#     sum_of_target = 0

#     withdrawal_list =[]


#     for line in statement_file:

#         splitted_line = line.split(",")
#         withdrawal = splitted_line[target_column]
#         float_withdrawal = float(withdrawal) ##CONVERT TO FLOAT 

#         description = splitted_line [description_col]


#         if float_withdrawal <=target_amount_max and float_withdrawal >= target_amount_min:
#             print(float_withdrawal, description, sep ="         ")
#             count_500 +=1
#             sum_of_target += float_withdrawal
#             withdrawal_list.append(line)


#     print(f"Total target: ", count_500)
#     print(f"Sum of target : ", sum_of_target)

#     return withdrawal_list

# filter = get_count_of_transaction(file_path, 1000, 10000,3, 6)
# print(filter)


# def writeback(data,name = "untitled.csv"):

#     file_name = name
#     file = open(f"eju/{name}", "w") 
#     ### YOU MAY DECIDE TO SET ANOTHER PARAMETER AND ADD UNDERNEATH THE PREVIOUS ONE. IN THIS CASE YOU WILL RUN THE FIRST FUNCTION, THEN THE NEW ONE BU IT WILL BE ON 'APPEND' MODE WHICH IS WRITTEN AS 'a'. WE NOTICED THE HEADER REPEATED ITSELF SO WE HAD TO UNDO THE 'POP' .

#     for line in data:

#         file.write(line)

#     file.close()
# writeback(filter, "Myfilter.csv")

