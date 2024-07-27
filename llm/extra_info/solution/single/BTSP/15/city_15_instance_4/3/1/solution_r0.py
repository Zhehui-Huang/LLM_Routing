import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_distances(cities):
    num_cities = len(cities)
    distances = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

def find_optimal_tour(cities):
    num_cities = len(cities)
    all_distances = calculate_distances(cities)
    
    # Try finding a tour manually that minimizes the max distance in each step (a greedy approach)
    tour = [0]
    unvisited = set(range(1, num_cities))
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: all_distances[last][x])
        unvisited.remove(next_city)
        tour.append(next_city)
    tour.append(0)  # return to the depot
    
    # Calculate total distance and maximum distance between consecutive cities
    total_cost = sum(all_distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(all_distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    return tour, total_cost, max_distance

# Define cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
    (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate the optimal tour
tour, total_cost, max_distance = find_optimal_tour(cities)

# Output the solution
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))