import math

# Define city coordinates and given tours
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182),
}

# Given tours and costs for each robot
tours = [
    [0, 16, 14, 18, 15, 12, 0],
    [0, 10, 8, 6, 3, 4, 11, 0],
    [0, 17, 20, 21, 19, 13, 0],
    [0, 1, 2, 5, 7, 9, 0],
]

# Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Compute costs and check requirements
all_cities_covered = set()
maximum_travel_cost = 0
calculated_costs = []

for tour in tours:
    total_cost = 0
    previous_city = tour[0]
    tour_cities_set = set()
    
    for city in tour[1:]:
        total_cost += euclidean_distance(previous_city, city)
        tour_cities_set.add(city)
        all_cities_covered.add(city)
        previous_city = city
    
    calculated_costs.append(total_cost)
    if city != 0:  # Check if tour ends at depot
        print("FAIL: Tour does not end at the depot.")
        break
    if len(tour_cities_set.intersection(set(tour[1:-1]))) != len(tour[1:-1]):
        print("FAIL: Duplicate city visit detected.")
        break
        
    if total_cost > maximum_travel_cost:
        maximum_travel_options = total_cost  # Track the max distance traveled by any robot

# Validate all requirements:
# 1. If all cities excluding the depot city (city 0) must be visited exactly once
if all_cities_covered == set(cities.keys()) - {0}:
    # 2. Check if the provided max cost matches calculated max cost
    if abs(max(maximum_travel_options - max(calculated_costs))) < 1e-6:
        print("CORRECT")
    else:
        print("FAIL: Travel costs do not match expected values.")
else:
    print("FAIL: Not all cities are visited or some are visited more than once.")