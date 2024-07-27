import math

# This function calculates the Euclidean distance between two cities using their coordinates.
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates - Indexed by city number
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# The given tours and expected travel costs
robots_info = {
    0: {'tour': [0, 1, 2, 3, 4, 5, 0], 'reported_cost': 162.64},
    1: {'tour': [0, 6, 7, 8, 9, 10, 0], 'reported_cost': 119.78},
    2: {'tour': [0, 11, 12, 13, 14, 15, 0], 'reported_cost': 138.09},
    3: {'tour': [0, 16, 17, 18, 19, 20, 21, 0], 'reported_cost': 152.52}
}

# Calculate actual tour travel cost and check correctness
calculated_total_cost = 0
all_cities_visited = set()

for robot_id, info in robots_info.items():
    tour = info['tour']
    reported_cost = info['reported_cost']
    calculated_cost = 0
    
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL: Robot {} doesn't start and end at the depot city (City 0).".format(robot_id))
        break
    
    for i in range(len(tour) - 1):
        start_city = tour[i]
        end_city = tour[i+1]
        distance = calculate_distance(cities[start_city], cities[end_city])
        calculated_cost += distance
        all_cities_visited.add(start_city)
        if i > 0:  # Exclude the depot city
            all_cities_visited.add(end_city)

    calculated_cost = round(calculated_cost, 2)  # Round to two decimal places
    calculated_total_cost += calculated_cost
    
    if calculated_cost != reported_cost:
        print("FAIL: Incorrect cost for robot {}. Reported: {}, Calculated: {}".format(robot_id, reported_cost, calculated_cost))
        break
else:
    if len(all_cities_visited) == 22:  # Including the depot city
        print("CORRECT")
    else:
        print("FAIL: Not all cities are visited exactly once.")