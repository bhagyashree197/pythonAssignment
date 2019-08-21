class get_numbers_divisible_by7:
    def __init__(self,number_range):
        self.number_range=number_range
    
    def generator_for_divisibilty(self):
        for count in range(self.number_range):
            if(count % 7 == 0):
                yield count
            else:
                continue
def main():
    number_range=int(input("Please Enter the range:"))
    c1=get_numbers_divisible_by7(number_range)
    numbers_divisible=c1.generator_for_divisibilty()
    print("The numbers divible by 7 till the range {} are".format(number_range))
    for count in numbers_divisible:
        print(count,"",end=" ")
    print("\n")
        
if __name__ == "__main__":
    main()