'''             ---:: SOURCE CODE ::---             '''
str1 = input("Enter the string: ")        # Taking input from user
list1 = list(str1)
str2 = ""

for i in list1:       # for loop for finind and swapping the commas and dots in the given string starts here ...
  if i==',':
    i = '.'
  elif i=='.':
    i = ','
    str2 += i       # ... for loop ends here

print("The given string after swapping commas and dots:--\n",str2)        # Giving output after swapping

'''
                ---:: OUTPUT ::---
>>> Enter the string: My name is Raj , I am from India .
The given string after swapping commas and dots:--
 My name is Raj . I am from India ,
'''
