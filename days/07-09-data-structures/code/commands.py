#!python3

numlist = [1, 2, 3, 4, 5]

>>> numlist
[1, 2, 3, 4, 5]
>>> numlist.reverse()
>>> numlist
[5, 4, 3, 2, 1]

>>> numlist.sort()
>>> numlist
[1, 2, 3, 4, 5]


>>> mystring = "julian"

>>> for i in list(mystring):
	print(i)

	
j
u
l
i
a
n



>>> l = list(mystring)
>>> t = tuple(mystring)
>>> 
>>> l
['j', 'u', 'l', 'i', 'a', 'n']
>>> 
>>> t
('j', 'u', 'l', 'i', 'a', 'n')



>>> l[0] = "b"
>>> 
>>> l
['b', 'u', 'l', 'i', 'a', 'n']
>>> 
>>> t[0] = "m"
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    t[0] = "m"
TypeError: 'tuple' object does not support item assignment
>>> 




>>> l.pop()
'n'
>>> l
['b', 'u', 'l', 'i', 'a']
>>> 


>>> l.insert(5, "n")
>>> 
>>> l
['b', 'u', 'l', 'i', 'a', 'n']
>>> 
>>> 




>>> l.pop(0)
'b'
>>> 
>>> l
['u', 'l', 'i', 'a', 'n']
>>> 



>>> l.insert(0, "m")
>>> 
>>> l
['m', 'u', 'l', 'i', 'a', 'n']
>>> 



>>> del l[0]
>>> 
>>> l
['u', 'l', 'i', 'a', 'n']
>>> 
>>> 





DICTS:

>>> pybites = {'julian': 30, 'bob': 33, 'mike': 33}
>>> 
>>> pybites
{'julian': 30, 'bob': 33, 'mike': 33}
>>> 


>>> people = {}
>>> people['julian'] = 30
>>> people
{'julian': 30}

>>> people['bob'] = 43
>>> people
{'julian': 30, 'bob': 43}
>>> 


>>> pybites.keys()
dict_keys(['julian', 'bob', 'mike'])
>>> 

>>> pybites.values()
dict_values([30, 33, 33])

>>> pybites.items()
dict_items([('julian', 30), ('bob', 33), ('mike', 33)])
>>> 

>>> for keys in pybites.keys():
	print(keys)

	
julian
bob
mike
>>> 

>>> for values in pybites.values():
	print(values)

	
30
33
33
>>> 

>>> for keys, values in pybites.items():
	print(keys + str(values))

	
julian30
bob33
mike33
>>> 

>>> for keys, values in pybites.items():
	print('%s is %d years of age' % (keys, values))

	
julian is 30 years of age
bob is 33 years of age
mike is 33 years of age
>>> 
