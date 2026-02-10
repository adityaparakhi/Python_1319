'''
Accept decimal no from console/terminal and convert that into
binary, octal,hexadecimal number system and display back on terminal again.
'''


num = int(input("Enter the Number: "))   #Accepting Decimal Number from User on Console

# Converting that number into Binary
binary_form = bin(num)   # Converts into binary number
print("Binary form of Input Number is ", binary_form)  # Display Binary number in Console
print("=================================")

# Converting that number into Octal
octal_form = oct(num)  # Converts into Octal number
print("Octal form of Input Number is ", octal_form)  # Display Octal number in Console
print("=================================")

# Converting that number into Octal
hexa_form = hex(num)  # Converts into Octal number
print("Hexadecimal form of Input Number is ", hexa_form)  # Display Hexaecimal number in Console
print("==================================")