import math
from itertools import permutations

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Compute the total cost of a given tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

# Find the shortest possible route via permutations (brute-force approach to get an initial feasible tour)
def find_best_tour():
    best_cost = float('inf')
    best_tour = []
    all_cities = list(cities.keys())[1:]  # Exclude the depot city for permutation
    for perm in permutations(all_cities):
        current_tour = [0] + list(perm) + [0]  # Starting and ending at the depot city
        current_cost = calculate_tour_cost(current_tour)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour
    return best_tour, best_cost

# Invoke the function to get the solution
best_tour, best_cost = find_best_tour()

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")