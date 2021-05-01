# # working with APi
# import requests
# url = 'https://rest.coinapi.io/v1/assets'
# headers = {'X-CoinAPI-Key' : '8B93E1CC-D792-4716-9F57-87AA9D7DD4FC'}
# response = requests.get(url, headers=headers)
# print(response.json())

# file_name = "dataset.txt"
# file = open(file_name,'w')
# print(response.json(), file=file)


# # Other things to take note in working with APIs: the API format = contained in the API Documentation
# # API call, base URL, endpoint, headers(extra authentication parameter), API key etc. URL = Base URL + endpoint url
# # sites 1 to get free API: expertpowerplus/API
# # site 2 for creating free API: jsonbin.io

# # PLEASE READ UP ON LIST AND DICTIONARIES AND ASK PREPARE FOR DISCUSSIONS NEXT CLASS

# # LISTS - https://realpython.com/python-lists-tuples/
# # DICT - https://realpython.com/python-dicts/
# # FUNCTIONS - https://realpython.com/defining-your-own-python-function/


a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(a[2:5])
# ['baz', 'qux', 'quux']
# Other features of string slicing work analogously for list slicing as well:
# Both positive and negative indices can be specified:

# >>> a[-5:-2]
# ['bar', 'baz', 'qux']
# >>> a[1:4]
# ['bar', 'baz', 'qux']
# >>> a[-5:-2] == a[1:4]
# True

# pls check the list link above. it is well detailed.

# a=['foo', 'bar', 'baz', 'qux', 'quux', 'corge'] [3]
# a = a + "234"
# print(a)


# x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
# print(x[1][2][1][2])
# print(x[1][2][1:])


a=['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
del a[4] 
print(a)

You can also insert elements into a list without removing anything. Simply specify a slice of the form [n:n] (a zero-length slice) at the desired index:

>>> a = [1, 2, 7, 8]
>>> a[2:2] = [3, 4, 5, 6]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]

You can delete multiple elements out of the middle of a list by assigning the appropriate slice to an empty list. You can also use the del statement with the same slice:

>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>> a[1:5] = []
>>> a
['foo', 'corge']

>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>> del a[1:5]
>>> a
['foo', 'corge']


>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>> a += 20
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a += 20
TypeError: 'int' object is not iterable

>>> a += [20]
>>> a
['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 20]


# just like string methods, there are also list methods
list methods = .append(), .extend(), .insert(index location, word to be inserted), .remove(), .pop(), ,pop(the index location). 


>>> a = ['a', 'b']
>>> a.append([1, 2, 3])
>>> a
['a', 'b', [1, 2, 3]]    # .append() prints all together


>>> a = ['a', 'b']
>>> a.extend([1, 2, 3])
>>> a
['a', 'b', 1, 2, 3]        #while .extend() prints all separated
In other words, .extend() behaves like the + operator. More precisely, since it modifies the list in place, it behaves like the += operator:

>>> a = ['a', 'b']
>>> a += [1, 2, 3]
>>> a
['a', 'b', 1, 2, 3]


t = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
t[2] = 'Bark!'
print(t)

# t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
# t[2] = 'Bark!'
# print(t)       #this would give an error....supporting the fact that tuple object are not changeable

# this is how to append without removing anything = called zero-lenght slicing
t = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
t[2:2] = ['Bark!']
print(t)






















