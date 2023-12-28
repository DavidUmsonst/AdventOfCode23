def get_line_id_and_max_number_of_each_color(line):
    GameID, AllRuns = line.split(": ")
    _, currentID = GameID.split(" ")
    runs = AllRuns.split("; ")
    N_runs = len(runs)
    n_green_max = -1
    n_blue_max = -1
    n_red_max = -1
    for i in range(N_runs):
        n_green, n_blue, n_red = get_number_of_colored_cubes(runs[i])
        if n_green > n_green_max:
            n_green_max = n_green
        if n_blue > n_blue_max:
            n_blue_max = n_blue
        if n_red > n_red_max:
            n_red_max = n_red
    
    return int(currentID), n_green_max, n_blue_max, n_red_max

def get_number_of_colored_cubes(run):
    results = run.split(", ")
    n_green = 0
    n_blue = 0
    n_red = 0
    for i in range(len(results)):
        num, color = results[i].split(" ")
        if color == 'green':
            n_green = int(num)
        elif color == 'red':
            n_red = int(num)
        elif color == "blue":
            n_blue = int(num)
    
    return n_green, n_blue, n_red

n_green_possible = 13
n_blue_possible = 14
n_red_possible = 12
result = 0
result2 = 0


with open("./Day2/input") as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    id, n_green, n_blue, n_red = get_line_id_and_max_number_of_each_color(line)
    if n_green <= n_green_possible and n_blue<= n_blue_possible and n_red<=n_red_possible:
        result += id
    result2 += n_green*n_blue*n_red

print(result)
print(result2)



