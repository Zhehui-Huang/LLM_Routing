import math
from itertools import permutations

# Input data: Cities and their coordinates (including the depot city)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)}

# Demands for each city
demands = {0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8, 10: 8,
           11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15}

robot_capacity = 160
num_robots = 2

# Compute Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to check robot load capacity and valid tour
def valid_tour(tour, demands, capacity_limit):
    total_demand = 0
    for city in tour:
        total_demand += demands[city]
        if total_demand > capacity_limit:
            return False
    return True

# Try permutations; note: for larger scale problems, this won't be efficient
# we are making it simple here due to the small number of cities and 2 robots
min_total_cost = float('inf')
best_assignments = None

for perm in permutations(range(1, 21)):  # All cities except the depot
    # Split permutation into two lists for two robots arbitrarily and make sure valid according to the rules
    for i in range(2, len(perm)):  # Possible splits, at least one city per robot, excluding the depot
        robot1_tour = [0] + list(perm[:i]) + [0]
        robot2_tour = [0] + list(perm[i:]) + [0]
        
        if valid_tour(robot1_tour, demands, robot_capacity) and valid_tour(robot2_tour, demands, robot_capacity):
            # Calculate total cost for these tours
            robot1_cost = sum(euclidean_distance(robot1_tour[j], robot1_tour[j+1]) for j in range(len(robot1_tour)-1))
            robot2_cost = sum(euclidean_distance(robot2_tour[j], robot2_tour[j+1]) for j in range(len(robot2_tour)-1))
            total_cost = robot1_cost + robot2_cost

            if total_cost < min_total_cost:
                min_total_cost = total_cost
                best_assignments = (robot1_tour, robot1_cost, robot2_tour, robot2_cost)

# Output the best route assignments and costs found
robot1_tour, robot1_cost, robot2_tour, robot2_cost = best_assignments
print(f"Robot 0 Tour: {robot1_tour}")
print(f"Robot 0 Total Travel Cost: {robot1_cost:.2f}")
print(f"Robot 1 Tour: {robot2_tour}")
print(f"Robot 1 Total Travel Cost: {robot2_cost:.2f}")
print(f"Overall Total Travel Cost: {robot1_cost + robot2_cost:.2f}")