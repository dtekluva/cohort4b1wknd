# MAP TAKES IN A FUNCTION AND AN ITERABLE AND CARRIES OUT THE FUNCTION ON EVERY MEMBER OF THE ITERABLE

words = ["salami", "tunde", "salau", "winston", "john"]

length_of_words = map(len, words)
mapped_object = length_of_words
unravelled_object = list(mapped_object)
print(unravelled_object)

reversed_words = map(reversed, words)

def reverse_for_real(value):
    return list(reversed(value))

mapped_object = map(reverse_for_real, words)

unravelled_object = list(mapped_object)
print(unravelled_object)

def add_number(name):
    return name + "->" + str(len(name))

print(list(map(add_number, words)))
ab = [2, 5, 7, 3, 7]

def square_rt(square):
    return square**2

print(list(map(square_rt,ab)))

string = "I am a boy and my name is james"
string2 = "       Jonah"
lower_case_version = string.lower()
print(lower_case_version)

upper_case_version = string.upper()
print(upper_case_version)

print(string2)
print(string2.strip())

print("Welcome to my small program \n")
Date_to_change = input("Please enter date: 
