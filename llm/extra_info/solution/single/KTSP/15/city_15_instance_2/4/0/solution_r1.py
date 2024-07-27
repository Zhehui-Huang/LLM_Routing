import numpy as np
from itertools import permutations, combinations
from scipy.spatial.distance import euclidean

# City coordinates setup
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to calculate the distance between two cities
def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Function to calculate total tour distance
def calculate_tour_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i + 1])
    total_distance += calculate_distance(tour[-1], tour[0])  # Return to depot
    return total_distance

# Function to find the shortest tour
def find_shortest_tour():
    shortest_distance = float('inf')
    best_tour = None
    city_indices = list(cities.keys())[1:]  # All cities except the depot
    
    # Generate all combinations of 7 other cities to visit
    for subset in combinations(city_indices, 7):
        possible_tour = [0] + list(subset)  # Start at depot, add cities, and then return to depot
        # Permute the possible tours
        for perm in permutations(possible_tour[1:]):
            tour = [0] + list(perm) + [0]  # Ensure start and end at depot
            distance = calculate_tour_distance(tour)
            if distance < shortest_distance:
                shortest_distance = distance
                best_tour = tour

    return best_tour, shortest_distance

# Calculate the best tour and its distance
shortest_tour, shortest_distance = find_shortest_tour()

print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {shortest_distance}")