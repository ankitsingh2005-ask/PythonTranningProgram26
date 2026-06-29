# Program to count the prime numbers in a given range
# take input from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# check for prime numbers in the range
for num in range(start, end + 1):
    # check if the number is greater than 1
    if num > 1: 
        # check for factors of num
        for i in range(2, num):
            # if num is divisible by any number between 2 and num-1, it is not prime
            if (num % i) == 0:
                break
            # if the loop completes without finding a factor, num is prime
        else:
            print(num, "is a prime number")