'''Pattern Using function'''

# 1. Square Pattern
def square(n):
    print("\nYou entered n =", n)
    print("Square Pattern:")
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


# 2. Right Triangle
def triangle(n):
    print("\nYou entered n =", n)
    print("Right Triangle:")
    for i in range(1, n+1):
        for j in range(i):
            print("*", end=" ")
        print()


# 3. Reverse Triangle
def reverse_triangle(n):
    print("\nYou entered n =", n)
    print("Reverse Triangle:")
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()


# 4. Hollow Square
def hollow_square(n):
    print("\nYou entered n =", n)
    print("Hollow Square:")
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# 5. Pyramid Pattern
def pyramid(n):
    print("\nYou entered n =", n)
    print("Pyramid Pattern:")
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(i):
            print("*", end=" ")
        print()


# 6. Reverse Pyramid
def reverse_pyramid(n):
    print("\nYou entered n =", n)
    print("Reverse Pyramid:")
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(i):
            print("*", end=" ")
        print()


# calling pattern functions
n = 5
square(n)
triangle(n)
reverse_triangle(n)
hollow_square(n)
pyramid(n)
reverse_pyramid(n)



'''Palindrome'''

# 1. Palindrome using while loop
def palindrome(num):
    print("\nYou entered number:", num)
    temp = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    print("Reversed number:", rev)

    if temp == rev:
        print("Result: Palindrome")
    else:
        print("Result: Not Palindrome")

palindrome(121)


# 2. Palindrome using for loop
def palindrome_for(num):
    print("\nYou entered number:", num)
    temp = num
    rev = 0

    count = 0
    t = num
    while t > 0:
        t = t // 10
        count += 1

    for i in range(count):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    print("Reversed number:", rev)

    if temp == rev:
        print("Result: Palindrome")
    else:
        print("Result: Not Palindrome")

palindrome_for(121)


# 3. Palindrome using string
def palindrome_str(s):
    print("\nYou entered string:", s)
    print("Reversed string:", s[::-1])

    if s == s[::-1]:
        print("Result: Palindrome String")
    else:
        print("Result: Not Palindrome")

palindrome_str("madam")



'''Reverse Using function'''

# 1. Using while loop
def reverse_num(num):
    print("\nYou entered number:", num)
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    print("Reversed number:", rev)

reverse_num(1234)


# 2. Using for loop
def reverse_num_for(num):
    print("\nYou entered number:", num)
    rev = 0

    count = 0
    temp = num
    while temp > 0:
        temp = temp // 10
        count += 1

    for i in range(count):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    print("Reversed number:", rev)

reverse_num_for(1234)


# 3. Using string
def reverse_str(s):
    print("\nYou entered string:", s)
    print("Reversed string:", s[::-1])

reverse_str("hello")



'''Prime Using function'''

# 1. Check Prime
def check_prime(num):
    print("\nYou entered number:", num)

    for i in range(2, num):
        if num % i == 0:
            print("Result: Not Prime")
            break
    else:
        if num > 1:
            print("Result: Prime Number")
        else:
            print("Result: Not Prime")

check_prime(7)


# 2. Prime Numbers from 1 to N
def p_prime(n):
    print("\nYou entered n =", n)
    print("Prime numbers are:")

    for num in range(2, n+1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end=" ")

p_prime(20)