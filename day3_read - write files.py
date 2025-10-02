f = open("notes.txt", "w")
f.write("Today I started learning Python.\n")
f.close()

f = open("notes.txt", "r")
print(f.read())
f.close()