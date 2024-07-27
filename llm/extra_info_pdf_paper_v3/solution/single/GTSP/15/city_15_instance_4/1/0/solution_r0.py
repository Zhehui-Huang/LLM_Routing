from itertools import permutations
import math

# City coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# City groups
groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Heuristic: Evaluate all permutations of choosing one city from each group
def find_shortest_tour(groups, depot):
    min_distance = float('inf')
    best_tour = None

    for combination in permutations([g[0] for g in groups]):  # Simple heuristic: Only picking the first city from each group
        tour = [depot] + list(combination) + [depot]
        distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        
        if distance < min_distance:
            min_distance = distance
            best_tour = tour
    
    return best_tour, min_distance

# Calculate the optimal tour and distance
tour, total_cost = find_shortest_tour(groups, 0)

# Outputs
print("Tour:", tour)
print("Total travel cost:", total_cost)