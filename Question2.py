def generate_array(row,col):
    new_list=[]
    for counter in range(row):
        temp_list=[]
        for count in range(col):
            result=counter*count
            temp_list.append(result)
        new_list.append(temp_list)
    return new_list    
        
def convert_into_list(user_input):
    user_input_list=user_input.split(",")
    for i in range(len(user_input_list)):
        user_input_list[i]=int(user_input_list[i])
    return user_input_list
    
def main():
    user_input=input("Please enter the number of Rows and Columns separated by a (,) (Ex:-2,3):");
    user_list=convert_into_list(user_input)
    user_result=generate_array(user_list[0],user_list[1])
    print("The generated output is:\n{}".format(user_result))
    
if  __name__=="__main__":
    main()
    