# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
import re
from Exception_Handling import *
def check_divisibility(number):
    '''
    The function converts the value in decimal form and checks whether it is divisible by 5
    Parameters:
        number(int):It is the number whose divisibilty is to be checked
    Returns:
        True/False(bool):It return True-if devisible else returns False
    '''
    
    if int(number,2) % 5 == 0:
        return True
    return False

def convert_into_list(user_input):
    '''
    The function converts the user_input which is in string format into the list 
    
    Parameters:
        user_input(string):The input given by the user in string format

    Returns:
        user_input_list(list):It returns the list format of the user given string
    '''

    user_input_list=user_input.split(",")
    return user_input_list
    
def main():
    '''
    This is the main function from where the execution begins
    It is responsible for taking the input from user and call various functions
    '''
    try:
        user_input=input("Please enter the binary numbers whose divisibility is to be checked separated by (,)(Eg:-1010,1011,1111):")
        user_list=convert_into_list(user_input)

        i=0
        new_list=[]
        for counter in user_list:
            if(re.search("^[^0|1]*$",counter)):
                raise NotABinaryNumberException(counter)
            flag=check_divisibility(counter)
            if(flag==True):
                new_list.append(counter)
                i+=1
        print("The numbers you entered,in decimal are:")
        for j in user_list:
            print(j,"(",int(j,2),")",end=" ")
        if(i==0):
            print("\nNone of these numbers are divible by 5")
        else:
            print("\nThe numbers divisible by 5 are:")
            print (",".join(new_list))

    except NotABinaryNumberException as NABN:
        print("Invalid Input:",NABN.value,"is not a Binary number")
        print("Please Enter Only Binary numbers(Number that consists of only 0 and 1)")
            
if __name__=="__main__":
    main()
     