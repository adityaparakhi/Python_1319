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

lst = []

lst.append(100)      # add element inside list
lst.append(False)
lst.append(100)
lst.append("Sai")
lst.append(100)
lst.append(False)
lst.append(10.6)

print(lst)
print("Length of list:", len(lst))
print(type(lst))





# # Q2. Home Work check the method works 
# i = (10, 20, 30)

# v1 = i.pop(10)       # AttributeError: 'tuple' object has no attribute 'pop'

# v2 = i.remove(100)    # AttributeError: 'tuple' object has no attribute 'remove'




# # Proper way
# v1 = i.pop(1)     # removes element at index 1
# print(v1)         # 20

# i.remove(10)      # removes value 10
# print(i)          # [30]