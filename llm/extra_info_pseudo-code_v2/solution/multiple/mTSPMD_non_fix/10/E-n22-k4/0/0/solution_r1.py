import numpy as np
import random
from math import sqrt

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Initial setup
num_robots = 4
num_cities = len(cities) - 1  # Exclude the depot

# Create random tours (splitting the list of cities other than the depot among robots)
city_indices = list(range(1, len(cities)))
random.shuffle(city_indices)

# Create approximately equal partitions for the 4 robots
robot_tour_lengths = np.array_split(city_indices, num_robots)

def calculate_tour_cost(tour, depot):
    cost = euclidean_distance(depot, tour[0])
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i-1], tour[i])
    return cost

# Starting depot is city 0 for all robots
tours = [[0] + list(tour) for tour in robot_tour_lengths]

# Calculate tour costs
tour_costs = [calculate_tour_cost(tour, 0) for tour in tours]
overall_cost = sum(tour_costs)

# Output results
for i, (tour, cost) in enumerate(zip(tours, tour_costs)):
    print(f"Robot {i} Tour: {[0] + tour + [0]}")  # Start and end at the depot
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")