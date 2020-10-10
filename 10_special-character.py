# Python3 program to check if a string  contains any special character 

# import required package 
import re 

# Function checks if the string contains any special character 
def run(string): 

    # Make own character set and pass this as argument in compile method 
    regex = re.compile('[@_!#$%^&*()<>?/}{~:]') 
    
    # Pass the string in search method of regex object.    
    if(regex.search(string) == None): 
        print "String is accepted" 
        
    else: 
        print "String is not accepted." 
    

# Driver Code 
if __name__ == '__main__' : 
    
    # Enter the string .You can edit the string of your choice
    string = "hack$oc@tober*^fest!!"
    
    # calling run function 
    run(string) 
