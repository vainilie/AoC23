import re

# Open a file in read mode ('r')
file_path = "input3"
file = open(file_path, "r")
# # Read the entire content of the file
# content = file.read()
# # Read the file line by line and save in lines
lines = []
lenght = 0

for line in file:
    lenght = len(line)
    lines.append("." + line.strip() + ".")
    # lines.append(line.strip())
new_line = str("." * lenght + "." + ".")

lines.insert(0, new_line)
lines.append(new_line)
numbers = []
coords = []
for num, line in enumerate(lines):
    numbers.append(re.findall("\d+", line))
    set_ = re.findall("\d+", line)
    print(set_)
    otrora = []
    for number in set_:
        if set_.count(number) == 1:
            coo = re.search(rf"\b{number}\b", line).span()
            coords.append(
                {
                    "line": int(num),
                    "num": int(number),
                    "coor": re.search(number, line).span(),
                    "coo0": coo[0] - 1,
                    "coo1": coo[1] + 1,
                }
            )
        else:
            if set_.count(number) > 1:
                if number not in otrora:
                    repetitions = set_.count(number)
                    print("rep", repetitions)
                    start = 0
                    while repetitions != 0:
                        otrora.append(number)
                        coo = ()
                        print("rep", repetitions)
                        print("start", start)
                        print(line[start:])
                        print(number)
                        coo = re.search(rf"\b{number}\b", line[start:-1]).span()
                        print(coo)
                        print(start)
                        repetitions -= 1
                        coords.append(
                            {
                                "line": int(num),
                                "num": int(number),
                                "coor": (coo[0] + start, coo[1] + start),
                                "coo0": coo[0] + start - 1,
                                "coo1": coo[1] + start + 1,
                            }
                        )
                        start = +(coo[1] + start)
print(coords)
symbol = []


def check(line, start, end, num, total, lines):
    tottal = total - 1
    if re.search("[^\d.]", lines[line][start:end]):
        symbol.append(num)
    else:
        #        if line != 0 and re.search("[^\d.]", lines[line - 1][start:end]):
        if re.search("[^\d.]", lines[line - 1][start:end]):
            symbol.append(num)
        else:
            # if line != len(lines):
            if re.search("[^\d.]", lines[line + 1][start:end]):
                symbol.append(num)


def check2(line, start, end, num, total, lines):
    asterisk = []
    tottal = total - 1
    inline = re.findall("\*", lines[line][start:end])
    if len(inline) > 0:
        repetitions = len(inline)
        while repetitions != 0:
            asteriska = []
            symbol.append(num)
            koordinate = re.search("\*", lines[line][start:end]).span()
            asteriska.append(line)
            asteriska.append(start + koordinate[0])
            asteriska.append(start + koordinate[1])
            repetitions -= 1
            start = start + koordinate[0]
            asterisk.append(asteriska)
        return asterisk
    else:
        upperline = re.findall("\*", lines[line - 1][start:end])
        if len(upperline) > 0:
            repetitions = len(upperline)
            while repetitions != 0:
                asteriska = []
                symbol.append(num)
                koordinate = re.search("\*", lines[line - 1][start:end]).span()
                asteriska.append(line - 1)
                asteriska.append(start + koordinate[0])
                asteriska.append(start + koordinate[1])
                repetitions -= 1
                start = start + koordinate[0]
                asterisk.append(asteriska)
            return asterisk
        else:
            downline = re.findall("\*", lines[line + 1][start:end])
            # if line != len(lines):
            if len(downline) > 0:
                repetitions = len(downline)
                while repetitions != 0:
                    asteriska = []
                    symbol.append(num)
                    koordinate = re.search("\*", lines[line + 1][start:end]).span()
                    print("AAAA", koordinate)
                    asteriska.append(line + 1)
                    asteriska.append(start + koordinate[0])
                    asteriska.append(start + koordinate[1])
                    repetitions -= 1
                    start = start + koordinate[0]
                    asterisk.append(asteriska)
                return asterisk

        # #        if line != 0 and re.search("[^\d.]", lines[line - 1][start:end]):
        # if re.search("\*", lines[line - 1][start:end]):
        #     koordinate = re.search("\*", lines[line-1][start:end]).span()
        #     asterisk.append(line - 1 )
        #     asterisk.append(start + koordinate[0])
        #     asterisk.append(start + koordinate[1])

        # symbol.append(num)
        # koordinate = re.search("\*", lines[line+1][start:end]).span()
        # asterisk.append(line + 1 )
        # asterisk.append(start + koordinate[0])
        # asterisk.append(start + koordinate[1])
        # return(asterisk)


asterisk = []
for coo in coords:
    print(coo)
    coo.update(
        {
            "asterisk": check2(
                coo["line"], coo["coo0"], coo["coo1"], coo["num"], len(lines), lines
            )
        }
    )
    if coo["asterisk"]:
        asterisk.append(coo)

asterisks = []

for item in asterisk:
    for ast in item["asterisk"]:
        asterisks.append(ast)
total = 0
sett = []

for valor in asterisks:
    print(valor)
    multi = 1
    x = asterisks.count(valor)
    if x == 2:
        if valor not in sett:
            sett.append(valor)

for valor in sett:
    print(valor)
    print("total", total)
    multi = 1
    for valores in asterisk:
        if valor in valores.get("asterisk"):
            print(valores.get("num"), "*")
            multi *= valores.get("num")
            print(multi)
    print("last multi", multi)
    total += multi
print(total)
# for line in lines:
#    print(line)
