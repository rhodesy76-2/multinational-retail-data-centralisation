#%% 
my_set = {1,2,3}
print(my_set)
print(type(my_set))

# %%
my_set_2 = set[3,4,5]
print(my_set_2)
print(type(my_set_2))
# %%
for x in my_set:
    print(x)
# %%
set_int = {8, 16, 24, 1, 25, 3, 10, 65, 55} 
set_str = {'f', 'l', 'k', 'a', 'w'}
max(set_int)
#%%
max(set_str)
# %%
set_int = {4, 12, 10, 9, 4, 13} 
set_str = {'b', 'z', 't', 'm', 'y', 'c'}
min(set_int)
# %%
min(set_str)
# %%
prime_numbers = {3, 5, 7, 11, 13}
prime_numbers.add(17)
#%%
print(prime_numbers)
# %%
prime_numbers = {3, 5, 7, 11, 13}
prime_numbers_2 = {17, 19, 23, 29}
prime_numbers.update(prime_numbers_2)
print(prime_numbers)
# %%
set1 = {15, 25, 35, 45, 55} 
set2 = {35, 45, 55, 65, 75}
union_set = set1.intersection(set2)
print(union_set)
# %%
set1 = {15, 25, 35, 45, 55} 
set2 = {35, 45, 55, 65, 75}
unique_set_1 = set1.difference(set2)
print(unique_set_1)
unique_set_2 = set2.difference(set1)
print(unique_set_2)
# %%
set1 = {15, 25, 35, 45, 55} 
set2 = {35, 45, 55, 65, 75}
unique_both = set1.symmetric_difference(set2)
print(unique_both)
# %%
list1 = [1, 2, 3, 4, 5, 6, 7, 8] 
list2 = [5, 6, 7, 8, 9, 10, 11, 12]
set_1 = set(list1)
set_2 = set(list2)
unique_both = set_1.symmetric_difference(set_2)
print(unique_both)
unique_both_2 = set_2.symmetric_difference(set_1)
print(unique_both_2)
# %%
list1 = [1, 5, 10, 20, 40, 80]
list2 = [6, 7, 20, 80, 100]
list3 = [3, 4, 15, 20, 30, 70, 80, 120]
set1=set(list1)
set2=set(list2)
set3=set(list3)
interset1 = set1.intersection(set2)
finalinterset= interset1.intersection(set3)
print(finalinterset)
interset = set1.intersection(set2).intersection(set3)
print(interset)
# %%
