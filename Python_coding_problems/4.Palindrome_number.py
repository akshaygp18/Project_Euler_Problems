# Largest Palindrome Product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(n):
    # Convert the number to a string
    num_str = str(n)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

def largest_palindrome_product():
    largest_palindrome = 0

    for num1 in range(999, 99, -1):
        for num2 in range(num1, 99, -1):
            product = num1 * num2
            if product > largest_palindrome and is_palindrome(product):
                largest_palindrome = product
    
    return largest_palindrome

result = largest_palindrome_product()
print(result)
