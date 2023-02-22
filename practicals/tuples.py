#%%
empty_tuple = ()
print(type(empty_tuple))
# %%
emptyTuple = tuple()
print(type(emptyTuple))
# %%
my_tuple = ("james", [1,2,3], (1,2,3))
print(type(my_tuple[0]))
print(type(my_tuple[1]))
print(type(my_tuple[2]))


# %%
my_tuple_2 = (1,2,3)
new_tuple = my_tuple_2 + my_tuple
print(new_tuple)
# %%
for x in my_tuple:
   
  # iterate in each tuple element
  for y in x:
      print(y)
       
  print()
# %%
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
vowels.count('i')
# %%
numbers = (1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6, 7, 7, 7)
numbers.count(7)
# %%
tuple = (1, 'f', [1, 2, 3], [4, 5], ('f', 'd'), ('f', 'd', 'e'), [1, 2, 3], 'a')
sum(tuple.count(x) for x in ([1, 2, 3], ('f', 'd')))
# %%
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
vowels.index('e')
# %%
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
vowels.index('i')
# %%
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
vowels.index('b')
# tuple.index(x): x not in tuple
# means b not in the touple
# %%
alphabet = ('a', 'e', 'i', 'o', 'u', 'g', 'l', 'i', 'u')
alphabet.index('i', 4, 8)
# %%
my_tuple = ("james", [1,2,3], (1,2,3), {"key": 3})
for x in my_tuple:
   
  # iterate in each tuple element
  for y in x:
      print(y)
       
  print()

# %%
tuple = (70, "AiCore", 10, "Programming", 70)
x, *y, z = tuple
print(x)
print(y)
print(z)
# %%
tuple = (70, "AiCore", 10, "Programming", 70) 
x, y, *z = tuple
print(x)
print(y)
print(z)
# %%
