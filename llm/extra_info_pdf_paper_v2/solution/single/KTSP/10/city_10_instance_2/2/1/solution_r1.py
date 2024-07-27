import math
from itertools import permutations
from itertools import combinations

# Coordinates of the cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Precompute distances between all pairs of cities
dist_matrix = {}
for i in cities:
    for j in cities:
        if i not in dist_matrix:
            dist_matrix[i] = {}
        dist_matrix[i][j] = distance(cities[i], cities[j])

# Select 6 cities including the depot (0), attempt to find the shortest tour by permutations
def find_shortest_tour():
    min_tour = None
    min_cost = float('inf')

    # Generate all combinations of 5 other cities (since city 0 is fixed in the route)
    for combo in combinations(range(1, 10), 5):
        current_perm = [0] + list(combo)
        # Permute the current combination to find the shortest path
        for perm in permutations(current_perm[1:]):
            tour = [0] + list(perm) + [0]  # Start and end at depot
            cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            if cost < min_cost:
                min_cost = cost
                min_tour = tour
    
    return min_tour, min_cost

# Find the optimal tour with minimum cost for the robot
optimal_tour, total_cost = find_shortest_tour()

# Output the tour and the cost
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))