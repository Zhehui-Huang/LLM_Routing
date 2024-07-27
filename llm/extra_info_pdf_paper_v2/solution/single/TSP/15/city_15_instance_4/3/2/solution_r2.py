import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city2][0] - cities[city1][0])**2 + (cities[city2][1] - cities[city1][1])**2)

# Compute all distances between cities
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean-map(cities)
ro_distance(i, j)

# Function to find the shortest tour using a simple heuristic approach
def find_shortest_tour():
    # Initialize with a high minimum cost and no tour
    min_cost = float('inf')
    best_tour = None
    
    # Generate all permutations of city indices except the depot city 0
    for perm in permutations(range(1, num_cities)):
        # Calculate total travel cost for the current permutation
        cost = distances[0][perm[0]]  # Start from depot to first city in permutation
        for i in range(len(perm) - 1):
            cost += distances[perm[i]][perm[i + 1]]  # Sum of distances between cities in permutation
        cost += distances[perm[-1]][0]  # Return from last city in permutation to depot
        
        # Check if the current permutation yields a lower cost than the previous minimum
        if cost < min_cost:
            min_cost = cost
            best_tour = [0] + list(perm) + [0]  # Construct the complete tour
    
    return best_tour, min_cost

# Calculate and print the shortest tour and its cost
tour, total_cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)