# print("hello")

# values = [2, 3, 1, 4, 5]

# sorted_values = values.sort(reverse=True)

# print(values)
# print(max(values))

# values = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# values.sort(key = lambda values: values[1])
# print(values)


def check_them (lista, listb):
    
    set_a = set(lista)
    set_b = set(listb)

    intersect = set_a.intersection(set_b)
    print(intersect)
    print("A and B a have atleast 1 common values: ", bool(intersect))

check_them([2,3,4,5,6], [3,4,5,6,7])