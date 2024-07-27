import numpy as np
import random
from scipy.spatial import distance

# City coordinates
cities = {
    0: (145, 215),
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

# Distance matrix computation
def compute_distance_matrix(cities):
    num_cities = len(cities)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            matrix[i][j] = distance.euclidean(cities[i], cities[j])
    return matrix

distance_matrix = compute_distance_matrix(cities)

# Initializing robots and depots
robots = 4
depots = {0: 0, 1: 1, 2: 2, 3: 3}

# Function to compute the total travel cost of a tour
def tour_cost(tour, distance_matrix):
    cost = 0.0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    return cost

# Generate a valid initial solution
def generate_initial_solutions(depots, non_depots, num_robots):
    all_cities = non_depots.copy()
    random.shuffle(all_cities)
    parts = np.array_split(all_cities, num_robots)
    tours = []
    for i, part in enumerate(parts):
        tour = [depots[i]] + list(part) + [depots[i]]
        tours.append(tour)
    return tours

# Evaluate solutions
def evaluate_solutions(tours, distance_matrix):
    total_cost = sum(tour_cost(tour, distance_matrix) for tour in tours)
    return total_cost

def initialize_population():
    non_depots = list(set(cities.keys()) - set(depots.values()))
    population = [generate_initial_solutions(depots, non_depots, robots) for _ in range(50)]
    return population

# Population Initialization
population = initialize_population()

# Evolve Population
best_solution = None
best_cost = float('inf')

for solution in population:
    cost = evaluate_solutions(solution, distance_matrix)
    if cost < best_cost:
        best_cost = cost
        best_solution = solution

# Display Final Solution
overall_cost = 0
for idx, tour in enumerate(best_solution):
    cost = tour--

cost(tour, distance_matrix)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
    overall_cost += cost

print(f"Overall Total Travel Cost: {overall_cost}")