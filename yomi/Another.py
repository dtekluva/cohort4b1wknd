# file_path = r"/Users/Yomi/Documents/cohort4b1wknd/materials/statement2.csv"
# file = open(file = file_path, mode = "r")

# statement = file.readlines()
# print(statement)

# for line in statement:
#     print(line)
#     print("n\n")

withdrawals500 = 0

file_path = r"/Users/Yomi/Documents/cohort4b1wknd/materials/statement2.csv"

statement_file = open(file_path, "r")# calling open builtin function using positional argument

for line in statement_file:

        splitted_line = line.split(",")
        withdrawals = splitted_line[3]
        description = splitted_line[6]
        # print(line.split(",")[])
        # print("\n\n")
        # print(withdrawals, description, sep = "            ")

        if withdrawals == "500.00":
            withdrawals500 +=1

            multiple_of_total = withdrawals500 * (500)

print(withdrawals500)
print(multiple_of_total)

srty = "check me out"
