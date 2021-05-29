# x = [1,2,3,4] # list 
# y = (1,2,3,4) # tuple

# x[0]= "ada"
# print(x)
# y[0] = 4
# print(y)

# data = {}

# name = input("Please enter name : ")
# math = input("Please enter math : ")
# eng = input("Please enter eng : ")
# french = input("Please enter french : ")
# igbo = input("Please enter igbo : ")

# # data["name"] = True
# # data["age"] = 30
# # data["color"] = "red"

# # print(data)

# data[name] = dict(
#     eng = eng,
#     math = math,
#     french = french,
#     igbo = igbo
# )

# print(data)


data = {}

while True:

    name = input("Please enter name : ")
    math = input("Please enter math : ")
    eng = input("Please enter eng : ")
    french = input("Please enter french : ")
    igbo = input("Please enter igbo : ")

    # data["name"] = True
    # data["age"] = 30
    # data["color"] = "red"

    # print(data)

    data[name] = dict(
        eng = eng,
        math = math,
        french = french,
        igbo = igbo
    )

    print(data)