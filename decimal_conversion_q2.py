'''
Accept binary, octal, hexadecimal from user and convert 
it into decimal number and display on screen/terminal/console

For Ex->> 
input1 = 0b0110
input2 = 2
'''

number = input("Enter number in binary, octal, or hexadecimal format: ")  # This number can be in binary, octal or hexadecimal numbers

base = int(input("Enter the base (2 = binary, 8 = octal, 16 = hexadecimal): "))  # Accept base of the number 

decimal_value = int(number, base)  # Converting the number into decimal form

print("=================================")
print("Decimal form of Input Number is ", decimal_value)   # Display result
print("=================================")

