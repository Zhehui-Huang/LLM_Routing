import math
import random
from itertools import permutations

# Data input
coords = {
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
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

num_robots = 2
cities = list(range(1, len(coords)))

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    c1, c2 = coords[city1], coords[city2]
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Function to compute the total travel cost of a tour
def compute_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))


# Function to divide cities amongst robots roughly evenly and greedily optimizing local paths
def divide_and_optimize(cities, num_robots):
    random.shuffle(cities)  # Shuffle to randomize the selection
    portions = [[] for _ in range(num_robots)]

    # Greedily assign cities to each robot
    for city in cities:
        # Choose the robot that minimizes the increase in path length when this city is added
        best_robot = None
        best_extra_cost = float('inf')
        best_new_tour = []

        for r in range(num_robots):
            # Current tour for robot r
            current_tour = portions[r] + [0]  # Circular
            best_local_tour = None
            local_best_cost = float('inf')
            
            # Try inserting the city at every possible position in the tour
            for i in range(len(current_tour)):
                new_tour = current_tour[:i] + [city] + current_tour[i:]
                cost = compute_cost(new_tour)
                if cost < local_best_cost:
                    local_best_cost = cost
                    best_local_tour = new_tour
            
            # If this insertion minimizes the extra cost across all robots
            if local_best_cost - compute_cost(current_tour) < best_extra_cost:
                best_extra_cost = local_best_cost - compute_cost(current_tour)
                best_robot = r
                best_new_tour = best_local_tour

        portions[best_robot] = best_new_tour[1:-1]  # Remove depot from ongoing city list
    
    for r in range(num_robots):
        portions[r] = [0] + portions[r] + [0]

    return portions

# Split cities amongst robots
tours = divide_and_optimize(cities, num_robots)

# Calculate the costs
costs = [compute_cost(tour) for tour in tours]
max_cost = max(costs)

# Generate Output
for i in range(num_robots):
    print(f'Robot {i} Tour:', tours[i])
    print(f'Robot {i} Total Travel Cost:', costs[i])

print(f'Maximum Travel Cost:', max_cost)