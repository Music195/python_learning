dogs = ["Beagle", "Bulldog", "Poodle", "Labrador", "Golden Retriever"] # can contain any type of data
print(dogs)  # Print the list of dogs
print(dogs[0])  # Print the first dog in the list

print("Windows" in dogs)  # Check if "Windows" is in the list of dogs

#dogs = [] # Reinitialize the list of dogs
dogs[2] = "Windows"  # Change the third dog in the list to "Windows"
print(dogs)  # Print the updated list of dogs
print(dogs[-1])  # Print the last dog in the list
print(dogs[-2])  # Print the second to last dog in the list
print(dogs[1:3])  # Print a slice of the list from index 1 to 2 (inclusive)
print(dogs[1:])  # Print a slice of the list from index 1 to the end
print(dogs)  # Print the entire list of dogs
dogs.append("Haskey")  # Add "Haskey" to the end of the list
print(dogs)  # Print the updated list of dogs
dogs.insert(2, "Empire")  # Insert "Windows" at index 2 in the list
print(dogs)  # Print the updated list of dogs
dogs.remove("Empire")  # Remove "Empire" from the list 
print(dogs)  # Print the updated list of dogs
dogs.extend (["Judah", 4]) #add the other list to the main list 
print (dogs) #Print the updated list of dogs
dogs += ["Alpha", 5] #add the other list to the main list
print (dogs) #Print the updated list of dogs
print(dogs.pop()) #remove the last element in the list and print it
print (dogs) #Print the updated list of dogs
print(dogs.pop(2)) #remove the third element in the list and print it
print (dogs) #Print the updated list of dogs
dogs.pop() #remove the last element in the list
print (dogs) #Print the updated list of dogs
dogs.insert(2, "Empire") #insert "Empire" at index 2 in the list
print (dogs) #Print the updated list of dogs
dogs[1:1] = ["Test1", "Test2"] #insert "Test1" and "Test2" at index 1 in the list
print (dogs) #Print the updated list of dogs
dogs[1:3] = ["Test3", "Test4"] #replace the elements at index 1 and 2 with "Test3" and "Test4"
print (dogs) #Print the updated list of dogs
dogs[2:5] = ["Test5"] #replace the elements at index 2 to 4 with "Test5"
print (dogs) #Print the updated list of dogs
print("------------------------------") #Print a separator line
print(dogs.pop()) #remove the last element in the list and print it ---#4
print (dogs) #Print the updated list of dogs
dogs.sort() #sort the list in ascending order
print (dogs) #Print the updated list of dogs
dogs.insert(2 , "barry") #insert "barry" at index 2 in the list
print (dogs) #Print the updated list of dogs
dogs.sort() #sort the list in ascending order
print (dogs) #Print the updated list of dogs
dogs.sort(key=str.lower) #sort the list in ascending order ignoring case
print (dogs) #Print the updated list of dogs
print("-----------------------------") #Print a separator line
dogsCopy = dogs[:] #create a copy of the list of dogs
print (dogsCopy) #Print the copy of the list of dogs
print ("----------------------------") #Print a separator line
print (dogsCopy is dogs) #Check if the copy of the list is the same as the original list
print (dogsCopy == dogs) #Check if the copy of the list is equal to the original list
print (dogs) #Print the original list of dogs
dogs = ["Beagle", "Bulldog", "Poodle", "Labrador", "Golden Retriever"] # can contain any type of data
print (sorted (dogs,key=str.lower)) #Print the sorted list of dogs in ascending order ignoring case without modifying the original list
print (dogs) #Print the original list of dogs
# dogs.clear() #clear the list
# print (dogs) #Print the updated list of dogs
