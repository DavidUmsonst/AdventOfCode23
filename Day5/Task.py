def get_mapped_key_from_mappings(key_to_be_mapped: int, mapping: list):
    mapped_key = -1
    for map in mapping:        
        destination_range_start, source_range_start, range_length = map.split(" ")
        destination_range_start = int(destination_range_start)
        source_range_start = int(source_range_start)
        range_length = int(range_length)
        if key_to_be_mapped in range(source_range_start,source_range_start+range_length):
            mapped_key = destination_range_start + key_to_be_mapped - source_range_start

    if mapped_key == -1:
        return key_to_be_mapped
    else:
        return mapped_key
    
def get_seeds(desired_seeds):
    seeds = []
    for value in desired_seeds.split(" "):
        if value != "seeds:":
            seeds.append(int(value))
    
    return seeds
    
def separate_seeds_and_mappings_from_input(lines):
    seed_to_soil_mappings=[]

    soil_to_fertilizer_mappings=[]

    fertilizer_to_water_mappings=[]

    water_to_light_mappings=[]

    light_to_temperature_mappings=[]

    temperature_to_humidity_mappings=[]

    humidity_to_location_mappings=[]

    counter_mappings = -1
    

    for i, line in enumerate(lines):
        if i == 0:
            seeds = line
        elif line == "seed-to-soil map:":
            counter_mappings=0
        elif line == "soil-to-fertilizer map:":
            counter_mappings=1
        elif line == "fertilizer-to-water map:":
            counter_mappings=2
        elif line == "water-to-light map:":
            counter_mappings=3
        elif line == "light-to-temperature map:":
            counter_mappings=4
        elif line == "temperature-to-humidity map:":
            counter_mappings=5
        elif line == "humidity-to-location map:":
            counter_mappings=6
        elif line == "":
            pass
        else:
            if counter_mappings == 0:
                seed_to_soil_mappings.append(line)
            elif counter_mappings == 1:
                soil_to_fertilizer_mappings.append(line)
            elif counter_mappings == 2:
                fertilizer_to_water_mappings.append(line)
            elif counter_mappings == 3:
                water_to_light_mappings.append(line)
            elif counter_mappings == 4:
                light_to_temperature_mappings.append(line)
            elif counter_mappings == 5:
                temperature_to_humidity_mappings.append(line)
            elif counter_mappings == 6:
                humidity_to_location_mappings.append(line)
    return seeds, seed_to_soil_mappings, soil_to_fertilizer_mappings, fertilizer_to_water_mappings, water_to_light_mappings, light_to_temperature_mappings, temperature_to_humidity_mappings, humidity_to_location_mappings

with open("./Day5/input") as file:
    lines = [line.rstrip() for line in file]

desired_seeds, seed_to_soil_mappings, soil_to_fertilizer_mappings, fertilizer_to_water_mappings, water_to_light_mappings, light_to_temperature_mappings, temperature_to_humidity_mappings, humidity_to_location_mappings = separate_seeds_and_mappings_from_input(lines)
print(desired_seeds)

# initialize array that contains the seeds
seeds = get_seeds(desired_seeds)

locations = []
# task 1
for seed in seeds:
    soil_value = get_mapped_key_from_mappings(seed,seed_to_soil_mappings)
    fertilzer_value = get_mapped_key_from_mappings(soil_value,soil_to_fertilizer_mappings)
    water_value = get_mapped_key_from_mappings(fertilzer_value,fertilizer_to_water_mappings)
    light_value = get_mapped_key_from_mappings(water_value,water_to_light_mappings)
    temperature_value = get_mapped_key_from_mappings(light_value,light_to_temperature_mappings)
    humidity_value = get_mapped_key_from_mappings(temperature_value,temperature_to_humidity_mappings)
    location_value = get_mapped_key_from_mappings(humidity_value,humidity_to_location_mappings)

    locations.append(location_value)

print("Location from Task 1:")
print(min(locations))


