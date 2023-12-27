def get_first_and_last_number(line,elements):
    min_ind_elements = [-1]*len(elements)
    max_ind_elements = [-1]*len(elements)

    for i, element in enumerate(elements):
        i_min, i_max = find_smallest_and_largest_occurence_of_element_in_line(line,element)
        min_ind_elements[i] = i_min
        max_ind_elements[i] = i_max    
    
    el_min, el_max = find_first_and_last_element(min_ind_elements,max_ind_elements,elements)

    return turn_element_to_number(el_min), turn_element_to_number(el_max)

def get_sum_of_first_and_last_number(line, elements):
    first_num, last_num = get_first_and_last_number(line,elements)

    return int(first_num+last_num)

def find_smallest_and_largest_occurence_of_element_in_line(line, element):
    i_min = -1
    i_max = -1

    i_min = line.find(element)
    if i_min == -1:
        # print("Element not in line")
        return i_min, i_max
    inc = 1
    i_max = line[i_min+inc:].find(element)
    if i_max == -1:
        i_max = i_min
    else:
        i_max = i_min+inc+i_max
        while True:
            inc += 1
            i_max_new = line[i_min+inc:].find(element)
            if i_max_new == -1:
                break
            else:
                i_max = i_min+inc+i_max_new
        
    return i_min, i_max

def find_first_and_last_element(minimum_indices, maximum_indices, elements):
    ind_min = float('inf')
    ind_max = -1

    for i, element in enumerate(elements):
        ind_min_new = minimum_indices[i]
        if ind_min_new > -1:
            if ind_min_new<ind_min:
                ind_min = ind_min_new
                el_min = element
        ind_max_new = maximum_indices[i]
        if ind_max_new > -1:
            if ind_max_new>ind_max:
                ind_max = ind_max_new
                el_max = element

    return el_min, el_max

def turn_element_to_number(element):
    if element == "one":
        return "1"
    
    elif element == "two":
        return "2"

    elif element == "three":
        return "3"

    elif element == "four":
        return "4"

    elif element == "five":
        return "5"

    elif element == "six":
        return "6"

    elif element == "seven":
        return "7"

    elif element == "eight":
        return "8"

    elif element == "nine":
        return "9"
    
    else:
        return element   

with open("./Day1/input") as file:
    lines = [line.rstrip() for line in file]

N_lines = len(lines)
elements = ["0", "1", "2","3","4","5","6","7","8","9","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

result = 0
for i in range(N_lines):
    result += get_sum_of_first_and_last_number(lines[i], elements)
print(result)