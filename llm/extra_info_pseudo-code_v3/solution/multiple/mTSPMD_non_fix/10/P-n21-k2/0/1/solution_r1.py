import math
import numpy as np
from collections import defaultdict

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Function to compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Starting depot for the robots (multiple possible start depots, but all start from depot city 0)
depots = {0: cities[0]}

# Initialize lists to hold the tour for each robot
num_robots = 2
tours = {i: [0] for i in range(num_robots)}

# List of all cities without starting city
remaining_cities = list(cities.keys())[1:]

# Initial NNS construction of tours
for n in range(num_robots):
    current_city = 0  # starting city for each robot is depot city 0
    while remaining_cities:
        # Find nearest city from current city
        nearest_city = min(remaining_cities, key=lambda x: euclidean_distance(current_city, x))
        remaining_cities.remove(nearest_city)
        tours[n].append(nearest_city)
        current_city = nearest_city
        if len(tours[n]) >= len(cities) // num_robots:
            break

# Calculate tour and total travel costs
def tour_cost(tour):
    total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return total_cost

total_overall_cost = 0

for n in range(num_robots):
    tours[n].append(0)  # assuming they need not return to a depot; adjust here
    individual_cost = tour_cost(tours[n])
    total_overall_cost += individual_cost
    print(f"Robot {n} Tour: {tours[n]}")
    print(f"Robot {n} Total Travel Cost: {individual_cost:.2f}")

print(f"Overall Total Travel Cost: {total_overall_cost:.2f}")