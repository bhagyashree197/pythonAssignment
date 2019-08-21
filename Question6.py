def count_digits_and_characters(user_string):
    uppercase_count=lowercase_count=0
    for counter in user_string:
        if (counter.isupper()):
            uppercase_count+=1
        elif counter.islower():
            lowercase_count+=1
    return uppercase_count,lowercase_count
    
def main():
    print("Count Number Of Uppercase And Lowercase Characters In The String")
    user_input=input("Please Enter a string:")
    uppercase_count,lowercase_count=count_digits_and_characters(user_input)
    print("Number of UpperCase characters in the string: %d"%uppercase_count)
    print("Number of LowerCase characterd in the string is %d"%lowercase_count)
   
if __name__=="__main__":
    main()
     