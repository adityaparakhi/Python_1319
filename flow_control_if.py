'''
HW ->You have one list of students marks.
    create two sub list for even and odd marks students
'''

stud_marks = [100,67,87,78,79,74,59,66,73,82,99,68,45,38]
even_marks = []
odd_marks = []

for i in stud_marks:
    if i % 2 == 0:
        even_marks.append(i)
    else:
        odd_marks.append(i)

print("Original Marks:", stud_marks)
print("Even Marks:", even_marks)
print("Odd Marks:", odd_marks)
