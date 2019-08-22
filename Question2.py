# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
from Exception_Handling import *
import re

def generate_matrix(row,col):
    '''
    The function is used to generate an array of dimension row*col where value of each cell
    is the product of row and column of that particular cell
    Parameters:
        row(int):The integer value that represents te number of rows the matrix should have.
        col(int):The integer value that represents te number of columns the matrix should have.
    Returns:
        new_list(list):It is a list containing the generated array.
    ''' 

    new_list=[]
    for counter in range(row):
        temp_list=[]
        for count in range(col):
            result=counter*count
            temp_list.append(result)
        new_list.append(temp_list)
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
        user_input=input("Please enter the number of Rows and Columns separated by a (,) (Ex:-2,3):");
        user_list=convert_into_list(user_input)
        if(len(user_list)<2 or len(user_list)>2):
            raise InAppropriateNumberOfValue()
        for i in range(len(user_list)):
            if (re.search("\D",user_list[i])):
                raise NotANumberException(user_list[i])
            user_list[i]=int(user_list[i])
        user_result=generate_matrix(user_list[0],user_list[1])
        print("The generated output is:\n{}".format(user_result))
    except NotANumberException as NumberException:
        print("Rows and Columns can only be a number")
        print("'{}' is not a number".format(NumberException.value))

    except InAppropriateNumberOfValue as IANOV:
        print("There can only be 2 inputs.")
        print("First One for number of rows and Second one for number of columns")


if  __name__=="__main__":
    main()
    