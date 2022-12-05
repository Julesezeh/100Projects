from factorfinder import factor_finder

#returns true if a number is a prime number
def is_prime(number):
    factors = factor_finder(number)
    basic_prime_numbers = [1,2,3,5,7]
    if  len(factors)==2:
        return True
    else:
        return False

#This function returns all the prime numbers from 0 to the specified number
def all_prime_numbers(number):
    prime_numbers = [str(x) for x in range(0,number+1) if is_prime(x)]
    return prime_numbers

if __name__ == "__main__":
    print("_____________________PRIME NUMBER FINDER____________________")
    print("By Jules Okoye-ezeh")
    print()
    print("This program takes a number from a user,and returns all the prime numbers that exist from zero up to that particular number")
    while True:
        choice = input("Enter a number: ")
        try:
            choice = int(choice)
            break
        except:
            print("\nInvalid input, Please enter a valid positive integer\n")
    all_prime = all_prime_numbers(choice)
    print()
    print("The prime numbers are: "+", ".join(all_prime))