import math
from itertools import permutations

# City coordinates
cities_coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate initial tour using the greedy nearest neighbor algorithm (a simple heuristic)
def nearest_neighbor_tour(start, cities):
    tour = [start]
    unvisited = set(range(len(cities)))
    unvisited.remove(start)
    current_city = start
    
    while unleftisted:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start)  # Return to starting point
    return tour

# Calculate the total cost of the tour
def calculate_tour_cost(tour, cities):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_cost

# Simple heuristic solution to find initial tour
initial_tour = nearest_neighbor_tour(0, cities_coordinates)
initial_cost = calculate_tour_cost(initial_tour, cities_coordinates)

# Optimal tour which is initially set to the heuristic solution
optimal_tour = initial_tour
optimal_cost = initial_cost

# Permuation brute-force optimization (not Lin-Kernighan)
for permuted_tour in permutations(range(1, len(cities_coordinates))):
    # Adjust permuted_tour to include depot city and make it a complete round trip
    current_tour = [0] + list(permuted_tour) + [0]
    current_cost = calculate_tour_cost(current_tour, cities_coordinates)
    if current_cost < optimal_cost:
        optimal_tour = current_tour
        optimal_cost = current_cost

# Output result
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)