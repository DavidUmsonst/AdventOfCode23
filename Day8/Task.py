def go_to_goal(input, graph):
    N_input = len(input)
    goal_reached = False
    steps_taken = 0
    current_state = 'AAA'

    while goal_reached == False:
        input_to_take = steps_taken % N_input
        command = input[input_to_take]
        directions = graph[current_state]
        if command == 'L':
            current_state = directions[0]
        else:
            current_state = directions[1]
        
        steps_taken += 1

        if current_state == 'ZZZ':
            goal_reached = True
        
    
    return steps_taken


def get_input_and_graph(lines):
    graph = dict()
    for i, line in enumerate(lines):
            if i == 0:
                input = line
            if i >= 2:
                node, edges = line.split(" = ")
                graph[node] = edges[1:-1].split(", ")
    return input, graph

with open('./Day8/input') as file:
    lines = [line.rstrip() for line in file]

input, graph = get_input_and_graph(lines)

steps_taken = go_to_goal(input=input, graph=graph)

print(steps_taken)