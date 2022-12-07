def factor_finder(number):
    #loop through all numbers from 1 to the number itself and append the number to the 'factors' list if the inputed number is completely divisible by the number in the current loop 
    factors = [str(x) for x in range(1,number+1) if number%x==0]
    return factors


if __name__ == "__main__":
    print("_____________________FACTOR FINDER____________________")
    print("by Jules Okoye-ezeh")
    print("This program takes an interger input and returns all the factors of that number. ")
    print()
    while True:
        try:
            num = int(input("Enter Number: "))
            break
        except ValueError:
            print("\nPlease enter a valid positive integer\n")
    results = factor_finder(num)
    print( f"The factors of {num} are... "+', '.join(results))
