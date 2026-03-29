'''
    List Comprehension
        l1 = [1,2]
        l2 = ["a", "b"]

        out_put = [(1, "a"), (1,"b"), (2, "a"), (2, "b")]
'''

# 1st way (Using normal loop)
l1 = [1, 2]
l2 = ["a", "b"]

res1 = []

for i in l1:
    for j in l2:
        res1.append((i, j)) 

print("Original List 1: ", l1)
print("Original List 2: ", l2)

print("\nOutput using normal loop:", res1)



# 2nd way (List Comprehension)
l1 = [1, 2]
l2 = ["a", "b"]

res2 = [(i, j) for i in l1 for j in l2]    # List Comprehension

print("Original List 1: ", l1)
print("Original List 2: ", l2)
print("\nOutput using list comprehension:", res2)




# Set Comprehension
l1 = [1, 2]
l2 = ["a", "b"]

res3 = {(i, j) for i in l1 for j in l2}     # Set Comprehension

print("Original List 1: ", l1)
print("Original List 2: ", l2)
print("\nOutput using set comprehension:", res3)