name = "Aditya Rajendra Parakhi"   #String
print("===================================")
print("Total Length of String ->>", len(name))

# Python slicing stops before the end index

# 5 Positive + Positive Index
print("\n===================================\n")
print("Start Positive + End Positive ->>")
print("From 0 to 8: ", name[:8])  # Starts from index 0 (default) and goes up to index 8 (not included)
print("From 0 to 11: ", name[0:11])  # Starts from index 0 and goes up to index 11 (11 not included)
print("From 0: ", name[0:])  # Starts from index 0 and goes till the end of the string
print("From 6 to 20: ", name[6:20])  # Starts from index 6 and goes up to index 20
print("From 12 to 18: ", name[12:18]) # Starts from index 12 and goes up to index 18



# 5 Negative + Negative Index
print("\n===================================\n")
print("Start Negative + End Negative ->>")

print("From -20 to -17: ", name[-20:-17])  # Starts from -20 and goes up to -17
print("From -16 to -1: ", name[-16:-1])  # Starts from -16 and goes up to -1 (last character not included)
print("From -10 to -3: ", name[-10:-3])  # Starts from -10 and goes up to -3
print("From -8 to -2: ", name[-8:-2])  # Starts from -8 and goes up to -2
print("From -12: ", name[-12:])  # Starts from -12 and goes till the end of the string



# 5 Positive + Negative Index
print("\n===================================\n")
print("Start Positive + End Negative ->>")
# Start index = Positive
# End index = Negative

print("From 0 to -8: ", name[0:-8])  # Starts from index 0 and removes last 8 characters
print("From 2 to -10: ", name[2:-10])  # Starts from index 2 and stops 10 characters before end
print("From 5 to -7: ", name[5:-7])  # Starts from index 5 and stops 7 characters before end
print("From 8 to -3: ", name[8:-3])  # Starts from index 8 and stops 3 characters before end
print("From 12 to -1: ", name[12:-1])  # Starts from index 12 and stops 1 characters before end



# 5 Negative + Positive Index
print("\n===================================\n")
print("Start Negative + End Positive ->>")
# Start index = Negative
# End index = Positive

print("From -19 to 6: ", name[-19:6])  # Start 19 characters from end, stop at index 6
print("From -21 to 9: ", name[-21:9])  # Start 21 characters from end, stop at index 9
print("From -10 to 22: ", name[-10:22])  # Start 10 characters from end, stop at index 22
print("From -12 to 18: ", name[-12:18])  # Start 12 characters from end, stop at index 18
print("From -9 to 23: ", name[-9:23])  # Start 9 characters from end, stop at index 23




# 5 Positive (+ve) Step Size
print("\n===================================\n")
print("Positive Step Size [start : end : +step] ->>")

# name[start : end : +step]
# If step is positive → movement is left ➝ right
print("0 to 23 step 1: ", name[0:23:1])  # Starts at index 0, prints normally till index 22
print("1 to 20 step 3: ", name[1:20:3])  # Starts at index 1, jumps 3 characters each time
print("4 to 24 step 2: ", name[4:24:2])  # Starts at index 4, prints every 2nd character
print("3 to 21 step 4: ", name[3:21:4])  # Starts at index 3, jumps 4 positions each time
print("6 to 22 step 5: ", name[6:22:5])  # Starts at index 6, jumps 5 positions each time




print("\n===================================\n")
print("Negative Step Size [start : end : -step] ->>")

# name[start : end : -step]
# If step is negative → movement is right ➝ left
print("23 to last step -1: ", name[23::-1])  # Starts at index 23, moves backward one by one
print("23 to 0 step -2: ", name[23:0:-2])  # Starts at index 23, jumps 2 positions backward
print("20 to 5 step -3: ", name[20:5:-3])  # Starts at index 20, moves back 3 steps each time
print("18 to 2 step -2: ", name[18:2:-2])  # Starts at index 18, prints every 2nd character backward
print("15 to 1 step -4: ", name[15:1:-4])  # Starts at index 15, jumps 4 positions backward