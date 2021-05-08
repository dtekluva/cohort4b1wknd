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
list methods = .append(), .extend(), .insert(index location, word to be inserted), .remove(the particular word), .pop(automatically starts popping from -1), ,pop(the index location). 


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

# DICTIONARIES
Dictionary elements are not accessed by numerical index rather they are accessed by their keys or .items

MLB_team can then also be defined this way:

>>> MLB_team = dict([
...     ('Colorado', 'Rockies'),
...     ('Boston', 'Red Sox'),
...     ('Minnesota', 'Twins'),
...     ('Milwaukee', 'Brewers'),
...     ('Seattle', 'Mariners')
... ])
If the key values are simple strings, they can be specified as keyword arguments. So here is yet another way to define MLB_team:

>>> MLB_team = dict(
...     Colorado='Rockies',
...     Boston='Red Sox',
...     Minnesota='Twins',
...     Milwaukee='Brewers',
...     Seattle='Mariners'
... )

A value is retrieved from a dictionary by specifying its corresponding key in square brackets ([]):

>>> MLB_team['Minnesota']
'Twins'
>>> MLB_team['Colorado']
'Rockies'


If you refer to a key that is not in the dictionary, Python raises an exception:
>>> MLB_team['Toronto']
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    MLB_team['Toronto']
KeyError: 'Toronto'


Adding an entry to an existing dictionary is simply a matter of assigning a new key and value:
>>> MLB_team['Kansas City'] = 'Royals'
>>> MLB_team
{'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Seattle': 'Mariners', 'Kansas City': 'Royals'}
If you want to update an entry, you can just assign a new value to an existing key:

>>> MLB_team['Seattle'] = 'Seahawks'
>>> MLB_team
{'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Seattle': 'Seahawks', 'Kansas City': 'Royals'}


To delete an entry, use the del statement, specifying the key to delete:

>>> del MLB_team['Seattle']
>>> MLB_team
{'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Kansas City': 'Royals'}

Building a Dictionary Incrementally
Defining a dictionary using curly braces and a list of key-value pairs, as shown above, is fine if you know all the keys and values in advance. But what if you want to build a dictionary on the fly?

You can start by creating an empty dictionary, which is specified by empty curly braces. Then you can add new keys and values one at a time:

>>> person = {}
>>> type(person)
<class 'dict'>

>>> person['fname'] = 'Joe'
>>> person['lname'] = 'Fonebone'
>>> person['age'] = 51                         # if the key is an integer, no need to put the interger in str " "
>>> person['spouse'] = 'Edna'
>>> person['children'] = ['Ralph', 'Betty', 'Joey']
>>> person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}

Once the dictionary is created in this way, its values are accessed the same way as any other dictionary:
>>> person
{'fname': 'Joe', 'lname': 'Fonebone', 'age': 51, 'spouse': 'Edna',
'children': ['Ralph', 'Betty', 'Joey'], 'pets': {'dog': 'Fido', 'cat': 'Sox'}}

>>> person['fname']
'Joe'
>>> person['age']
51
>>> person['children']
['Ralph', 'Betty', 'Joey']

Retrieving the values in the sublist or subdictionary requires an additional index or key:
>>> person['children'][-1]
'Joey'
>>> person['pets']['cat']
'Sox'
This example exhibits another feature of dictionaries: the values contained in the dictionary don’t need to be the same type. In person, some of the values are strings, one is an integer, one is a list, and one is another dictionary.


You can even use built-in objects like types and functions:

>>> d = {int: 1, float: 2, bool: 3}
>>> d
{<class 'int'>: 1, <class 'float'>: 2, <class 'bool'>: 3}
>>> d[float]
2

However, there are a couple restrictions that dictionary keys must abide by.

First, a given key can appear in a dictionary only once. Duplicate keys are not allowed. A dictionary maps each key to a corresponding value, so it doesn’t make sense to map a particular key more than once.

You saw above that when you assign a value to an already existing dictionary key, it does not add the key a second time, but replaces the existing value:

Secondly, a dictionary key must be of a type that is immutable.
MEANING, LISTS AND DICTIONARIES CANNOT BE DICTIONARY KEYS BECAUSE THEY ARE MUTABLE.
 You have already seen examples where several of the immutable types you are familiar with—integer, float, string, and Boolean—have served as dictionary keys.

A tuple can also be a dictionary key, because tuples are immutable:

>>> d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
>>> d[(1,1)]
'a'
>>> d[(2,1)]
'c'
(Recall from the discussion on tuples that one rationale for using a tuple instead of a list is that there are circumstances where an immutable type is required. This is one of them.)

However, neither a list nor another dictionary can serve as a dictionary key, because lists and dictionaries are mutable:

>>> d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}
TypeError: unhashable type: 'list'


By contrast, there are no restrictions on dictionary values. Literally none at all. A dictionary value can be any type of object Python supports, including mutable types like lists and dictionaries, and user-defined objects, which you will learn about in upcoming tutorials.

There is also no restriction against a particular value appearing in a dictionary multiple times:

>>> d = {0: 'a', 1: 'a', 2: 'a', 3: 'a'}
>>> d
{0: 'a', 1: 'a', 2: 'a', 3: 'a'}
>>> d[0] == d[1] == d[2]
True


# DICTIONARY METHODS
.clear(), .get(key, else anything), .items(), .keys(), .values(), .pop(), .pop(key), .pop(item), .update(), .del()



>>> d = {'a': 10, 'b': 20, 'c': 30}

>>> print(d.get('b'))
20
>>> print(d.get('z'))
None
If <key> is not found and the optional <default> argument is specified, that value is returned instead of None:

>>> print(d.get('z', -1))
-1
d.items() returns a list of tuples containing the key-value pairs in d. The first item in each tuple is the key, and the second item is the key’s value:

>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d
{'a': 10, 'b': 20, 'c': 30}

>>> list(d.items())
[('a', 10), ('b', 20), ('c', 30)]
>>> list(d.items())[1][0]
'b'
>>> list(d.items())[1][1]
20

Any duplicate values in d will be returned as many times as they occur:

>>> d = {'a': 10, 'b': 10, 'c': 10}
>>> d
{'a': 10, 'b': 10, 'c': 10}

>>> list(d.values())
[10, 10, 10]

d.pop(<key>[, <default>])
Removes a key from a dictionary, if it is present, and returns its value.

If <key> is present in d, d.pop(<key>) removes <key> and returns its associated value:

>>> d = {'a': 10, 'b': 20, 'c': 30}

>>> d.pop('b')
20
>>> d
{'a': 10, 'c': 30}
d.pop(<key>) raises a KeyError exception if <key> is not in d:


d.popitem()
Removes a key-value pair from a dictionary.

d.popitem() removes the last key-value pair added from d and returns it as a tuple:

>>> d = {'a': 10, 'b': 20, 'c': 30}

>>> d.popitem()
('c', 30)
>>> d
{'a': 10, 'b': 20}

>>> d.popitem()
('b', 20)
>>> d
{'a': 10}
If d is empty, d.popitem() raises a KeyError exception:

>>> d = {}
>>> d.popitem()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d.popitem()
KeyError: 'popitem(): dictionary is empty'

# just so you know: Note: In Python versions less than 3.6, popitem() would return an arbitrary (random) key-value pair since Python dictionaries were unordered before version 3.6.

d.update(<obj>)
Merges a dictionary with another dictionary or with an iterable of key-value pairs.

If <obj> is a dictionary, d.update(<obj>) merges the entries from <obj> into d. For each key in <obj>:

If the key is not present in d, the key-value pair from <obj> is added to d.
If the key is already present in d, the corresponding value in d for that key is updated to the value from <obj>.
Here is an example showing two dictionaries merged together:

>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d2 = {'b': 200, 'd': 400}

>>> d1.update(d2)
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}
In this example, key 'b' already exists in d1, so its value is updated to 200, the value for that key from d2. However, there is no key 'd' in d1, so that key-value pair is added from d2.

<obj> may also be a sequence of key-value pairs, similar to when the dict() function is used to define a dictionary. For example, <obj> can be specified as a list of tuples:

>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d1.update([('b', 200), ('d', 400)])
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}
Or the values to merge can be specified as a list of keyword arguments:

>>> d1 = {'a': 10, 'b': 20, 'c': 30}
>>> d1.update(b=200, d=400)
>>> d1
{'a': 10, 'b': 200, 'c': 30, 'd': 400}

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2, z = 300)
print(d1)

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)
print(d1)


d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2, z = 300, f = (1,2))
print(d1)

# Another way to define dictionaries
d = {}
d ['key1'] = 900
d['key2'] = 800
d['key76'] =700

print(d.get('key1'))

# also pls note that we cannot slice a dictionary

x = ['a', 'b', {'foo': 1,'bar':  {'x' : 10,'y' : 20,'z' : 30}, 'baz': 3}, 'c', 'd']

print(x[2]['bar']['z'])    # remember, dictionaries are called by their keys, not index. it is list that is called by its index.

































































