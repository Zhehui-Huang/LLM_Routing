import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Number of robots
num_robots = 8

# Partition the city indices into approximately equal parts, excluding the depot
city_indices = list(cities.keys())[1:]
partitions = [city_indices[i::num_robots] for i in range(num_robots)]

# Function to calculate the complete tour cost for a robot
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Assign each partition to a robot and compute the tours and costs
tours = []
costs = []

for partition in partitions:
    # Create a full tour starting and ending at the depot city for each partition
    tour = [0] + partition + [0]
    total_cost = calculate_tour_cost(tour)
    tours.append(tour)
    costs.append(total_cost)

# Output the results
overall_total_cost = sum(costs)
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")