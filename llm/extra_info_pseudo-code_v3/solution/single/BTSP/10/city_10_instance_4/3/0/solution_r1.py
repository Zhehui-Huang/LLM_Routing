import math
from sys import maxsize

# Coordinates of each city (including the depot city 0)
coordinates = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Calculating Euclidean distances between each pair of cities
def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Generate all distances
distances = {}
n = len(coordinates)

for i in range(n):
    for j in range(i+1, n):
        if i != j:
            dist = calculate_distance(coordinates[i], coordinates[j])
            distances[(i, j)] = dist
            distances[(j, i)] = dist

# Attempting to find a feasible tour minimizing the max edge weight in the tour
def find_feasible_tour():
    # Generate a starting permutation
    best_max_edge = maxsize
    best_tour = None

    # Check all permutations of cities: 1, 2, ..., n-1 
    # (excluding the depot city 0, around which we will wrap the tour)
    for perm in permutations(range(1, n)):
        # Current permutation with start and end at the depot
        current_tour = (0,) + perm + (0,)
        
        # Calculate the max and total distance for this permutation
        cur_max_edge = 0
        total_distance = 0
        for i in range(len(current_tour) - 1):
            edge_dist = distances[(current_tour[i], current_tour[i+1])]
            total_distance += edge_dist
            if edge_dist > cur_max_edge:
                cur_max_edge = edge_dist
        
        # Update best tour if current max edge is the smallest found so far
        if cur_max_array < best_max_edge:
            best_max_edge = cur_max_edge
            best_tour = current_tour
            best_total_distance = total_distance
    
    return best_tour, best_total_distance, best_max_edge

# Finding the optimal tour
tour, tour_cost, max_distance = find_feasible_tour()

# Output results
print("Tour:", tour)
print("Total travel cost:", tour_cost)
print("Maximum distance between consecutive cities:", max_distance)