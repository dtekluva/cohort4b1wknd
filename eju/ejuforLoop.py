FOR LOOP IS USED TO LOOK THROUGH A COLLECTION.
a= ["foo", "baz", "bar" ]
for i in a:
    print(i)

students = [ "ali", "baba", "Bola", "salam"]
for student in students:
 print(student)

students = [ "ali", "baba", "Bola", "salam"]
for pizza in students:
 print(pizza)

students = [ "ali", "baba", "Bola", "salam"]
for pizza in students:
 print(pizza, end = ",")

print(iter("foobar"))

teams = ["liverpool", "acmilan", "arsenal", "juventus", "mancity", "barcelona"]
teams_iterator = iter(teams)
print(next(teams_iterator))
print(next(teams_iterator)) 
# SHIFT ALT DIRECTION - USED TO DUPLICATE A LINE
print(next(teams_iterator))
print(next(teams_iterator))
YOU CAN DO THE BELOW INSTEAD
for team in teams:
     print(team)
     input()

for team in reversed(teams):
    print(team)

d = {'foo':1, 'bar':2, 'baz': 3}
for k in d:
    # print(k)
    # print(d[k])
    for item in d.items():
        # THIS SHOWS KEY.VALUE
     print(item)
x = range(5)
for n in x:
    print(n)
RANGE IS START ,STOP, STEP
for i in range(1, 20, 4):
    print(i)

LET'S USE WHILE LOOP FOR THE ASSIGNMENT
for i in range (100, 1000):
    sum_i = i + i + i
    i_str = str(i)
    last_char = i_str[2] 
    last_char_multiple = last_char * 3


    if sum_i == int(last_char_multiple):
        print(i, sum_i, last_char, last_char_multiple)
        break
    i+=1

for i in range(1500,2701):
    number = 1500
    max_number = 2701

while number < max_number:
    if number % 7 == 0 and number % 5 == 0:
        print(f"Found, our number is {number}")
        
number += 1

 
for i in range(1499,2701):
 if i % 5 == 0 and i % 7 ==0:
    print("Found : ",i)

HOW DO WE COUNT THE TOTAL RESULTS

items_found= 0

for i in range(1500,2701):
  if i % 5 == 0 and i % 7 ==0:
    print(i)
    items_found += 1

print(items_found)

THIS IS THE SOLUTION TO THE QUESTION
for i in range (1,5):
    print("* "*i)

    if i==4:
        for i in range(5,0, -1):
            print("* "*i)

IF WE REMOVE THE NEGATIVE
for i in range (1,5):
    print("* "*i)

    if i==4:
        for i in range(5,0, 1):
            print("* "*i)

items_found= 0

for i in range(100,400):
  if i % 2 == 0:
    print(i)
    items_found += 1

    i_str = str(i)
for i in range(100,400):
    i_str = str(i)
    first_char = int(i_str[0])
    sec_char = int(i_str[1])
    third_char = int(i_str[2])

    if first_char % 2 ==0 and sec_char % 2 == 0 and third_char % 2 == 0:
        print(first_char, sec_char, third_char)



for i in range(100,400):
    i_str = str(i)
    first_char = int(i_str[0])
    sec_char = int(i_str[1])
    third_char = int(i_str[2])

    if first_char % 2 ==0 and sec_char % 2 == 0 and third_char % 2 == 0:

        print(i, end = ", ")
