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
print("=" * 50)
print("=" * 50)




# Class 4

class Frame:

    def __init__(self, f_n, f_w, f_h):
        self.type = f_n
        self.width = f_w
        self.height = f_h

    def display_data(self):
        print("\tFrame Name:", self.type)
        print("\tWidth:", self.width)
        print("\tHeight:", self.height)

    def area(self):
        print("\tArea of Frame is: " ,self.width * self.height, "sq.ft")


f1 = Frame("Nature Frame", 200, 100)
f2 = Frame("Dog Frame" , 100 , 100)
f3 = Frame("Bike" , 300 , 250)

print("Object 1= ")
f1.display_data()
f1.area()
print("=" * 50)
print("Object 2= ")
f2.display_data()
f2.area()
print("=" * 50)
print("Object 3= ")
f3.display_data()
f3.area()
print("=" * 50)
print("=" * 50)




# Class 5

class Dog:

    def __init__(self, d_n, d_b, d_a, d_g):
        self.name = d_n
        self.breed = d_b
        self.age = d_a
        self.gender = d_g


    def display_data(self):
        print("\tDog Name:", self.name)
        print("\tBreed:", self.breed)
        print("\tAge:", self.age)
        print("\tGender:", self.gender)


    def eat(self):
        pass


d1 = Dog("Tommy", "Labrador", 3 , "Male")
d2 = Dog("Maya" , "Dalmension" , 2.7 , "Female")
d3 = Dog("Street Dog", "Karvani" , 1 , "Male")

print("Object 1=")
d1.display_data()
print("=" * 50)
print("Object 2=")
d2.display_data()
print("=" * 50)
print("Object 3=")
d3.display_data()
print("=" * 50)
print("=" * 50)





# Task 3

# Player Class
class Player:
    def __init__(self, j_no, p_na, to_ru, to_wi, c_na):
        self.jersey_no = j_no
        self.player_name = p_na
        self.total_runs = to_ru
        self.total_wickets = to_wi
        self.country_name = c_na

    def display(self):
        print("\tJersey No:", self.jersey_no)
        print("\tPlayer Name:", self.player_name)
        print("\tTotal Runs:", self.total_runs)
        print("\tTotal Wickets:", self.total_wickets)
        print("\tCountry:", self.country_name)
        print("--" *20)

# MI Team
MI_team = []

# Object creation
p1 = Player(45, "Rohit Sharma", 6500, 15, "India")
p2 = Player(63, "Suryakumar Yadav", 3500, 0, "India")
p3 = Player(9, "Tilak Varma", 1000, 0, "India")
p4 = Player(17, "Danish Malewar", 0, 0, "India")
p5 = Player(12, "Quinton de Kock", 3200, 0, "South Africa")
p6 = Player(44, "Ryan Rickelton", 0, 0, "South Africa")
p7 = Player(0, "Robin Minz", 0, 0, "India")
p8 = Player(33, "Hardik Pandya", 2500, 60, "India")
p9 = Player(0, "Mitchell Santner", 500, 30, "New Zealand")
p10 = Player(0, "Will Jacks", 500, 10, "England")
p11 = Player(0, "Naman Dhir", 0, 0, "India")
p12 = Player(8, "Raj Angad Bawa", 0, 0, "India")
p13 = Player(0, "Corbin Bosch", 0, 0, "South Africa")
p14 = Player(96, "Atharva Ankolekar", 0, 0, "India")
p15 = Player(0, "Shardul Thakur", 300, 90, "India")
p16 = Player(93, "Jasprit Bumrah", 60, 150, "India")
p17 = Player(18, "Trent Boult", 200, 110, "New Zealand")
p18 = Player(56, "Deepak Chahar", 100, 70, "India")
p19 = Player(11, "Mayank Markande", 50, 35, "India")
p20 = Player(23, "Raghu Sharma", 0, 0, "India")
p21 = Player(70, "Allah Ghazanfar", 0, 0, "Afghanistan")
p22 = Player(42, "Ashwani Kumar", 0, 0, "India")
p23 = Player(25, "Mohammed Izhar", 0, 0, "India")


# add all referance variable inside one list
players = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,
           p16,p17,p18,p19,p20,p21,p22,p23]


for p in players:
    MI_team.append(p)

print("\n\nTask 3 =")

for p in MI_team:
    p.display()