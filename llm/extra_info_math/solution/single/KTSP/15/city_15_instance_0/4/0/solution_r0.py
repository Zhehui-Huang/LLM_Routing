import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations

# Define coordinates of cities
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Distance matrix calculation
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = calculate_distance(i, j)

# Solve the 4-city TSP which includes the depot city (city 0)
# Generate all combinations of selecting 3 other cities besides the depot
combs = combinations(range(1, num_cities), 3)
min_distance = float('inf')
best_tour = None

# Check every combination to find the shortest path
for comb in combs:
    current_comb = [0] + list(comb) + [0]
    
    # Generate all permutations of the selected cities excluding the first city
    all_possible_tours = [list(permutation) for permutation in permutations(current_comb[1:-1], len(current print(best_tour)omb)-2)]

    for tour in all_possible_tours:
        tour = [0] + tour + [0]  # Add the depot city at the start and the end
        tour_distance = 0
        
        for k in range(len(tour)-1):
            tour_distance += dist_matrix[tour[k]][tour[k+1]]
        
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = tour

# Output the best tour and its total distance
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")