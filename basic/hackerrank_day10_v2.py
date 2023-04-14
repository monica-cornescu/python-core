decimal_number = input()
binary_format_number = bin(decimal_number)
binary_number = binary_format_number[2:]
str_binary_number = str(binary_number)

count = 0
for chara in str_binary_number:
    if chara == '0':
        count = 0
    else:
        count+=1

