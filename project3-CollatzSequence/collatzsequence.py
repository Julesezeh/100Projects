#1. If n is even, the next number n is n / 2.
#2. If n is odd, the next number n is n * 3 + 1.
#3. If n is 1, stop. Otherwise, repeat.

def main():
    print()
    print('_____________________COLLATZ SEQUENCE______________________')
    print("Please enter a non-negative number that isn't 0 or 1 ")
    sequence = []
    count=0
    while True:
        n = input(":> ")
        if n.isdigit() and int(n)>1:
            n = int(n)
            sequence.append(n)
            break
        elif count<2:
            print("Invalid input")
            count+=1
        else:
            print("Invalid input, Please enter a non negative integer that isn't 0 or 1")
            count = 0
    while n>1:
        if n%2==0:
            n=int(n/2)
        else:
            n = n*3+1
        sequence.append(n)

    for x in sequence:
        print(x,end=',')


if __name__ == "__main__":
    main()

