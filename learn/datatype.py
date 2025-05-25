# class myclass():
#   def __len__(self):
#     return 0

# myobj = myclass()
# print(bool(myobj))

# class MyCollection:
#     def __init__(self, items):
#         self.items = items  # Store a list of items

#     def __len__(self):
#         return len(self.items)  # Return the length of the items list

# # Create an instance of MyCollection
# collection = MyCollection([1, 2, 3])
# print(collection.items)  # Output: [1, 2, 3]

# # Call len() on the object
# print(len(collection))  # Output: 3

# # Check the truthiness of the object
# print(bool(collection))  # Output: True

# print(collection)


# collection1 = MyCollection([1, 2, 3])
# collection2 = MyCollection([4, 5, 6])
# print(collection1.items)  # Output: [1, 2, 3]
# print(collection2.items)  # Output: [4, 5, 6]

# thisTuple = (1, 2, 2, 3)
# print(thisTuple.count(2))  #   

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# tri_recursion(6)


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# class Person:
#     name = "John"
#     age = 36


# p1 = Person()
# print(p1.name)

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))