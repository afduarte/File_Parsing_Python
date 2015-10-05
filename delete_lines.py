from sys import argv, stdout

file = argv[1]
find = argv[2]

f = open(file,"r")
lines = f.readlines()
f.close()

n = open(file+".new","w")

for line in open(file):
    if find not in line:
        n.write(line)

n.close()
print("Deleted every line that contained "+find)
