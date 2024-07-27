import numpy as np
import random

# Utilizing numpy for calculating Euclidean distance
def euclidean_distance(p1, p2):
    return np.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Implementing the nearest neighbor heuristic
def nearest_neighbor_tour(start_city, cities, distance_matrix):
    unvisited = set(cities)
    tour = [start_city]
    unvisited.remove(start_city)
    
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
        
    tour.append(start_city) # Return to the depot
    return tour

# Implementing 2-opt optimization
def two_opt(tour, distance_matrix):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i+2, len(tour) - 1):
                if (distance_matrix[tour[i]][tour[i-1]] + distance_matrix[tour[j+1]][tour[j]] >
                    distance_matrix[tour[i]][tour[j+1]] + distance_matrix[tour[j]][tour[i-1]]):
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improvement = True
    return tour

# Calculate total tour cost
def calculate_total_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

def solve_k_tsp(cities_coordinates, k=16):
    num_cities = len(cities_coordinates)
    distance_matrix = [[euclidean_distance(cities_coordinates[i], cities_coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]
    
    # Selecting random 15 cities plus the depot city 0
    selected_cities = random.sample(range(1, num_cities), k-1)
    selected_cities.append(0)  # Include the depot
    
    # Initialize a random tour with the nearest neighbor heuristic
    initial_tour = nearest_neighbor_tour(0, selected_cities, distance_matrix)
    
    # Optimize tour using the 2-opt heuristic
    optimized_tour = two_opt(initial_tour, distance_matrix)
    
    # Calculate the cost of the optimized tour
    total_cost = calculate_total_cost(optimized_tour, distance_matrix)
    
    return optimized_tour, total_cost

# Example coordinates as per given data
cities_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Solving the problem
tour, total_cost = solve_k_tsp(cities_coordinates)

print("Tour:", tour)
print("Total travel cost:", total_cost)