# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

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

    user_input=input("Please enter the binary numbers whose divisibility is to be checked separated by (,)(Eg:-1010,1011,1111):")
    user_list=convert_into_list(user_input)
    i=0
    new_list=[]
    for counter in user_list:
        flag=check_divisibility(counter)
        if(flag==True):
            new_list.append(counter)
            i+=1
    if(i==0):
        print("None of these numbers are divible by 5")
    else:
        print("The numbers divisible by 5 are:")
        print (",".join(new_list))
            
if __name__=="__main__":
    main()
     