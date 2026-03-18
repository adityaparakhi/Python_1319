'''
Program: Functions with Return
Q1: Palindrome
Q2: Reverse Number
Q3: Even or Odd
Q4: Prime Number
'''


print("==================================\n==================================")
# 1. Palindrome Function

def palindrome(num):
    temp = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if temp == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"



# call
print("\n--- Palindrome Check ---")
num = 121
result = palindrome(num)
print("Given Number: ", num)
print("Output: ", result)



print("==================================\n==================================")



# 2. Reverse Number Function

def revNum(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return rev


# call
print("\n--- Reverse Number ---")
num = 1234
result = revNum(num)
print("Given Number: ", num)
print("Output: ", result)



print("==================================\n==================================")


# 3. Even or Odd Function

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# call
print("\n--- Even or Odd ---")
num = 7
result = even_odd(num)
print("Given Number: ", num)
print("Output: ", result)



print("==================================\n==================================")

# 4. Prime Number using Function and return

def check_prime(num):
    if num <= 1:
        return "Not Prime"

    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"

    return "Prime Number"


# call
print("\n--- Prime Number ---")
num = 7
result = check_prime(num)
print("Givn Number: ", num)
print("Output: ", result)