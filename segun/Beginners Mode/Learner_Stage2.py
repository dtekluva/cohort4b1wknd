group = ["debra", 'Ade', "Tony", "Mavelous"]

# string = "my text"
# def reverse_text(string):

#     reverse_str = string[::-1]
#     print(reverse_str)

# reverse_text(string)

# file_path = r"C:\Users\Segun\Desktop\cohort4b1wknd\materials\statement2.csv" #make to get you corresponding file path
# file = open(file=file_path, mode = "r")

file_path = "C:/Users/Segun/Desktop/cohort4b1wknd/materials/statement2.csv" #make to get you corresponding file path
file = open(file=file_path, mode = "r")

statement = file.readlines()
print(statement)

# for value in statement:
#     print(value)
#     print("\n\n")

statement_file = open(file_path, "r")# calling open builtin function using positional argument

for line in statement_file:

    splitted_line = line.split(",")
    # lodgement = splitted_line[4]
    # description = splitted_line[6]
    # # print(line.split(",")[4])
    # # print("\n\n")
    # print(lodgement, description, sep = "            ")


def get_count_of_transaction(file_path, target_amount, target_column, description_col):

    statement_file = open(file_path, "r")# calling open builtin function using positional argument
    count_500 = 0

    for line in statement_file:

        splitted_line = line.split(",")
        withdrawal = splitted_line[target_column]
        description = splitted_line[description_col]

        if withdrawal == target_amount:
            print(description)
            count_500 += 1

    print(f"Total {target_amount} : ", count_500)

get_count_of_transaction(file_path, "500.00", 3, 6)

