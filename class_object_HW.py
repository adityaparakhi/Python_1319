# Task 2 (Create 5 classes with 2 attributes and 1 method)

# Class 1

class Bottle:

    def __init__(self, b_co, b_ca):       
        self.color = b_co
        self.capacity = b_ca

    def water_capacity(self):
        print("Water level is:", self.capacity, "ml")

# create object using referance variable
b1 = Bottle("Silver", 9.5)
b2 = Bottle("Red", 9)

print("Class Bottle ->")
print("Object 1 =")
print("\tBottle Color: " , b1.color , "\n\tBottle Capacity: " , b1.capacity, "ml")
print("=" * 50)
print("Object 2 =")
print("\tBottle Color: " , b2.color , "\n\tBottle Capacity: " , b2.capacity, "ml")
print("=" * 50)
print("Display Methods :-")
# calling methods 
b1.water_capacity()
b2.water_capacity()
print("=" * 50)
print("=" * 50)



# Class 2

class Door:

    def __init__(self, d_t, d_c, d_h):
        self.door_type = d_t
        self.door_color = d_c
        self.door_height = d_h

    def open_close(self):
        pass

d1 = Door("wooden", "Brown", 7.5)
d2 = Door("Iron", "silver", 7)
d3 = Door("Fiber", "Black White Mix", 8)

print("Class Door ->")
print("Object 1 =")
print("\tDoor Type: " , d1.door_type , "\n\tDoor Color: " , d1.door_color, "\n\tDoor Height: " , d1.door_height)
print("=" * 50)
print("Object 2 =")
print("\tDoor Type: " , d2.door_type , "\n\tDoor Color: " , d2.door_color, "\n\tDoor Height: " , d2.door_height)
print("=" * 50)
print("Object 3 =")
print("\tDoor Type: " , d3.door_type , "\n\tDoor Color: " , d3.door_color, "\n\tDoor Height: " , d3.door_height)
print("=" * 50)
print("=" * 50)


# Class 3 

class Light:

    def __init__(self, co, wat, br):
        self.color = co
        self.wattage = wat
        self.brand = br
    
    def on_off(self):
        pass

    def check_wattage(self):
        print("The wattage of light is ", self.wattage, "Wt.")


l1 = Light("Off White", 20 , "PHILIPS")
l2 = Light("Yellow", 25 , "SYSKA" )
l3 = Light("White" , 10 , "HAVELLS")


print("Class Light ->")
print("Object 1 =")
print("\tLight Color: " , l1.color , "\n\tLight Wattage: " , l1.wattage , "\n\tLight Brand: " , l1.brand)
print("=" * 50)
print("Object 2 =")
print("\tLight Color: " , l2.color , "\n\tLight Wattage: " , l2.wattage , "\n\tLight Brand: " , l2.brand)
print("=" * 50)
print("Object 3 =")
print("\tLight Color: " , l3.color , "\n\tLight Wattage: " , l3.wattage , "\n\tLight Brand: " , l3.brand)