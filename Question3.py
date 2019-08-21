def sort_words(input_list):
    input_list.sort()
    return input_list

def convert_into_list(user_input):
    user_input_list=user_input.split(",")
    return user_input_list
    
def main():
    user_input=input("Please enter the words to be sorted separated using (,) (Eg:-red,black,green,blue):")
    user_list=convert_into_list(user_input)
    sorted_words=sort_words(user_list)
    print("The result after sorting words is:\n{}".format(sorted_words))
     
if __name__=="__main__":
    main()