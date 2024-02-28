def get_race_times_and_distances(lines):
    
    _, race_time_string = lines[0].split(':')
    times = race_time_string.split()
    _, race_distance_string = lines[1].split(':')
    distances = race_distance_string.split()
    
    return times, distances

def get_one_race_time_and_distance(lines):
    
    _, race_time_string = lines[0].split(':')
    times = race_time_string.split()
    _, race_distance_string = lines[1].split(':')
    distances = race_distance_string.split()

    one_time = ""
    one_distance = ""

    for i in range(len(times)):
        one_time += times[i]
        one_distance += distances[i]

    return one_time, one_distance

class BoatRace:

    def __init__(self, time_length: int):
        self._time_length = time_length
        self._distances_travelled = [[]]*(self._time_length+1)
        for time_button_pressed in range(self._time_length+1):
            self._distances_travelled[time_button_pressed] = time_button_pressed*(self._time_length-time_button_pressed)

    def how_many_distances_further_than_x(self, x: int):
        counter = 0 
        for distance_travelled in self._distances_travelled:
            if distance_travelled>x:
                counter+=1
        
        return counter


with open("./Day6/input") as file:
    lines = [line.rstrip() for line in file]

race_times, race_distances = get_race_times_and_distances(lines)

result_task1 = 1
for i in range(len(race_times)):
    race = BoatRace(int(race_times[i]))
    result_task1 *= race.how_many_distances_further_than_x(int(race_distances[i]))


print(f"Result of Task 1: {result_task1}")

one_times, one_distance = get_one_race_time_and_distance(lines)

race = BoatRace(int(one_times))
result_task2 = race.how_many_distances_further_than_x(int(one_distance))

print(f"Result of Task 2: {result_task2}")
