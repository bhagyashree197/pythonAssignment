# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H] 
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input. 

from math import *
import re
import sys
from Exception_Handling import *

def calculate_value(input_list):
    '''
    This function calculates the result based on the given formula.
     
     Parameters:
        input_list(list):The list whose result is to be calculated

     Return:
        new_list(list):The list of calculated values
    '''

    new_list=[]
    C=50
    H=30
    for counter in input_list:
        new_list.append(round(sqrt((2 * C *counter)/H)))
    return new_list


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
        user_input=input("Please Enter the numbers to be calculated(Separate the number using (,)):")
        user_input_list=convert_into_list(user_input)
        for i in range(len(user_input_list)):
            if (re.search("\D",user_input_list[i])):
                raise NotANumberException(user_input_list[i])
            else:
                user_input_list[i]=int(user_input_list[i])
        user_result=calculate_value(user_input_list)
        print("The result is\n{}".format(user_result))

    except NotANumberException as NumberException:
        print("Invalid Input:'{}' is not a number".format(NumberException.value))
        print("Only result of numbers can be calculated")
       

    
if  __name__=="__main__":
    main()
        