import math
from itertools import permutations

# City coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# City groups
groups = [
    [7, 10, 11, 12], 
    [3, 8, 13, 16], 
    [2, 4, 15, 18], 
    [1, 9, 14, 19], 
    [5, 6, 17]
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def total_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Generate all possible tours by selecting one city from each group
def generate_all_tours():
    all_group_combinations = []
    for prod in itertools.product(*groups):
        all_group_combinations.append(list(prod))
    all_tours = [[0] + list(comb) + [0] for comb in all_group_combinations]
    return all_tours

# Find the shortest tour
def find_shortest_tour():
    all_tours = generate_all_tours()
    best_tour = None
    min_cost = float('inf')
    
    for tour in all_tours:
        cost = total_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    
    return best_tour, min_cost

# Get the best tour and its cost
best_tour, best_tour_cost = find_shortest_tour()

print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)