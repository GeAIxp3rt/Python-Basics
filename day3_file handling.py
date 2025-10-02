f = open("training.txt", "w")
f.write("Football: 4 hours\n")
f.write("Music: 4 hours\n")
f.close()

f = open("training.txt", "r")
print("Training schedule:\n", f.read())
f.close()