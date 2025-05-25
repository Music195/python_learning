dog = { "name": "Roger", "age": 5, "breed": "bulldog" } # create a dictionary with dog information
print(dog["name"]) # print the name of the dog // Roger
print(dog['age']) # print the age of the dog // 5
print(dog['breed']) # print the breed of the dog // bulldog
dog["name"] = "Syd" # change the name of the dog to "Syd"
print(dog["name"]) # print the updated name of the dog // Syd
print (dog.get("name")) # get the age of the dog // Syd
print (dog.get("color")) # get the color of the dog // None
print (dog.get("color", "black")) # get the color of the dog with default value // black
print (dog.pop("name")) # remove the name of the dog and print it // Syd
print (dog) # print the updated dog dictionary // {'age': 5, 'breed': 'bulldog'} 
print (dog.popitem()) # remove the last item in the dictionary and print it // ('breed', 'bulldog')
print (dog) # print the updated dog dictionary // {'age': 5}  
print ( "age" in dog) # check if "age" is in the dictionary // True
print ( "breed" in dog) # check if "breed" is in the dictionary // False
print (dog.keys()) # print the keys of the dictionary // dict_keys(['age'])
dog = { "name": "Roger", "age": 5, "breed": "bulldog" } # create a dictionary with dog information
print (dog.keys()) # print the keys of the dictionary // dict_keys(['name', 'age', 'breed'])
print (list (dog.keys())) # print the keys of the dictionary as a list // ['name', 'age', 'breed']
print (dog.values()) # print the values of the dictionary // dict_values(['Roger', 5, 'bulldog'])
print (list (dog.values())) # print the values of the dictionary as a list // ['Roger', 5, 'bulldog']
print (dog.items()) # print the items of the dictionary // dict_items([('name', 'Roger'), ('age', 5), ('breed', 'bulldog')])
print (list (dog.items())) # print the items of the dictionary as a list // [('name', 'Roger'), ('age', 5), ('breed', 'bulldog')]
print (len(dog)) # print the length of the dictionary // 3
dog["favorite_food"] = "chicken" # add a new key-value pair to the dictionary
print (dog) # print the updated dog dictionary // {'name': 'Roger', 'age': 5, 'breed': 'bulldog', 'favorite_food': 'chicken'}
del dog["favorite_food"] # delete the key-value pair from the dictionary
print (dog) # print the updated dog dictionary // {'name': 'Roger', 'age': 5, 'breed': 'bulldog'}
dogCopy = dog.copy() # create a copy of the dictionary
print (dogCopy) # print the copy of the dog dictionary // {'name': 'Roger', 'age': 5, 'breed': 'bulldog'}

