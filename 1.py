# lines = []
# # Open a file in read mode ('r')
# file_path = "input1"
# file = open(file_path, "r")
# # Read the entire content of the file
# # content = file.read()
# # Read the file line by line and save in lines
# for line in file:
#     lines.append(line.rstrip())


# lines_replaced = []
# digits = []
# for line in lines:
#     print(line)
#     digit = {}
#     digit1 = []
#     num = 1
#     while num < 10:
#         if str(num) in line:
#             if line.count(str(num)) > 0:
#                 print(line)
#             pos = line.find(str(num))
#             digit.update({pos: num})
#         num += 1

#     for word in word_digit_pairs:
#         if word in line:
#             pos = line.find(word)
#             print(word)
#             digit.update({pos: int(word_digit_pairs[word])})
#     print(digit)
#     for item in dict(sorted(digit.items())):
#         digit1.append(digit[item])
#     print(digit1)
#     digits.append(digit1)

#     #    print(line.find(word))
#     #   print(word)


# # all_digits=[]
# # for line in lines_replaced:
# #     digits = []
# #     for character in line:
# #         if character.isdigit(): #test if it is digit or not
# #             digits.append(character)
# #     all_digits.append(digits)
# #        # print(line, end='')  # end='' to avoid adding extra newline characters

# sum_all = 0

# for x, line in enumerate(digits):
#     # print(lines[x])
#     # print(line)

#     first_and_last = str(line[0]) + str(line[-1])  # sum
#     # print(type(first_and_last))
#     sum_all += int(first_and_last)
#     # all_first_and_last.append(first_and_last)
# print(sum_all)

lines = []
# Open a file in read mode ('r')
file_path = "input1"
file = open(file_path, "r")
# # Read the entire content of the file
# content = file.read()
# # Read the file line by line and save in lines
for line in file:
    lines.append(line.rstrip())

# # PART 2
# # create a dict
word_digit_pairs = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def count_appear(line, num):
    times = line.count(num)
    data = {}
    if times > 0:
        initial_pos = 0
        while times > 0:
            pos = line.find(num, initial_pos)
            if len(num) > 1:
                data.update({pos: word_digit_pairs[num]})
            else:
                data.update({pos: num})
            initial_pos = pos + 1
            times -= 1
        return data
    else:
        pass


# for line in lines:
all_digits_sort = []
for line in lines:
    digits = {}
    number = 1
    while number < 10:
        if line.count(str(number)) > 0:
            digits.update(count_appear(line, str(number)))
        number += 1

    for num in word_digit_pairs:
        if line.count(num) > 0:
            digits.update(count_appear(line, num))
    all_digits_sort.append(sorted(digits.items()))

add = 0
for line in all_digits_sort:
    add += int(line[0][1] + line[-1][1])
print(add)
