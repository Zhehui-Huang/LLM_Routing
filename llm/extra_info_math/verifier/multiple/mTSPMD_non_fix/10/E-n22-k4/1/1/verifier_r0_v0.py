import math

# Data
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

tours = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]

# Functions to calculate the distance and cost
def calculate_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Verify test 1: Each city is visited exactly once across all robots
visited_cities = sum([tour[1:-1] for tour in tours], [])
if len(set(visited_cities)) != 21 or any(visited_cities.count(city) != 1 for city in range(1, 22)):
    print("FAIL")
    exit()

# Verify test 2: All robots start their tour from depot city 0
if not all(tour[0] == 0 for tour in tours):
    print("FAIL")
    exit()

# Verify test 3: Allow robots to end their tours at any city
# (implicitly verified by the format and no need for additional checks)

# Verify test 4: Minimize total travel cost
# Calculate costs claimed by the tasks
claimed_costs = [0, 0, 0, 0]  # Given in the task, all are 0
calculated_costs = [sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)) for tour in tours]
if any(claimed != calc for claimed, calc in zip(claimed_costs, calculated_costs)):
    print("FAIL")
    exit()

# If all checks are passed
print("CORRECT")