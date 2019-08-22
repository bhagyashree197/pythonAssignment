# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

import re

def convert_into_list(user_input):
    '''
    The function converts the user_input which is in string format into the list 
    
    Parameters:
        user_input(string):The input given by the user in string format

    Returns:
        It returns the list format of the user given string
    '''

    user_input_list=user_input.split(",")
    return user_input_list
    
def main():
    '''
    This is the main function from where the execution begins
    It is responsible for taking the input from user and call various functions
    '''

    user_input=input("Enter the Password(seperated by ,):")
    user_list=convert_into_list(user_input)
    new_list=[]
    i=0
    for counter in user_list:
        
        #checks whether the individual values of list matches the pattern or not
        temp=re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])(?=.{6,12})",counter)
        if temp:
            #If the string matches the pattern 
            new_list.append(counter)
            i=1
    if i==0:
        #If there are no string that match the Password criteria
        print("None of the input Passwords match the Password Criteria")
    else:
        #If atleat one string match the criteria
        print("The Password input that match the Password criteria are")
        print(",".join(new_list))
    
if __name__ == "__main__":
    main()