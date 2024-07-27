import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += distance_matrix[tour[i - 1]][tour[i]]
    total_distance += distance_matrix[tour[-1]][tour[0]]
    return total_distance

def two_opt(cities, distance_matrix):
    best_tour = list(range(len(cities)))
    best_distance = calculate_total_distance(best_tour, distance_matrix)

    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(cities) - 2):
            for j in range(i+1, len(cities)):
                if j-i == 1: 
                    continue
                new_tour = best_tour[:]
                new_tour[i:j] = best_tour[j-1:i-1:-1]
                new_distance = calculate_total_distance(new_tour, distance_matrix)
                if new_distance < best_distance:
                    best_tour = new_tour
                    best_distance = new_distance
                    improvement = True
    return best_tour, best_distance

# Cities defined by coordinates
cities = [
    (53, 68),  # Depot city
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# Calculate the distance matrix
n_cities = len(cities)
distance_matrix = [[0]*n_cities for _ in range(n_cities)]
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Find the optimal tour with 2-opt
optimal_tour, optimal_cost = two_opt(cities, distance_matrix)
optimal_tour.append(optimal_tour[0])  # completing the tour by returning to the depot

# Output result
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)