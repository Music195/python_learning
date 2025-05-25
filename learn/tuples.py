name = ("Roger", "Syd", "Syd", "Roger", "Roger") #Create a tuple with 5 elements
print (name[0]) #Print the first element in the tuple 
# print (name[1]) #Print the second element in the tuple # Roger
print(name.index("Roger")) #Print the index of "Roger" in the tuple #0

print(len(name)) #Print the length of the tuple #2
print(name.count("Roger")) #Print the count of "Roger" in the tuple #3
print("Roger" in name) #Check if "Roger" is in the tuple #True
print(name[0:2]) #Print the first two elements in the tuple #("Roger", "Syd")
print(sorted(name)) #Print the sorted tuple #("Roger", "Roger", "Roger", "Syd", "Syd")
newName = name + ("Tina", "Queen") #Create a new tuple by concatenating the original tuple with another tuple
print(newName) #Print the new tuple #("Roger", "Syd", "Syd", "Roger", "Roger", "Tina", "Queen")
#newName.insert(2, "Empire") #Tuples are immutable, so this will raise an error
