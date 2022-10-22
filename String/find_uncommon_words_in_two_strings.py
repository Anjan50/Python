'''                ---::Source Code::---                 '''
list3 = []                # declaring empty list to store uncommon items
str1 = input("Enter the 1st string: ")        # taking string 1 from user
list1 = str1.split()
str2 = input("Enter the 2nd string: ")        # taking string 2 from user
list2 = str2.split()
for i in list1:               # loop to find items present in string 1 but not in string 2
  if i not in list2:
    list3.append(i)
for i in list2:               # loop to find items present in string 2 but not in string 1
  if i not in list1:
    list3.append(i)
print("All the uncommon items among the given two lists are:--\n",list3)        # displaying uncommon items

'''                    ---::Output::---
>>> Enter the 1st string: Python is type of snake.
>>> Enter the 2nd string: Python is also a programming language.
All the uncommon items among the given two lists are:--
 ['type', 'of', 'snake.', 'also', 'a', 'programming', 'language.']
'''
