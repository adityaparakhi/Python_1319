'''All ways'''

# 1st way Basic Method (Most Common)
num = int(input("Enter a number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")



# 2nd way Efficient Method (Check till n-1)
num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print("Not a Prime Number")
        break
else:
    print("Prime Number")



# 3rd way Better Method (Check till n//2)
num = int(input("Enter a number: "))

for i in range(2, num//2 + 1):
    if num % i == 0:
        print("Not a Prime Number")
        break
else:
    print("Prime Number")



# 4th way Best Method (Square root)
num = int(input("Enter a number: "))

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print("Not a Prime Number")
        break
else:
    if num > 1:
        print("Prime Number")
    else:
        print("Not a Prime Number")

