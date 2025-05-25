#Sets 
names = {"John", "Jane", "Jack", "Jill", "Joe"}
names2 = {  "Jack"}

intersetion = names & names2 #Find the intersection of two sets
print(intersetion) #Print the intersection of two sets #{"Jack"}
mod = names | names2 #Find the union of two sets
print(mod) #Print the union of two sets #{"John", "Jane", "Jack", "Jill", "Joe"}
mod = names - names2 #Find the difference of two sets
print(mod) #Print the difference of two sets #{"John", "Jane", "Jill", "Joe"}
mod = names > names2 #Find the symmetric difference of two sets
print(mod) #Print the symmetric difference of two sets #True
mod = names < names2 #Find the symmetric difference of two sets
print(mod) #Print the symmetric difference of two sets #False}
print (list(names)) #Convert the set to a list and print it #["John", "Jane", "Jack", "Jill", "Joe"]
set1 = {"John", "Jane", "Jack", "Jill", "Joe", "Jack"}  #Create a set with duplicate elements but only one will be stored
print(set1) #Print the set #{"John", "Jane", "Jack", "Jill", "Joe"}
