import math

# Definition of cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Solution provided for the robot tours
robot_tours = [
    [0, 1, 0],
    [0, 2, 0],
    [0, 3, 0],
    [0, 4, 0],
    [0, 5, 0],
    [0, 6, 0],
    [0, 7, 0],
    [0, 10, 12, 15, 11, 8, 13, 9, 14, 0]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Check if all cities except depot are visited exactly once
visited_cities = set()
all_cities_visited = set(range(1, 16))

# Check each tour
for tour in robot_tours:
    for i in range(len(tour) - 1):
        visited_cities.add(tour[i+1])

# Check if all cities have been visited once and only once
correct_city_visit = (visited_cities == all_cities_visited)

# Validate travel costs are as calculated
costs_are_correct = True
travel_costs = [
    27.78,
    42.05,
    65.12,
    44.05,
    46.17,
    24.08,
    44.05,
    142.51
]

for i, tour in enumerate(robot_tours):
    calculated_cost = 0
    for j in range(len(tour) - 1):
        calculated_cost += euclidean_distance(tour[j], tour[j+1])
    # Compare calculated cost to provided cost
    if not math.isclose(calculated_cost, travel_costs[i], rel_tol=1e-2):
        costs_are_correct = False
        break

# Determine if solution is correct
if correct_city_visit and costs_are_correct:
    print("CORRECT")
else:
    print("FAIL")