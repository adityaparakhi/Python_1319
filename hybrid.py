# Base Class
class A:
    def m1(self):
        prop1 = ["House" , "Cash"]
        print(prop1)

    def m2(self):
        prop2 = ["Cash" , "Car" , "Farm"]
        print(prop2)


# Hierarchical Inheritance
class B(A):
    def m1(self):
        prop3 = ["Cash" , "Car" , "House" , "Farm"]
        print(prop3)

    def m3(self):
        prop4 = ["Car" , "Bike" , "Gold"]
        print(prop4)


class C(A):
    def m1(self):
        prop5 = ["Cash" , "House"]
        print(prop5)

    def m4(self):
        prop6 = ["Cash" , "Car" , "House" , "Farm"]
        print(prop6)


class D():
    def m1(self):
        prop7 = ["Car" , "Bike" , "Gold"]
        print(prop7)

    def m5(self):
        prop8 = ["Cash" , "House"]
        print(prop8)


# Multilevel
class E(B):
    def m1(self):
        prop9 = ["Car" , "Bike" , "Gold"]
        print(prop9)

    def m6(self):
        prop10 = ["Cash" , "Car" , "Farm"]
        print(prop10)


class G(E):
    def m1(self):
        prop11 = ["Cash" , "Car" , "House" , "Farm"]
        print(prop11)

    def m7(self):
        prop12 = ["Cash" , "Bike"]
        print(prop12)


# Multiple Inheritance (Hybrid)
class F(C, D):
    def m1(self):
        prop13 = ["Car" , "Farm"]
        print(prop13)

    def m8(self):
        prop14 = ["Cash" , "Bike"]
        print(prop14)


# Object for G
print("Access the G class elements ->")
jay = G()

# Calling Methods
jay.m1()
jay.m2()
jay.m3()
jay.m6()
jay.m7()



# Object for F
print("\nAccess the F class elements ->")
viru = F()

# Calling Methods
viru.m1()
viru.m2()
viru.m4()
viru.m5()
viru.m8()


# MRO
print("\n---- MRO ----")
print("A:", A.__mro__)
print("B:", B.__mro__)
print("C:", C.__mro__)
print("D:", D.__mro__)
print("E:", E.__mro__)
print("F:", F.__mro__)
print("G:", G.__mro__)