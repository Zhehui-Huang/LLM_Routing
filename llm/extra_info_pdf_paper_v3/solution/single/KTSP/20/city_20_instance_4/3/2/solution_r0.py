import numpy as np
import itertools

# City coordinates
city_positions = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

n = len(city_positions)  # total cities
k = 16  # cities to be visited including the depot

# Calculate distances
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i, j] = np.linalg.norm(np.array(city_positions[i]) - np.array(city_positions[j]))

# Heuristic to select k cities (here we select the 15 nearest cities to the depot plus the depot itself)
distances_from_depot = list(enumerate(distances[0][1:], start=1))
selected_cities = sorted(distances_from_depot, key=lambda x: x[1])[:k-1]
selected_cities = [0] + [city[0] for city in selected_cities]  # include depot 

# Greedy algorithm to create an initial tour by next nearest neighbor
def nearest_neighbor_tour(start_city, selected_cities):
    unvisited = set(selected_cities)
    tour = [start_city]
    unvisited.remove(start_city)
    
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        unvisited.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    
    return tour + [start_city]  # return to the starting city

initial_tour = nearest_neighbor_tour(0, selected_cities)

# 2-opt heuristic to improve the tour
def two_opt(tour):
    best_tour = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if distances[tour[i - 1]][tour[j]] + distances[tour[i]][tour[j + 1]] < \
                   distances[tour[i - 1]][tour[i]] + distances[tour[j]][tour[j + 1]]:
                    best_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                    improved = True
        tour = best_tour
    return best_tour

optimized_tour = two_opt(initial_tour)

# Calculate the total cost of the tour
total_cost = sum(distances[optimized_tour[i]][optimized_tour[i + 1]] for i in range(len(optimized_tour) - 1))

# Output
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)