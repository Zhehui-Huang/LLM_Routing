import math
from itertools import permutations

# Coordinates of cities including the depot as the first city
coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Function to calculate euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the total cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Assuming all cities must be visited, brute-force optimal for small number of cities
# Generate all possible tours that return to the starting point and find the minimum cost tour
def find_optimal_tour():
    min_cost = float('inf')
    best_tour = None
    all_cities = list(range(1, len(coordinates)))  # Excluding the depot initially for permutations
    for perm in permutations(all_cities):
        current_tour = [0] + list(perm) + [0]  # Start and end at the depot
        current_cost = tour_cost(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour
    return best_tour, min_cost

# Compute the best tour with its total travel cost
best_tour, total_cost = find_optimal_tour()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", total_cost)