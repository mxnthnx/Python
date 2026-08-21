x = 70
y = 69
z = 70

print( x > y) #Prints True or False
print(x == z) #Prints True or False

#=========================================

a = 100
b = 99

if b > a:
    print(f"{b} is greate than {a}.")
else: 
    print(f"{b} is smaller than {a}")
    
#=========================================

def myDih():
    return True

if myDih():
    print("YES!")
else:
    print("NO!")
    
#=========================================

c = "Hello"

i = isinstance(c, str)

print("It's a string")

#OR

d = "Cake"

if(isinstance(d, str)):
    print("It's a cake")
else:
    print("NGA")
