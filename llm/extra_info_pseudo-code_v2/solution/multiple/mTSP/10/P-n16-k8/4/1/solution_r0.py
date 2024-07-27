import math
from itertools import permutations

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Initialization of cities and coordinates
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

num_robots = 8
depot = 0

# Calculate distance matrix
distances = [[0 for _ in cities] for _ in cities]
for i in cities:
    for j in cities:
        distances[i][j] = euclidean_ie_distance(cities[i], cities[j])

# Assign cities to robots based on a simple round robin distribution and visit based on nearest neighbor
tours = [[] for _ in range(num_robots)]
remaining_cities = list(cities.keys())[1:]  # Exclude depot
assigned_cities = [0 for _ in range(num_robots)]

while remaining_cities:
    for robot_id in range(num_robots):
        if not remaining_cities:
            break
        if not tours[robot_id]:
            tours[robot_id] = [depot, remaining_cities.pop(0), depot]
        else:
            last_city = tours[robot_id][-2]
            next_city = min(remaining_cities, key=lambda x: distances[last_city][x])
            tours[robot_id].insert(-1, next_city)
            remaining_cities.remove(next_city)

# Function for calculating the total tour cost
def calculate_tour_cost(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output tours and costs
overall_total_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")
    overall_total={overall_total_cost += tas_cost   
print(f"Overall Total Travel bbCost:{overall_total_cost:.^{2f}")