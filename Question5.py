# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def count_digits_and_characters(user_string):
    '''
    The function counts the number of characters and digits in the string
    Parameter:
        user_string(string):It is the string in which number of characters and digits is to be calculated
    Returns:
        character_count(int):Number of characters in the string
        digit_count(int):Number of digits in the string
    '''

    character_count=digit_count=0
    for counter in user_string:
        counter=ord(counter)
        if ((counter>=ord('a') and counter <=ord('z')) or (counter >= ord('A') and counter <= ord('Z'))):
            character_count+=1
        elif counter>=ord('0') and counter<=ord('9'):
            digit_count+=1
    return character_count,digit_count
    
def main():
    '''
    This is the main function from where the execution begins
    It is responsible for taking the input from user and call various functions
    '''

    print("Calculate Number Of Digits And Characters In The String")
    user_input=input("Please Enter a string:")
    character_count,digit_count=count_digits_and_characters(user_input)
    print("Number of characters in the string: %d"%character_count)
    print("Number of digits in the string is %d"%digit_count)
   
if __name__=="__main__":
    main()