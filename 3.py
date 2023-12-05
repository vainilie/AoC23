import re

# Open a file in read mode ('r')
file_path = "input3"
file = open(file_path, "r")
# # Read the entire content of the file
# content = file.read()
# # Read the file line by line and save in lines
lines = []
for line in file:
    lines.append(line.rstrip())

for line in lines:
    line.replace(".", " ")
symbols =[]
total = 0
totall = 0
for num, line in enumerate(lines):
    
    symbol = []
    numbers = re.findall(r"\d+",line)
    for number in numbers:
        location = re.search(number,line).span()
        locA = location[0]
        locB = location[1]
        if location[0] != 0:
            locA = location[0] - 1
        if location[1] != len(line):
            locB = location[1] + 1
        if len(re.findall(r"[^\d\s]", line[locA:locB])) > 0:
            print(num, line, (re.findall(r"[^\d\s]", line[locA:locB])), number)
            symbol.append(number)
        else:
            if num !=0 and len(re.findall(r"[^\d\s]", lines[num - 1][locA:locB])) > 0:
                print("up",num, line, (re.findall(r"[^\d\s]", lines[num-1][locA:locB])), number)
                symbol.append(number)

            else: 
                if num < (len(lines)-1) and  len(re.findall(r"[^\d\s]", lines[num + 1][locA:locB])) > 0:
                    symbol.append(number)
        symbols += symbol
#print(symbols)

sumar = 0
for sym in symbols:
    sumar += int(sym)
    print(sumar)
