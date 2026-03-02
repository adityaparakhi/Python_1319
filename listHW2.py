# st = set()

# st.add(100)      #add element inside set
# st.add(False)
# st.add(100)
# st.add("Sai")
# st.add(100)
# st.add(False)
# st.add(10.6)

# print(st)
# print("Length of set: ",len(st))
# print(type(st))



# Q1.exact same check for list is Home Work

# Create list
lst = []

lst.append(100)
lst.append(False)
lst.append(100)
lst.append("Sai")
lst.append(100)
lst.append(False)
lst.append(10.6)

print("Original List:", lst)
print("Length:", len(lst))
print("Type:", type(lst))


# append()
lst.append("New")
print("\nAfter append('New'):", lst)


# insert()
lst.insert(1, "Insert")
print("After insert(1, 'Insert'):", lst)


# remove()
lst.remove(100)   # removes first occurrence
print("After remove(100):", lst)


# pop()
removed_value = lst.pop()   # removes last element
print("After pop():", lst)
print("Popped value:", removed_value)

removed_index = lst.pop(2)  # removes element at index 2
print("After pop(2):", lst)
print("Popped index value:", removed_index)


# count()
print("Count of 100:", lst.count(100))


# index()
print("Index of 'Sai':", lst.index("Sai"))


# reverse()
lst.reverse()
print("After reverse():", lst)


# sort() (separate numeric list)
nums = [5, 2, 8, 1]
nums.sort()
print("Sorted nums list:", nums)


# clear()
lst.clear()
print("After clear():", lst)





# # Q2. Home Work check the method works 
# i = (10, 20, 30)

# v1 = i.pop(10)       # AttributeError: 'tuple' object has no attribute 'pop'

# v2 = i.remove(100)    # AttributeError: 'tuple' object has no attribute 'remove'




# # Proper way
# v1 = i.pop(1)     # removes element at index 1
# print(v1)         # 20

# i.remove(10)      # removes value 10
# print(i)          # [30]