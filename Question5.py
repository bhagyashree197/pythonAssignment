def count_digits_and_characters(user_string):
    character_count=digit_count=0
    for counter in user_string:
        counter=ord(counter)
        if ((counter>=ord('a') and counter <=ord('z')) or (counter >= ord('A') and counter <= ord('Z'))):
            character_count+=1
        elif counter>=ord('0') and counter<=ord('9'):
            digit_count+=1
    return character_count,digit_count
    
def main():
    print("Calculate Number Of Digits And Characters In The String")
    user_input=input("Please Enter a string:")
    character_count,digit_count=count_digits_and_characters(user_input)
    print("Number of characters in the string: %d"%character_count)
    print("Number of digits in the string is %d"%digit_count)
   
if __name__=="__main__":
    main()