import re

# Open a file in read mode ('r')
file_path = "sample4"
file = open(file_path, "r")
# # Read the entire content of the file
# content = file.read()
# # Read the file line by line and save in lines
lines = []
for line in file:
    lines.append(line.strip())

total = 0
pairs = []
for num, row in enumerate(lines, 1):
    row = row.replace("  ", " 0")
    cards = row.split(":")
    cards = cards[1].strip().split(" | ")
    winner = cards[0].split(" ")

    having = cards[1].split(" ")
    win = set(winner)
    have = set(having)
    both = have.intersection(win)

    if len(both) > 0:
        total += pow(2, len(both) - 1)

    pairs.append({"card": num, "many": 1, "win": len(both)})

print("ALL PAIRS")
print(pairs)

for num, pair in enumerate(pairs):
    print("PAIR", pair)
    times = pair.get("win")
    print("VECES", times)
    times_ = times
    while times_ > 0:
        origin = pairs[num + times_].get("many")
        print("PARA CADA TIME", pairs[num + times_].get("many"))
        origin += pair["many"]
        print("NUEVO VALOR", origin)
        pairs[num + times_].update({"many": origin})
        times_ -= 1


print("NUEVO", pairs)

total_ = 0
for pair in pairs:
    total_ += pair["many"]
print(total_)
