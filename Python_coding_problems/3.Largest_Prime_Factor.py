# # Largest Prime Factor
# # Problem 3
# # The prime factors of 13195 are 5, 7, 13 and 29.
# # What is the largest prime factor of the number 600851475143?

# import pandas as pd
import pandas as pd

def largest_prime_factor(n):
    # Initialize the largest prime factor
    largest_prime = 2

    # Create an empty list to store prime factors
    prime_factors_list = []

    # While n is greater than 1
    while n > 1:
        # Check if the current prime factor divides n
        if n % largest_prime == 0:
            # If it does, divide n by the prime factor
            n = n // largest_prime

            # Add the prime factor to the list
            prime_factors_list.append(largest_prime)
        else:
            # If it doesn't, increment the current prime factor
            largest_prime += 1

    # Convert the list to a DataFrame
    prime_factors_df = pd.DataFrame({"Prime Factors": prime_factors_list})

    # Print the DataFrame containing prime factors
    print(prime_factors_df)

# Call the function with the number 600851475143
largest_prime_factor(600851475143)

