file_path = r"C:\Users\Adebowale\Desktop\UNivelcity\DataScience class\cohort4b1wknd\materials\statement2.csv" #make to get you correspinding file path

statement_file = open(file_path, "r")

def get_count_of_transaction(file_path, target_column, description_col):

    statement_file = open(file_path, "r")# calling open builtin function using positional argument
    count_Desc = 0
    list_of_withdrawal =[]
    Description_word = input('Enter the Keyword:    ')
    for line in statement_file:

        splitted_line = line.split(",")
        withdrawal = splitted_line[target_column]
        description = splitted_line[description_col]
        # float_withdrawal = float(withdrawal)

        if Description_word in description:

                        
            print(description, withdrawal, sep='             ')
            count_Desc += 1
            list_of_withdrawal.append(withdrawal)

    print(f"Total {Description_word} : ", count_Desc)
    # print(list_of_withdrawal)
    print(f"Sum of target : ", sum(map(float,list_of_withdrawal)))

get_count_of_transaction(file_path, 3, 6)
