import re

# Open a file in read mode ('r')
file_path = "input2"
file = open(file_path, "r")
# # Read the entire content of the file
# content = file.read()
# # Read the file line by line and save in lines
lines = []
for line in file:
    lines.append(line.rstrip())

games = {}
for line in lines:
    game = line.rsplit(":")
    num = re.findall("\d+", game[0])[0]
    sets = game[1].rsplit(";")
    sets_ = []
    for set_ in sets:
        colors = set_.rsplit(",")
        sett_ = {}
        for color in colors:
            build = color.split(" ")
            sett_.update({build[2]: int(build[1])})
        sets_.append(sett_)
    games.update({int(num): sets_})

# Valid
valid = {"red": 12, "green": 13, "blue": 14}

true = []
false = []
for game, sets in games.items():
    true.append(game)
    for sett in sets:
        for x, y in valid.items():
            if sett.get(x) and sett.get(x) > y:
                false.append(game)

valid_games = set(true) - set(false)

total = 0
for game, sets in games.items():
    high = 1
    for x in valid.keys():
        numbers = []
        for sett in sets:
            if x in sett.keys():
                numbers.append(sett.get(x))
        high *= max(numbers)
    total += high
print(total)
