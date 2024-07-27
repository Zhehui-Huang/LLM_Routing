import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
          (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
          (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
          (50, 28), (69, 9)]

# Groups of cities
groups = [
    [5, 6, 7, 11, 17],  # Group 0
    [1, 4, 8, 13, 16],  # Group 1
    [2, 10, 15, 18, 19],  # Group 2
    [3, 9, 12, 14]  # Group 3
]

def solve_gtsp(cities, groups):
    best_tour = None
    min_cost = float('inf')
    
    # Permute group representatives (one from each group)
    for perm in permutations([0, 1, 2, 3]):
        for representative_0 in groups[perm[0]]:
            for representative_1 in groups[perm[1]]:
                for representative_2 in groups[perm[2]]:
                    for representative_3 in groups[perm[3]]:
                        tour = [0, representative_0, representative_1, representative_2, representative_3, 0]
                        cost = 0
                        for i in range(len(tour) - 1):
                            cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
                        
                        if cost < min_cost:
                            min_cost = cost
                            best_tour = tour
    
    return best_tour, min_cost

# Find the best tour and its cost
best_tour, min_cost = solve_gtsp(cities, groups)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))