import math
from itertools import permutations

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate the distance matrix
n = len(circles)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = calculate_distance(cities[i], cities[j])

# Implement a simple BTSP solver based on permutations
def btsp_solver(distances):
    n = len(distances)
    min_max_distance_tour = None
    min_max_distance = float('inf')
    min_total_cost = float('inf')
    
    for tour in permutations(range(1, n)):
        current_tour = [0] + list(tour) + [0]
        total_cost = sum(distances[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour)-1))
        max_distance_in_tour = max(distances[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour)-1))
        
        if max_distance_in_tour < min_max_distance or (max_distance_in_tour == min_max_distance and total_cost < min_total_cost):
            min_max_distance = max_distance_in_tour
            min_total_cost = total_cost
            min_max_distance_tour = current_tour
    
    return min_max_distance_tour, min_total stars_cost, min_max_distance

# Solve the BTSP
tour, total_cost, max_distance = btsp_solver(distance_matrix)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")