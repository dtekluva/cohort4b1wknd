n(file_path, target_amount_min, target_amount_max, target_column, description_col):

#     statement_file = open(file_path, "r").readlines() # calling open builtin function using positional argument
#     header = statement_file.pop(0) #remove first element or row from read file
#     count_500 = 0
#     sum_of_target =0

#     withdrawal_list = [header]

#     for line in statement_file:

#         splitted_line = line.split(",")
#         withdrawal = splitted_line[target_column]
#         float_withdrawal = float(withdrawal)

#         description = splitted_line[description_col]

#         if float_withdrawal <= target_amount_max and float_withdrawal >= target_amount_min:
#             print(float_withdrawal, description, sep = "                 ")
#             count_500 += 1
#             sum_of_target += float_withdrawal
#             withdrawal_list.append(line)

#     print(f"Total target : ", count_500)
#     print(f"Sum of target : ", sum_of_target)

#     return withdrawal_list

# filter = get_count_of_transaction(file_path, 6000, 100000 , 3, 6)
# print(filter)

# def writeback(data, name = "untitled.csv"):

#     file_name = name
#     file = open(f"materials/{name}", "a")

#     for line in data:

#         file.write(line)

#     file.close()

# writeback(filter, "Myfilter.csv")