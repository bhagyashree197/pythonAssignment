from math import *

def calculate_value(input_list):
    new_list=[]
    C=50
    H=30
    for counter in input_list:
        new_list.append(round(sqrt((2 * C *counter)/H)))
    return new_list

def convert_into_list(user_input):
    user_input_list=user_input.split(",")
    for i in range(len(user_input_list)):
        user_input_list[i]=int(user_input_list[i])
    return user_input_list
    
def main():
    user_input=input("Please Enter the numbers to be calculated(Separate the number using (,)):")
    user_input_list=convert_into_list(user_input)
    user_result=calculate_value(user_input_list)
    print("The result is\n{}".format(user_result))
    

if  __name__=="__main__":
    main()
        