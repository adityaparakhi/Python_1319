class Student:
    def __init__(self,n,r):
        self.name = n
        self.rollNo = r

    # Magic Method    # Overloading
    def __add__(self, other):
        return self.name + other.name
    
    def __sub__(self, other):
        return self.rollNo - other.rollNo
    
    def __mul__(self, other):
        return self.rollNo * other.rollNo
    
    def __truediv__(self, other):
        return self.rollNo / other.rollNo

    def __floordiv__(self, other):
        return self.rollNo // other.rollNo

    def __pow__(self, other):
        return self.rollNo ** other.rollNo


# Object Creation
s1 = Student("Vaibhav", 5)
s2 = Student("Aditya", 3)

print("Addition: ", s1 + s2)
print("Subtraction: ", s1 - s2)
print("Multiplication: ", s1 * s2)
print("Division: ", s1 / s2)
print("Floor Division: ", s1 // s2)
print("Power value: ", s1 ** s2)