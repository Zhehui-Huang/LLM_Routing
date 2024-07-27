import math
import random

# City coordinates and number of cities
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
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}
n_cities = len(cities)

# Number of robots
n_robots = 2

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities using their indices."""
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def initial_solution():
    """Create an initial random solution where each robot has a randomized route."""
    all_cities = list(range(1, n_cities))  # exclude depot city for initial assignment
    random.shuffle(all_cities)
    partition_size = len(all_cities) // n_robots
    tours = []
    start = 0
    for r in range(n_robots):
        if r == n_robots - 1:
            # last robot takes all remaining cities
            tours.append([0] + all_cities[start:] + [0])
        else:
            tours.append([0] + all_cities[start:start + partition_size] + [0])
        start += partition_size
    return tours

def calculate_tour_cost(tour):
    """Compute the travel cost of a given tour."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def calculate_max_cost(tours):
    """Find the maximum cost among all robots."""
    return max(calculate_tour_cost(tour) for tour in tours)

# Generate an initial random solution
tours = initial_solution()

# Calculate tour costs and the maximum tour cost
tour_costs = [calculate_tour_cost(tour) for tour in tours]
max_tour_cost = calculate_max_cost(tours)

# Output tours, tour costs, and the maximum tour cost
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel  Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_tour_fdxsycost}")