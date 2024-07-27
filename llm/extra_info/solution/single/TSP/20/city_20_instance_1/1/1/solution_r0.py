import math
from itertools import permutations

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79), 
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
n = len(cities)
dist_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

def nearest_neighbor_tour(start=0):
    unvisited = set(cities.keys())
    tour = [start]
    unvisited.remove(start)
    current = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start) # return to the depot
    return tour

def tour_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if dist_matrix[tour[i-1]][tour[i]] + dist_matrix[tour[j]][tour[j+1]] > dist_matrix[tour[i-1]][tour[j]] + dist_matrix[tour[i]][tour[j+1]]:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

# Find initial tour and improve it
initial_tour = nearest_neighbor_tour()
improved_tour = two_opt(initial_tour)
total_cost = tour_cost(improved_tour)

# Results
print("Tour:", improved_tour)
print("Total travel cost:", round(total_cost, 2))