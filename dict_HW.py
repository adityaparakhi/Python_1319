'''
level 1
    create dict of 2025 movies

    movies_db = {}     #min 4 movies

    cast_dhur = ["Ranveer Singh", "Akshay Datt", "Sara Arjun"]

    movies_db["Dhurandar"] = cast_dhur



    print-->
    keys()
    values()
    items()

    count cast working in how many movies count and movie names

'''


# Empty dictionary
movies_db = {}


# Cast of 2025 movies

cast_Kesari_Chapter_2 = ["Akshay Kumar", "R. Madhavan", "Ananya Panday"]

cast_raid2 = ["Ajay Devgn", "Vaani Kapoor", "Riteish Deshmukh"]

cast_son_of_sardaar_2 = ["Ajay Devgn", "Mrunal Thakur", "Sanjay Dutt"]

cast_housefull_5 = ["Akshay Kumar", "Riteish Deshmukh", "Abhishek Bachchan", "Jacqueline Fernandez", "Sonam Bajwa"]

cast_sunny_sanskari = ["Varun Dhawan", "Janhvi Kapoor", "Sanya Malhotra", "Rohit Saraf"]

cast_param_sundari = ["Sidharth Malhotra", "Janhvi Kapoor"]

cast_baaghi_4 = ["Tiger Shroff", "Sanjay Dutt"]



# Insert cast and movie names inside Dictionary
movies_db["Kesari Chapter 2"] = cast_Kesari_Chapter_2
movies_db["Raid 2"] = cast_raid2
movies_db["Son of Sardaar 2"] = cast_son_of_sardaar_2
movies_db["Housefull 5"] = cast_housefull_5
movies_db["Sunny Sanskari Ki Tulsi Kumari"] = cast_sunny_sanskari
movies_db["Param Sundari"] = cast_param_sundari
movies_db["Baaghi 4"] = cast_baaghi_4      



# Print full Dictionary
print("Total data of 2025 released movies with its cast is --->\n", movies_db)
print("\n===================================================================================================\n")

# 1. Print all keys using keys() method from dictionary
print("All Keys form the Dictionary ---->")
for m in movies_db.keys():
    print(m)
print("\n===================================================================================================\n")



# 2. Print all values using values() method from dictionary
print("All values form the Dictionary ---->")
for v in movies_db.values():
    print(v)
print("\n===================================================================================================\n")


# 3. Print all keys and values using items() method form dictionary
print("All keys and values form the Dictionary ---->") 
for m, v in movies_db.items():
    print(m, "------>", v)
print("\n===================================================================================================\n")



# 4. Counting the cast working in how many movies and also in which movie
cast = input("Enter the Actor/Actress name: ")
count = 0

print(f"Movies of {cast} is: ")
for m in movies_db:
    
    if cast in movies_db.get(m):
        print(m)                #Printing the movie names where cast is worked
        count += 1

print(f"{cast} worked in {count} movie.")