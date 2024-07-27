import random
from math import sqrt

# Define the cities and their coordinates
cities = {
    0: (145, 215), # Depot city 0
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
    21: (139, 182)
}

# Number of robots and their starting depots
num_robots = 4
depot_cities = {0: 0}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Nearest Neighbor Algorithm for individual tour
def nearest_neighbor_tour(start, unvisited):
    tour = [start]
    current_city = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_ciety
    return tour

# Implementing four basic tours for simplicity - one for each robot
unvisited_cities = set(cities.keys()) - {0}
tours = []
total_cost = 0

for i in range(num_robots):
    if unvisited_cities:
        start_city = depot_cities.get(i, 0)  # Each robot starts from depot city 0
        tour = nearest_neighbor_tour(start_city, list(unvisited_cities))
        unvisited_cities -= set(tour)
        tours.append(tour)

# Calculating travel cost for each tour
costs = []
for tour in tours:
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i + 1])
    costs.append(cost)
    total_cost += cost

# Print out the results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {round(costs[i], 2)}")

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")