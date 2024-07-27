import math
from itertools import permutations

# City Coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Groups
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

def euclidean_distance(city1, city2):
    return math.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Calculate all possible tours from one city from each group plus the depot
def find_optimal_tour():
    min_tour = None
    min_cost = float('inf')
    
    for city1 in groups[0]:
        for city2 in groups[1]:
            for city3 in groups[2]:
                permutation_cost = {}
                
                for tour in permutations([city1, city2, city3]):
                    candidates = [0] + list(tour) + [0]
                    cost = sum(euclidean_distance(candidates[i], candidates[i+1]) for i in range(len(candidates) - 1))
                    
                    if cost < min_cost:
                        min_cost = cost
                        min_tour = candidates
                
    return min_tour, min_cost

# Finding the optimal tour among options
optimal_tour, total_cost = find_optimal_tour()

# Output the optimal tour and it's cost
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))