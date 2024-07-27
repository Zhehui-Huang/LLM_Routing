import itertools
from scipy.spatial.distance import euclidean

# Define the cities with their coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Find all combinations of 11 cities plus the depot city, forming groups of 12 cities
combinations_of_cities = itertools.combinations(range(1, 15), 11)

# Define a function to calculate the total cost of a tour
def calculate_tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Variables to track the best tour and its cost
min_cost = float('inf')
best_tour = []

# Check each combination
for combo in combinations_of_cities:
    current_cities = [0] + list(combo)
    # Permutations of the selected cities to form tours
    for perm in itertools.permutations(current_cities):
        tour = list(perm) + [0]  # ensure it starts and ends at depot
        cost = calculate_tour_cost(tour, cities)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))