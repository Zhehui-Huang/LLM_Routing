import math
from itertools import combinations, permutations

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate distance matrix
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(i, j)

# Function to compute the tour cost
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    return cost

# Generate candidate tours using subset selection and permutation
def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    # Select 9 cities in combination with the depot
    for cities_subset in combinations(range(1, n), 9):
        full_tour = [0] + list(cities_subset) + [0]
        # Generate all permutations of the selected cities
        for perm in permutations(cities_subset):
            candidate_tour = [0] + list(perm) + [0]
            # Calculate the tour cost
            current_cost = tour_cost(candidate_tour)
            # Check and update best tour found
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = candidate_tour
    return best_tour, best_cost

# Find the shortest tour using the heuristic
best_tour, best_cost = find_shortest_tour()

# Printing the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))