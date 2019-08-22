# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
import re
from Exception_Handling import *

def sort_words(input_list):
	'''
	The function sorts the list in ascending order
	Parameter:
		input_list(list):It is a list that contains the string value given by the user
		Returns:
			input_list(list):The user sorted user list in ascending order
	'''
	input_list.sort()
	return input_list

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
	try:
		user_input=input("Please enter the words to be sorted separated using (,) (Eg:-red,black,green,blue):")
		user_list=convert_into_list(user_input)
		for i in user_list:
			if(re.search("^[^a-zA-Z]*$",i)):
				raise OnlyCharactersExpression
		sorted_words=sort_words(user_list)
		print("The result after sorting words is:\n{}".format(sorted_words))
	except OnlyCharactersExpression as OnlyChar:
		print("The input should contain only characters")
		print("Special characters(!,@,#,%,&,*) and digits are not allowed")




if __name__=="__main__":
    main()