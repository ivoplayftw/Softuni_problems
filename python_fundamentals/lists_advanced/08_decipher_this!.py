def decyper(msg):
    msg_list = msg.split()
    ascii_code = []
    msg_no_digits = []
    first_letter = ''
    other_part_of_str = ''
    decypered = []
    for element in msg_list:
        nums = ''.join(char for char in element if char.isdigit())
        ascii_code.append(int(nums))
        if nums in element:
            msg_no_digits.append(element.replace(nums, ''))
    for ele in range(len(ascii_code)):
        first_letter = chr(ascii_code[ele])
        if len(msg_no_digits[ele]) < 2:
            other_part_of_str = msg_no_digits[ele]
            decypered.append(first_letter + other_part_of_str)
        else:
            other_part_of_str = msg_no_digits[ele]
            start = other_part_of_str[0]
            end = other_part_of_str[-1]
            decypered.append(first_letter + end + other_part_of_str[1:-1] + start)
    return decypered


message = input()
print(*decyper(message))
