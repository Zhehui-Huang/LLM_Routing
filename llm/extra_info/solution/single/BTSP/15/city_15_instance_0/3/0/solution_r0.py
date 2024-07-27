import math
import itertools

# Coordinates of each city including the depot
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), 
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

def euclidean_distance(p1, p2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Construct a distance matrix
num_cities = len(cities)
dist_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Find the tour minimizing the maximum distance between consecutive cities
def find_minmax_tour():
    best_tour = None
    min_max_distance = float('inf')
    total_best_cost = float('inf')
    
    # Attempting to solve using permutations (feasible for small number of cities like 15)
    # In practice, use better methods or heuristics for larger problems
    for perm in itertools.permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        max_distance = 0
        total_cost = 0
        
        for i in range(len(tour) - 1):
            dist = dist_matrix[tour[i]][tour[i + 1]]
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        
        if max_distance < min_maxspece or (max_distance == min_max_distance and total_cost < total_best_cost):
            min_max_distance = max_distance
            best_tour = tour
            total_best_cost = total_cost
    
    return best_tour, total_best_cost, min_max_distance

# Use the function to find the best tour
tour, total_cost, max_distance = find_minmax_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")