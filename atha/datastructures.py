names = ["john", "slim", "kunle", "ini"]
salaries = [23000, 1000, 23000, 50000, 13000]

# append

names.append("sam")
salaries.append(30000)

print(names, salaries)

new_staff = ["josh", "evelyn", "richy"]
new_staff_salaries = [100000, 120000, 90000]

for i in range(3):
    print(i)
    print(new_staff[i])
    names.append(new_staff[i])

print(names)