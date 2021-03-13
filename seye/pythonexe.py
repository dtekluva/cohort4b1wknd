# new_file = open("C:/Users/Adeola/Desktop/Python_Doc.txt", mode = "w")
# new_file.write("Name Age Gender\n")

# info_list = ["James 34 Male", "Titi 21 Female"]

# for info in info_list:
#     new_file.writelines(info)
#     new_file.write("\n")


# new_file.close()

# read_file = open("C:/Users/Adeola/Desktop/Python_Doc.txt", mode = "r")
# output1 = read_file.readlines()
# print(output1)
 
# # output2 = read_file.read()
# # print(output2)


# # import csv
# # note = open("C:/Users/Adeola/Desktop/Python_Doc/school record.csv", mode = "w", newline = "")
# # pen = csv.writer(note)

# # fields = ["Name", "Subject", "Grade"]
# # pen.writerow(fields)

# # records = [["Anita", "Biology", "C4"], ["Luke", "Further Maths", "B2"], ["Ismail", "IRK", "E8"], ["Henry", "Music", "A1"]]
# # pen.writerows(records)

# # note.close()


# import xlwt
# from tempfile import TemporaryFile

# book = xlwt.Workbook()
# sheet_one = book.add_sheet("health_records")
# sheet_two = book.add_sheet("employee_records")

# # row 1
# sheet_one.write(0, 0, "Name")
# sheet_one.write(0, 1, "Age")
# sheet_one.write(0, 2, "Genotype")

# # row 2
# sheet_one.write(1, 0, "Adamu")
# sheet_one.write(1, 1, 15)
# sheet_one.write(1, 2, "AS")

# # row 3
# sheet_one.write(2, 0, "Marcaus")
# sheet_one.write(2, 1, 56)
# sheet_one.write(2, 2, "SC")

# # row 4
# sheet_one.write(3, 0, "Amelia")
# sheet_one.write(3, 1, 22)
# sheet_one.write(3, 2, "AA")

# # row 5
# sheet_one.write(4, 0, "Carrick")
# sheet_one.write(4, 1, 38)
# sheet_one.write(4, 2, "AS")


# # for the second sheet
# sheet_two.write(0, 0, "Name")
# sheet_two.write(0, 1, "Age")
# sheet_two.write(0, 2, "Payroll")


# name = "C:/Users/Adeola/Desktop/Python_Doc/Hospitalfile.xls"
# book.save(name)
# book.save(TemporaryFile())


# FUNCTIONS
def bone_cracker():
    print("This function cracks bones!")

# bone_cracker()

# yo = lambda x : 50 + x
# print(yo(5))

# def my_adder(x):
#     output = 50 + x
#     print(output)

# my_adder(5)    

# def my_adder(x):
#     output = 50 + x
#     return output

# print(my_adder(5))    

# # Arbitrary Arguments
# def greetings(*names):
#     print("Hello" +"" + names[1])


# greetings("James", "Harley", "Stones")

# Keyword argument
def fruit_loops(fruit2, fruit1):
    print("My favourite is" + " " + fruit1)


fruit_loops(fruit1 = "Apple", fruit2 = "Graperr")    