def a():
    print("a() called")
    b()
    d()
    print("a() finished")

def b():
    print("b() called")
    c()
    print("b() finished")

def c():
    print("c() called")
    print("c() finished")
    
def d():
    print("d() called")
    print("d() finished")

a()
print("Program finished")
# Output:
# a() called
# b() called
# c() called
# c() finished
# b() finished
# a() finished
# Program finished