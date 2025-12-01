dial = 50
total = 0
with open("./input.txt", "r") as fp:
    for line in fp.readlines():
        rotation = line.replace("R", "").replace("L", "-")
        dial = (dial + int(rotation)) % 100
        if (dial == 0):
            total += 1
print(total)