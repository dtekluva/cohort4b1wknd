# #Functions Contd:
# # before calling a function, you must first print the output with an indentation before callign the function



# # string= "my0i0jin"
# # def reversed(string):
# #     string= "my text"
# #     reversed_text = string[::-1]
# #     print(reversed_text)
# # reversed(string) 

# # name = "MY Text"
# # count = name.isupper
# # print(bool(count))


# # word = "Hello Mr Samuel Okon"
# # uppercases = 0
# # lowercases = 0

# # for i in word:
# #     print(i, i.isupper(), i.islower())
# #     if i.islower():
# #         lowercases +=1
# #     elif i.isupper():
# #         uppercases+=1
# # print(uppercases,lowercases)


# # to write it in a function:


# word = "Hello Mr Samuel Okon"


# def case_counter(string):
#     uppercases = 0
#     lowercases = 0

#     for i in word:
#         # print(i, i.isupper(), i.islower())
#         if i.islower():
#             lowercases +=1
#         elif i.isupper():
#             uppercases+=1
#     print(uppercases,lowercases)   # pls note the indentation of your print.

# # case_counter(word)
# case_counter("WHY are you early to class")   #in running this, it'll still be picking from Word coz you defined "for i in word". To change this, define "for i in string" ie "for i in your parameter"


# def case_counter(string):
#     uppercases = 0
#     lowercases = 0

#     for i in string:         #always try to do this "for i in the parameter
#         # print(i, i.isupper(), i.islower())
#         if i.islower():
#             lowercases +=1
#         elif i.isupper():
#             uppercases+=1
#     print(uppercases,lowercases)       # meaning, print the total value of uppercases and lowercases.   
# case_counter(word)
# case_counter("WHY are you early to class")


# #write a function to READ A FILE from a file path

# # from atha's note, using the backslash to open a folder, baskslash has special function. so with we highlight all and change them to a forward slash (coz windows does not care) or we use the r in front of the file path. r means raw = adopt raw file path. a white space after the r nullifies it

# # # file_name = "C:/Users/user/Desktop/CP CLASSES/Python Backend/Code Folder/cohort4b1wknd/materials/statement2.csv"
# # # ORRR 
# # file_name = r"C:\Users\user\Desktop\CP CLASSES\Python Backend\Code Folder\cohort4b1wknd\materials\statement2.csv"
# # # Action =open(file_name, "r")          #positional argument in which the positions index must not change

# # Action=open(file = file_name, mode = "r")    #keyword argument in which the positions index is allowed to be interchange. But usign this, the 2nd file = a a keyword for working with files either read, write, append

# # statement = file.readlines()    #to read line by line
# # # statement = file.read()    #to read character by character
# # print(statement)



# # IN SUMMARY:
# # file_name = r"C:\Users\user\Desktop\CP CLASSES\Python Backend\Code Folder\cohort4b1wknd\materials\statement2.csv"
# # action=open(file = file_name, mode = "r")     # using keyword argument, the keyword "file" must be used.
# # statement = action.readlines()
# # # statement = file.read()
# # print(statement)

# # for i in statement:      #N/B: we introduced the for loop here so the print can run the excel file row by row instead of printing in one long line.
# #     print(i)
# #     # print("\n")


# #ANOTEHER EXAMPLE
# # to print just lodgement column in the file ie index of 4.

# # file_name = r"C:\Users\user\Desktop\CP CLASSES\Python Backend\Code Folder\cohort4b1wknd\materials\statement2.csv"
# # action=open(file = file_name, mode = "r")    
# # statement = action.readlines()
# # print(statement)

# # for i in statement:
# #     # print(i.split(",")[4])
# #     # print(i.split(",")[6].rjust(70))
# #     print(i.split(",")[3])

# #     # print("\n")







# # # To count the number of times 500 occured in withdrawals:
# # file_name = r"C:\Users\user\Desktop\CP CLASSES\Python Backend\Code Folder\cohort4b1wknd\materials\statement2.csv"
# # action=open(file = file_name, mode = "r")    
# # statement = action.readlines()
# # # print(statement)
# # count_500 = 0
# # for i in statement:
# #     splitted_line = i.split(',')
# #     withdrawal = splitted_line[3]
# #     description = splitted_line[6]
# #     if withdrawal == "500.00":
# #         print(withdrawal, ">>>>", description)
# #         count_500+=1
# # print(count_500)





# # To count the number of times 500 occured in withdrawals (and put it in a function): first thing is to highlight and tab everything

# file_name = r"C:\Users\user\Desktop\CP CLASSES\Python Backend\Code Folder\cohort4b1wknd\materials\statement2.csv"

# # def transaction_doc(file_name,target_amount,target_column,description_col):

# #     action=open(file = file_name, mode = "r")    
# #     statement = action.readlines()
# #     # print(statement)
# #     count_500 = 0
# #     for i in statement:
# #         splitted_line = i.split(',')
# #         withdrawal = splitted_line[target_column]   #this is called passing arguments to a function
# #         description = splitted_line[description_col]
# #         if withdrawal == target_amount:
# #             print(withdrawal, ">>>>", description)
# #             count_500+=1
# #     print(count_500)

# # transaction_doc(file_name,"500.00",3,6)

# # def transaction_doc(file_name,target_amount,target_column,description_col):

# action=open(file = file_name, mode = "r")    
# statement = action.readlines()
# for i in statement:
#     splitted_line = i.split(',')
#     print(splitted_line)



# # Pls copy from atha's note how to get sum of total targets of the particular line of transactions


# following the same logic, pls do atha's assignment (read, write and append)
# pls do more rehearsals on functions from w3 resource......that's the only way forward
# read real python link on OOP




# OOP = OBJECT ORIENTED PROGRAMMING

# class creation, class call = instantiation, class attribute, instance attribute, 


































































