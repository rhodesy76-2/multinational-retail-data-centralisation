
# %%
my_list = []
dict_1 = {'London': [51.509865,-0.118092]} 
dict_2 = {'Paris': [48.864716, 2.349014]}
my_list.append(dict(dict_1))
my_list.append(dict(dict_2))
print(my_list)
#%

dict_1 = {'London': [51.509865,-0.118092]} 
dict_2 = {'Paris': [48.864716, 2.349014]}
my_list = [dict_1,dict_2]
for index in range(len(my_list)):
    for key, value in my_list[index].items():
        print(key, value[0])
#%%
my_list = [{'London': [51.509865, -0.118092]}, {'Paris': [48.864716, 2.349014]}]

for index in range(len(my_list)):
    for key, value in my_list[index].items():
        print(key, value[0])
# %%
dict_1 = {"name" : "James", "age" : 46, "favourite_colour" : "green"}
dict_2 = {"name" : "Regina", "age" : 47, "favourite_colour" : "gray"}
dict_3 = {"name" : "Lucy", "age" : 7, "favourite_colour" : "purple"}
all_dict = [dict_1, dict_2, dict_3] 
new_dict = {d['name']:{'age': d['age'], 'favourite_colour': d['favourite_colour']} for d in all_dict}
print(new_dict)
# %%
def count_characters(word_list):
  """
  This function takes a list of words and returns the total number of characters in the list.

  Args:
    word_list (list): List of strings to be counted 

  Returns:
    int: The total number of characters
  
  """
  character_count = 0 
  for word in word_list:
      character_count+=len(word)
  return character_count

# Use the following code to test the function
test_word_list = ['hello', 'world'] 
characters = count_characters(test_word_list)
print(characters) # this should print out 10
# %%
def count_chars(words: list) -> int:
    """ Count all characters across a list of words.

    Args:
        words (list): A list of strings.
    
    Returns:
        int: The total number of characters in the list of words. 
    """
    num_chars = 0 
    for word in words:
        num_chars += len(word)
    return num_chars

# Use the following code to test the function
test_word_list = ['hello', 'world'] 
characters = count_chars(test_word_list)
print(characters) # this should print out 10
# %%
class Phone:
  def __init__(self, number, balance = 20):
    self.number = number
    self.balance = balance

  def make_call(self, number, duration=1):
    if self.balance >= duration:
      print(f"Calling {number} for {duration} minutes")
      self.balance -= duration
    else:
      print("Insufficient balance.")

  def info(self):
    print("Phone Number:", self.number)
    print("Balance:", self.balance)
    
my_phone = Phone('07771234567')

# Make a call
my_phone.make_call('07412127895')

# View info
my_phone.info()
# %%
