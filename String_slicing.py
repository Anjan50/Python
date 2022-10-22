# String slicing in Python to check if a string can become empty by recursive deletion

def is_valid(string, sub_string):
   # checking the lengths of string and sub_string
   if len(string) > 0 and len(sub_string):
      # iterating until string becomes empty
      while len(string) > 0:
         # finding the sub_string in string
         index = string.find(sub_string)
         # checking whether its present or not
         if index == -1:
            # returning false
            return False
         # removind the sub_string
         string = string[0: index] + string[index + len(sub_string):]
      # returning True
      return True
   else:
      # returning False
      return False
if __name__ == '__main__':
   # initializing the string and string
   string = 'tutorialstutorialspointpoint'
   sub_string = 'tutorialspoint'
   # invoking the method
   print(is_valid(string, sub_string))
