# message = "Allow me to enlighten you,\n\tThis is a new era\n\tThings are peachy" # backslashes enable for special character behaviours i.e \n moves text to the next line.
# # print(message, end="THIS IS THE END")
# print(message, end="\nTHIS IS THE END")

#### (END) PARAMETER FOR PRINT

# prefered_end = "\n"
# prefered_end = "\n\n\n\n\n"
# prefered_end = "\t\t\t\t\t"

# print(1, end = prefered_end)
# print(2, end = prefered_end)
# print(3, end = prefered_end)
# print(4, end = prefered_end)


#### (SEP) PARAMETER FOR PRINT

# sep = ""

# print("Kunle", "Ada", "Shola", sep = ",", end = "")
# print("Kunle", "Ada", "Shola", sep = "-")
# print("Kunle", "Ada", "Shola", sep = " and ")

#### (FILE) PARAMETER FOR PRINT

# message1 = "This is a message to the people of my lovely country."
# message2 = "Be strong and fight against injustice."

# file = open("atha/message.txt", "w") # w- write r- read a-append  note that file to be written be print must be opened in write mode.
# print(message1, message2, sep="\nPARAGRAPH ENDS \n\n", file=file)

# CREATE SIMPLE CSV FILE AND WRITE TO
# csv_file = open("atha/message.csv", "w") # w- write r- read a-append  note that file to be written be print must be opened in write mode.

# print(1,2,3,4,5,68,1, sep="", file = csv_file )
# print(2,3,4,5,6,7,8,9, sep="", file = csv_file )

# print("1,2,3,4,5,68,1", file = csv_file)

# import datetime

# print(datetime.datetime.now())

# log_file = open("atha/logs.csv", "a")

# print(datetime.datetime.now(), "enter was pressed", sep=",", file=log_file)