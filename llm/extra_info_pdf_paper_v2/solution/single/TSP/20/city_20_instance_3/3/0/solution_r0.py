import math
from itertools import permutations

# List of city coordinates, 0-indexed where city 0 is the depot
city_coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate total cost of the tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(tour[i - 1], tour[i])
    return total_cost

# Implementing a simple nearest neighbor heuristic
def nearest_neighbor_tour(start_city):
    unvisited = set(range(1, len(city_coordinates)))
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # return to the start city
    return tour

# Use first a simple nearest neighbor route to get a feasible solution
initial_tour = nearest_neighbor_tour(0)
initial_cost = calculate_total_cost(initial_tour)

# Perform 2-opt swaps to improve the tour
def two_opt(tour):
    best_cost = calculate_total_cost(tour)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = calculate_total_cost(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour[:]
                    best_cost = new_cost
                    improved = True
        tour = best_tour
    return best_tour, best_cost

# Optimize the initial tour with 2-opt
final_tour, final_cost = two_opt(initial_tour)

# Output the tour and the total cost
print("Tour:", final_tour)
print("Total travel cost:", final_cost)