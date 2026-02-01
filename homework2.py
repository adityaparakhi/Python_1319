# Create Following table structure using string formatting in python

# <	= Left align
# >	= Right align
# ^	= Center align 



# Printing the table using string formatting using .format method

print("Using .format")
print("----------------------------")
print("| {:^7}| {:^7}| {:^7}|".format("Roll", "Name", "Marks"))
print("----------------------------")
print("| {:^7}| {:^7}| {:^7}|".format(1, "Jay", 88))
print("----------------------------")
print("| {:^7}| {:^7}| {:^7}|".format(2, "Niru", 77))
print("----------------------------")
print(" ")



# Printing the table using string formatting using f" " method

print("Using f'' ")
print("----------------------------")
print(f"| {'Roll':^7}| {'Name':^7}| {'Marks':^7}|")
print("----------------------------")
print(f"| {1:^7}| {'Jay':^7}| {88:^7}|")
print("----------------------------")
print(f"| {2:^7}| {'Niru':^7}| {77:^7}|")
print("----------------------------")