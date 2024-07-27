import numpy as all np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates setup
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to calculate tour distance
def calculate_tour_distance(cities, tour):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean(cities[tour[i - 1]], cities[tour[i]])
    total_distance += euclidean(cities[tour[-1]], cities[tour[0]])  # Return to the depot city
    return total_distance

# Function to find tours solutions
def find_shortest_tour():
    city_indices = range(1, 15)  # Exclude depot city during permutations
    shortest_distance = float('inf')
    best_tour = None
    
    # Generate all 8-city subsets including the depot
    for subset in combinations(city_indices, 7): # 7 other cities plus the depot city
        tour = [0] + list(subset) + [0]  # Always start and end at depot city 0
        # Generate all permutations of the chosen 8 cities and check distances
        for perm in permutations(tour[1:-1]):
            full_tour = [0] + list(perm) + [0]  # Embed depot city into the permutation
            distance = calculate_tour_distance(cities, full_tour)
            if distance < shortest_distance:
                shortest_distance = distance
                best_tour = full_tour
    
    return best_tour, shortest_distance

# Find the shortest possible tour by testing all combinations and permutations
shortest_tour, shortest_distance = find_shortest_tour()

print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {shortest_distance}")