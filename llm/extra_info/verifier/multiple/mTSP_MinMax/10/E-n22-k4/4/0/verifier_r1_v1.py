import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

solution_tours = [
    [0, 12, 14, 15, 16, 18, 0],     # Robot 0
    [0, 3, 4, 6, 8, 10, 11, 0],     # Robot 1
    [0, 13, 17, 19, 20, 21, 0],     # Robot 2
    [0, 1, 2, 5, 7, 9, 0]           # Robot 3
]

given_costs = [121.20933003054614, 124.23927957725854, 138.2546749628742, 111.83855721201843]

# Ensure all tours start and end at the depot
start_end_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in solution_tours)

# Ensure each city except the depot is visited exactly once
all_cities = set(range(1, 22))
visited_cities = set(city for tour in solution_tours for city in tour if city != 0)
visits_once = all_cities == visited_cities

# Calculate costs and check they match the given costs closely
computed_costs = []
for tour in solution_tours:
    cost = sum(euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour)-1))
    computed_costs.append(cost)

correct_costs = all(abs(given - computed) < 1e-6 for given, computed in zip(given_costs, computed_costs))

# Ensure the objective to minimize the maximum distance is met
minimize_max_distance = max(computed_costs) <= max(given_costs)

# Check if all conditions are satisfied
correct_solution = start_end_deport and visits_once and minimize_max_distance and debug_costs
print("CORRECT" if debug_solution else "FAIL")