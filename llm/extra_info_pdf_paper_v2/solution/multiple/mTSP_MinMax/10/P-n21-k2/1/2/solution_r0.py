import math
import random

# Define city coordinates with city index as key
coordinates = {
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

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Initialize robots
number_of_robots = 2
tours = {i: [0] for i in range(number_of_robots)}

# Assign cities (excluding depot) to robots initially
cities = list(range(1, 21))
random.shuffle(cities)

# Initial distribution of cities
cities_per_robot = len(cities) // number_of_robots
for i in range(number_of_robots):
    tours[i].extend(cities[i * cities_per_robot:(i + 1) * cities_per_robot])

# Adding the depot to the end of each tour
for i in range(number_of_robots):
    tours[i].append(0)

# Function to compute tour cost
def compute_tour_cost(tour):
    cost = 0
    for j in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[j]], coordinates[tour[j + 1]])
    return cost

# Improvement phase: variable neighborhood search (simplified for example)
def two_opt_swap(tour):
    best_cost = compute_tour_cost(tour)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue
                new_tour = tour[:]
                new_tour[i:j] = tour[j - 1:i - 1:-1]
                new_cost = compute_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    improved = True
        tour = best_tour[:]
    return tour

# Apply local search to each robot's tour
for i in range(number_of_robots):
    tours[i] = two_opt_swap(tours[i])

# Calculate costs
tour_costs = {i: compute_tour_cost(tours[i]) for i in range(number_of_robots)}
max_cost = max(tour_costs.values())

# Output formatted results
for i in range(number_of_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")