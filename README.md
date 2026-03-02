
# List Output -->
Original List: [100, False, 100, 'Sai', 100, False, 10.6]
Length: 7
Type: <class 'list'>

After append('New'): [100, False, 100, 'Sai', 100, False, 10.6, 'New']
After insert(1, 'Insert'): [100, 'Insert', False, 100, 'Sai', 100, False, 10.6, 'New']
After remove(100): ['Insert', False, 100, 'Sai', 100, False, 10.6, 'New']
After pop(): ['Insert', False, 100, 'Sai', 100, False, 10.6]
Popped value: New
After pop(2): ['Insert', False, 'Sai', 100, False, 10.6]
Popped index value: 100
Count of 100: 1
Index of 'Sai': 2
After reverse(): [10.6, False, 100, 'Sai', False, 'Insert']
Sorted nums list: [1, 2, 5, 8]
After clear(): [] 




# 2nd Question Ans
v1 = i.pop(10)       # AttributeError: 'tuple' object has no attribute 'pop'
v2 = i.remove(100)    # AttributeError: 'tuple' object has no attribute 'remove'
