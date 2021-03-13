# message = "Allow me to enlighten you,\n\tThis is a new era\n\tThings are peachy" # backslashes enable for special character behaviours i.e \n moves text to the next line.
# # print(message, end="THIS IS THE END")
# print(message, end="\nTHIS IS THE END")


# prefered_end = "\n"
# prefered_end = "\n\n\n\n\n"
prefered_end = "\t\t\t\t\t"

# print(1, end = prefered_end)
# print(2, end = prefered_end)
# print(3, end = prefered_end)
# print(4, end = prefered_end)

# SEP PARAMETER FOR PRINT
sep = ""
# print("Kunle", "Ade", "Shola", sep = ",")
# print("Kunle", "Ade", "Shola", sep = "and")

# (File) Parameter for Print
message1 = "This is a message to the people of my lovely country"
message2 = "Be strong and fight against injustice"
csv_file = open("seye/seye.txt", "w") # w- write r- read a- append note that the file to be written be printed must be opened in the write mode

print(1, 2, 3, 4, 5, 68, 1, sep=",", file = csv_file)
print(2, 3, 4, 5, 6, 7, 8, sep=",", file = csv_file)