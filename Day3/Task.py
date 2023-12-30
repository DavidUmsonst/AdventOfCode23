import numpy as np

class NumberEntry:
    def __init__(self, xpos, ypos, length, value):
        self.xpos = xpos
        self.ypos = ypos
        self.length = length
        self.value = value

    def __repr__(self) -> str:
        return f"Number {self.value}, starting at ({self.xpos},{self.ypos}) with length {self.length}"

    def get_position(self):
        return self.xpos, self.ypos
    
    def get_length(self):
        return self.length
    
    def get_value(self):
        return self.value
    
    def set_position(self,x,y):
        self.xpos=x
        self.ypos=y
    
    def set_length(self, length):
        self.length=length
    
    def set_value(self, value):
        self.value = value
    
def generate_number_entries_and_index_matrix(lines):
    
    n_rows = len(lines)
    n_columns = len(lines[0])
    index_matrix = np.zeros((n_rows,n_columns))
    gear_matrix = np.zeros((n_rows,n_columns))
    list_of_numbers = []
    number_counter = 1

    for i, line in enumerate(lines):
        new_number = ''
        getting_new_number = False
        for j in range(n_columns):
            character_j = line[j]
            if character_j.isdigit():
                if not getting_new_number:
                    getting_new_number = True
                    new_number += character_j
                    x_start = i
                    y_start = j
                    gear_matrix[i][j] = number_counter
                else:
                    new_number += character_j
                    gear_matrix[i][j] = number_counter
                
                if j == n_columns-1:
                    list_of_numbers.append(NumberEntry(x_start,y_start,n_columns-y_start,int(new_number)))
                    getting_new_number = False
                    new_number = ''
                    gear_matrix[i][j] = number_counter
                    number_counter += 1

                    
            else:
                if character_j != '.':
                    index_matrix[i][j] = 1
                    if character_j == '*':
                        gear_matrix[i][j] = -1
                if getting_new_number:
                    list_of_numbers.append(NumberEntry(x_start,y_start,j-y_start,int(new_number)))
                    getting_new_number = False
                    new_number = ''
                    number_counter +=1
    # print(number_counter)
    return list_of_numbers, index_matrix, gear_matrix

def check_if_number_is_valid(number: NumberEntry, index_matrix):
    xpos,ypos = number.get_position()
    num_length = number.get_length()
    nx,ny = index_matrix.shape
    x_start = np.max([0,xpos-1])
    x_end = np.min([nx,xpos+2]) 
    y_start = np.max([0,ypos-1])
    y_end = np.min([ny,ypos+num_length+1])
    matrix_slice = index_matrix[x_start:x_end,y_start:y_end]
    
    is_valid = 1 in matrix_slice
    return is_valid

def get_result(lines):
    numbers, index_matrix, gear_matrix = generate_number_entries_and_index_matrix(lines)
    result = 0
    for number in numbers:
        if check_if_number_is_valid(number,index_matrix):
            result += number.get_value()
    return result

def get_gear_ratio_result(lines):
    numbers, index_matrix, gear_matrix = generate_number_entries_and_index_matrix(lines)
    

with open("./Day3/input") as file:    
    lines = [line.rstrip() for line in file]

numbers, index_matrix, gear_matrix = generate_number_entries_and_index_matrix(lines)

result = get_result(lines)

print(result)