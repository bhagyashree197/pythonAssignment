# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def count_digits_and_characters(user_string):
    '''
    The function counts the number of uppercase and lowercase characters within a string
    Parameter:
        user_string(list):List whose uppercase and lowercase characters is to be counted
    Returns
        uppercase_count(int):Number of uppercase characters
        lowercase_count(int):Number oflowercase characters
    '''
    uppercase_count=lowercase_count=0
    for counter in user_string:
        if (counter.isupper()):
            uppercase_count+=1
        elif counter.islower():
            lowercase_count+=1
    return uppercase_count,lowercase_count
    
def main():
    '''
    This is the main function from where the execution begins
    It is responsible for taking the input from user and call various functions
    '''

    print("Count Number Of Uppercase And Lowercase Characters In The String")
    user_input=input("Please Enter a string:")
    uppercase_count,lowercase_count=count_digits_and_characters(user_input)
    print("Number of UpperCase characters in the string: %d"%uppercase_count)
    print("Number of LowerCase characterd in the string is %d"%lowercase_count)
   
if __name__=="__main__":
    main()
     