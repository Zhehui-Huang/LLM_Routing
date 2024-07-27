import math
import itertools

# City coordinates
cities = {
    0: (50, 42),  # Depot
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# City groups
groups = [
    [1, 2, 6],  # Group 0
    [3, 7, 8],  # Group 1
    [4, 5, 9]   # Group 2
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all possible tours from the given city groups including the depot
def generate_possible_tours():
    all_combinations = itertools.product(*groups)
    possible_tours = [[0] + list(combination) + [0] for combination in all_combinations]
    return possible_tours

# Calculate the tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Find the shortest tour from all possible tours
def find_shortest_tour():
    possible_tours = generate_possible_tours()
    min_cost = float('inf')
    best_tour = None
    for tour in possible_tours:
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

# Get the shortest tour and its cost
shortest_tour, tour_cost = find_shortest_tour()

# Output the results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {tour_cost:.2f}")