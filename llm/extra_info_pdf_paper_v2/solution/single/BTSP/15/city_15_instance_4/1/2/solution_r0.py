import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def compute_all_distances(cities):
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

def find_min_max_tour(cities):
    n = len(cities)
    all_distances = compute_all_distances(cities)
    best_max_distance = float('inf')
    best_tour = None
    best_total_cost = float('inf')

    for perm in permutations(range(1, n)):
        current_tour = [0] + list(perm) + [0]
        max_distance = 0 
        total_cost = 0
        
        for i in range(len(current_tour)-1):
            d = all_distances[current_tour[i]][current_tour[i+1]]
            total_cost += d
            if d > max_distance:
                max_distance = d

        if max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < best_total_cost):
            best_max_distance = max_distance
            best_tour = current_tour
            best_total_cost = total_cost
    
    return best_tour, best_total_cost, best_max_distance

cities = [
    (35, 40), (39, 41), (81, 30), (5, 50),
    (72, 90), (54, 46), (8, 70), (97, 62),
    (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

best_tour, best_total_cost, best_max_distance = find_min_max_tour(cities)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")