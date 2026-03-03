# String using range function
print("================================\n")
s1 = "Hello Python"
# range function in forward direction
print("String in Forward Direction ---->")
for i in range(len(s1)):
    print(s1[i])


# range function in reverse direction
print("-----------------------------------")
print("String in Reverse Direcion ---->")
for i in range(len(s1)-1, -1, -1):
    print(s1[i])




# List using range function
print("\n===============================\n")
l1 = [11,12,13,14,15,16,17,18,19,20]
# range function in forward direction
print("List in Forward Direction ---->")
for i in range(len(l1)):
    print(l1[i])      


# range function in reverse direction
print("-----------------------------------")
print("List in Reverse Direction ---->")
for i in range(len(l1)-1,-1,-1):
    print(l1[i])




# Tuple using range function
print("\n================================\n")
t1 = (1,2,3,4,5,6)
# range function in forward direction
print("Tuple in Forward Direction ---->")
for i in range(len(t1)):
    print(t1[i])

 
# range function in reverse direction
print("-----------------------------------")
print("Tuple in Reverse Direction ---->")
for i in range(len(t1)-1,-1,-1):
    print(t1[i])