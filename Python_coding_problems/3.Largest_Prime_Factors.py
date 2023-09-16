# Largest Prime Factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?


def largest_prime_factor(n):

    # Initilaize the largest prime factor
    largest_prime = 2

    # while n is greater than 1
    while n>1:
        # check if the current prime factor divides n
        if n % largest_prime == 0:
            # If it does, divide n by the prime factor
            n = n // largest_prime

        else:
            # If it doesn't, increment the current prime factor 
            largest_prime += 1
    
    return largest_prime

# Call the function with the number 600851475143
print(largest_prime_factor(600851475143))Even 