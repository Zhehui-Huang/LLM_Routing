import numpy as np
import itertools
import random

def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Find the shortest route that involves visiting exactly k cities starting and ending at the depot
def shortest_tour(cities, k):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    
    # Calculate the full distance matrix
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = calculate_distance(cities[i], cities[j])

    # Initialize a random tour including the depot
    tour = [0] + random.sample(range(1, n), k - 1)
    tour.append(0) # Return to the depot
    min_distance = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    best_tour = tour[:]
    
    # Use a simple approach to optimize: swap within tour and check if the distance improves
    improved = True
    while improved:
        improved = False
        for i in range(1, k - 1):  # Exclude the depot when swapping
            for j in range(i + 1, k):
                new_tour = best_tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                new_distance = sum(distance_matrix[new_tour[i]][new_tour[i+1]] for i in range(len(new_tour)-1))
                if new_distance < min_distance:
                    min_distance = new_distance
                    best_tour = new_tour
                    improved = True
                    
    return best_tour, min_distance

# Main execution
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

k = 10  # Including the depot
best_tour, min_distance = shortest_t-problemour(cities, k)

# Output the solution
print("Tour:", best_tour)
print("Total travel cost:", round(min_distance, 2))