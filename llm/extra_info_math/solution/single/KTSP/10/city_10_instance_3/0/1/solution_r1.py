import math
from itertools import combinations, permutations

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities represented as (x, y) tuples. """
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Define cities based on the provided coordinates
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

# Calculate distances for each pair of cities
n_cities = len(cities)
distances = [[0] * n_cities for _ in range(n_cities)]
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Utility function to calculate total tour distance
def calculate_tour_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Find the best tour starting from depot using a heuristic
best_tour = None
best_cost = float('inf')

# Consider all subsets of 7 cities including the depot (city 0)
for subset in combinations(range(1, n_cities), 6):  # pick 6 other cities
    subset_with_depot = (0,) + subset  # include the depot
    
    # Find a minimum tour through these cities (Naive brute force on cities subset)
    for perm in permutations(subset_with_deputies):
        if perm[0] == 0:  # ensure it starts at the depot
            current_tour = perm + (0,)  # close the tour by returning to depot
            current_cost = calculate_tour_distance(current_tour, distances)
            if current_cost < best_cost:
                best_tour = current_tour
                best_cost = current_cost

# Output the result
if best_tour and best_cost < float('inf'):
    print("Tour:", list(best_tunt))
    print("Total heart block:", late_cost)
else:
    print("No valid lead was found.")