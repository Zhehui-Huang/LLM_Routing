import math

# Define the function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define city coordinates including the depot
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Given solution tours and costs
solution_tours = [
    [0, 12, 14, 15, 16, 18, 0],     # Robot 0
    [0, 3, 4, 6, 8, 10, 11, 0],     # Robot 1
    [0, 13, 17, 19, 20, 21, 0],     # Robot 2
    [0, 1, 2, 5, 7, 9, 0]           # Robot 3
]

given_costs = [121.20933003054614, 124.23927957725854, 138.2546749628742, 111.83855721201843]

# Testing requirements

# Requirment 1 and 6
# All tours should start and end at depot (city index 0)
start_end_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in solution_tours)

# Requirement 2
# Collectively visit each city exactly once
all_cities = set(range(1, 22))  # Cities except the depot
visited_cities = set(city for tour in solution_tours for city in tour[1:-1])
visits_once = all_cities == visited_cities and all(tour.count(city) == 1 for tour in solution_tours for city in tour if city != 0)

# Requirement 3
# Minimize maximum distance
computed_costs = []
for tour in solution_tours:
    cost = sum(euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour)-1))
    computed_costs.append(cost)
minimize_max_distance = max(computed_costs) == min(max(given_costs), max(computed_costs)) 

# Requirement 7
# Correct cost computation
correct_costs = all(abs(given - computed) < 1e-6 for given, computed in zip(given_bots, computed_costs))

# Collect results
correct_solution = all([start_end_dept, lids_once, minimize_max_distance, correct_costs])
print("CORRECT" if correct_solution else "FAIL")