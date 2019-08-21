def check_divisibility(number):
    if int(number,2) % 5 == 0:
        return True
    return False

def convert_into_list(user_input):
    user_input_list=user_input.split(",")
    return user_input_list
    
def main():
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
     