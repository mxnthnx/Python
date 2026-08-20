#Basic

x = "Nga"

def myfunc():
    print("This is " + x)
    
myfunc()

#Assigning variable inside a function, with the same name as the global variable

y = "Freak"

def myfunc():
    y = "Chewwks"
    print("This is " + y)
    
myfunc()

print("I'm a " + y)