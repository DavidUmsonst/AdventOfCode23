
def get_points_of_card(line):
    _, numbers = line.split(': ')
    winningNumbers, actualNumbers = numbers.split(' | ')
    listOfWinningNumbers = winningNumbers.split(' ')
    listOfActualNumbers = actualNumbers.split(' ')
    counter = -1
    for winningNumber in listOfWinningNumbers:
        if winningNumber != '':
            if winningNumber in listOfActualNumbers:
                counter += 1
    points = 0
    if counter>=0:
        points = 2**(counter)
    
    return points, counter+1


with open("./Day4/input") as file:
    lines  = [line.rstrip() for line in file]

N_lines = len(lines)
Number_of_cards = [1]*N_lines

total_points = 0
for i, line in enumerate(lines):
    points, number_of_winning_cards = get_points_of_card(line)
    additional_cards = Number_of_cards[i]
    for j in range(i+1,min([i+number_of_winning_cards+1,N_lines])):
        Number_of_cards[j] += additional_cards
    total_points += points

print(f"Task 1: Number of total points: {total_points}")
print(f"Task 2: Number of total cards won: {sum(Number_of_cards)}")