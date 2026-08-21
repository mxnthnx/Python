x = "next piercing is gonna be a bullet through my skull"
a = " Blank space before and after quotes "

print("bullet" in x)

if "skull" in x:
    print("Yeah, he's gonna make it all worth it.")
    
if "kill" not in x:
    print("Kill is not in the sentence")

print(x[0:10]) #First character is counted as 0, +1 for empty space between words.
print(x[28:51]) #If you use '-', opposite shit...

print(x.upper())
print(x.lower())
print(a.strip())
print(x.replace("n","i"))
print(a.split(","))

c = x + " " + a
print(c)

#=================================

fuck = 69
shit = f"You're lucky, you got {fuck} backshots."
fucking = f"Nga got {fuck:.3f}" #":.3f" to add decimals
holy = f"Nga got shot {69*69} times"
print(shit)
print(fucking)
print(holy)

#==========================================
#Error Code
#text = "This is a "text"" 
text = "This is a \"text\"" 
print(text) #prints <"text">