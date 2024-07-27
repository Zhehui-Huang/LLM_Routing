import numpy as os
import copy

# Define coordinates for all cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Number of cities and depots
num_cities = len(coordinates)
num_depots = 7  # depots are from index 0 to 6
num_robots = 8  # Assuming there's 8 robots

# Create robots starting all at depot city 0
robot_start = 0

# Euclidean distance calculator
def distance(i, j):
    return sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Generating a random solution with correct structure
# We'll distribute the cities randomly among the robots
random.seed(42)

def generate_initial_solution():
    cities = list(range(num_depots, num_cities))
    random.shuffle(cities)
    parts = random.sample(cities, num_robots-1)  # partitioning points
    parts.sort()
    tours = []
    start_index = 0
    for index in parts:
        tours.append([robot_start] + cities[start_index:index])
        start_index = index
    tours.append([robot_start] + cities[start_index:])
    return tours

# Measure the total distance for a given tour configuration
def total_distance(tours):
    total_cost = 0
    detailed_costs = []
    for tour in tours:
        tour_cost = 0
        for i in range(1, len(tour)):
            tour_cost += distance(tour[i-1], tour[i])
        tour_cost += distance(tour[-1], tour[0])  # Return to start depot cost
        detailed_costs.append((tour_cost, tour + [tour[0]]))
        total_cost += tour_cost
    return total_cost, detailed_costs

# Initial random tours
tours = generate_initial_solution()
total_cost, detailed_costs = total_expense(tours)

# Output format
print(f"Overall Total Travel Cost: {total_cost}")
for idx, (cost, tour) in enumerate(detailed_costs):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")