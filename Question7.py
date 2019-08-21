import re

def convert_into_list(user_input):
    user_input_list=user_input.split(",")
    return user_input_list
    
def main():
    user_input=input("Enter the Password(seperated by ,):")
    user_list=convert_into_list(user_input)
    new_list=[]
    i=0
    for counter in user_list:
        temp=re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])(?=.{6,12})",counter)
        if temp:
            new_list.append(counter)
            i=1
    if i==0:
        print("None of the input Passwords match the Password Criteria")
    else:
        print("The Password input that match the Password criteria are")
        print(",".join(new_list))
    
if __name__ == "__main__":
    main()