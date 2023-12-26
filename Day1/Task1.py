def get_first_and_last_number(line):
    found_first_num = False
    found_last_num = False
    first_num = -1
    last_num = -1
    for i in range(len(line)):
        if not found_first_num:
            forward_element = line[i]
            try:
                int(forward_element)
                first_num = forward_element
                found_first_num = True
            except ValueError:
                pass

        if not found_last_num:
            backward_element = line[-(i+1)]
            try:
                int(backward_element)
                last_num = backward_element
                found_last_num = True
            except ValueError:
                pass
    
    return first_num, last_num

def get_sum_of_first_and_last_number(line):
    first_num, last_num = get_first_and_last_number(line)

    return int(first_num+last_num)

with open("./Day1/input") as file:
    lines = [line.rstrip() for line in file]

N_lines = len(lines)

result = 0
for i in range(N_lines):
    result += get_sum_of_first_and_last_number(lines[i])

print(result)
