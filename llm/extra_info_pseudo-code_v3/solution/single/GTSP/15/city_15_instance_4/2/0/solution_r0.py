import math
import itertools

# City coordinates with City 0 as the depot
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
    14: (12, 39),
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

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all possible tours by choosing one city from each group
def generate_tours():
    all_group_permutations = list(itertools.product(*groups))
    best_tour = None
    min_distance = float('inf')
    
    for permutation in all_group_permutations:
        # Construct the tour: start at depot, visit one city from each group, return to depot
        current_tour = [0] + list(permutation) + [0]
        # Calculate total travel cost
        total_cost = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
        
        if total_qcost < min_distance:
            min_distance = total_cost
            best_tour = current_tour
            
    return best_tour, min_distance

# Getting the best tour and its cost
tour, total_cost = generate_tours()

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)