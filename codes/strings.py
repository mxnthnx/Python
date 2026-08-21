x = "next piercing is gonna be a bullet through my skull"

print("bullet" in x)

if "skull" in x:
    print("Yeah, he's gonna make it all worth it.")
    
if "kill" not in x:
    print("Kill is not in the sentence")

print(x[0:10]) #First character is counted as 0, +1 for empty space between words.
print(x[28:51])