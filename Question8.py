'''
 Define a class with a generator which can iterate the numbers,
 which are divisible by 7, between a given range 0 and n.
'''

class get_numbers_divisible_by7:
    '''
    The class that consists of a generator that generates the value from 0 to n 
    and returns only those numbers that are divisible by 7
    '''
    def __init__(self,number_range):
        '''
        This function accepts the input passed by individual object
        Parameter:
            number_range:Represents until which number the generator should iterate
        '''

        self.number_range=number_range
    
    def generator_for_divisibilty(self):
        '''
        This is a generator that generates number from 0 to number_range.
        And returns only those values that are divisible by 7
        Returns:
            The number that are divisible by 7
        '''

        for count in range(self.number_range):
            if(count % 7 == 0):
                yield count
            else:
                continue
def main():
    '''
    This is the main function from where the execution begins
    It is responsible for taking the input from user and call various functions
    '''

    number_range=int(input("Please Enter the range:"))
    c1=get_numbers_divisible_by7(number_range)
    numbers_divisible=c1.generator_for_divisibilty()
    print("The numbers divible by 7 till the range {} are".format(number_range))
    for count in numbers_divisible:
        print(count,"",end=" ")
    print("\n")
        
if __name__ == "__main__":
    main()