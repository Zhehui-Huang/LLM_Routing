import numpy as np
import itertools
import random

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Compute distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
    return dist_matrix

dist_matrix = calculate_distance_matrix(cities)

def find_best_tour(dist_matrix, k=13):
    num_cities = len(dist_matrix)
    min_tour_cost = float('inf')
    min_tour = []
    
    # Explore multiple random starts to increase chance of getting closer to optimal solution
    for _ in range(100):  # Example: 100 multi-start iterations
        # Randomly select k-1 cities to visit (not including the depot city)
        selected_cities = random.sample(range(1, num_cities), k-1)
        selected_cities = [0] + selected_cities  # Include depot city
        
        # Generate all permutations of selected cities and compute the tour cost
        for permutation in itertools.permutations(selected_cities):
            # Ensuring to start and end at depot
            current_tour = list(permutation) + [0]
            tour_cost = sum(dist_matrix[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour)-1))
            
            if tour_cost < min_tour_cost:
                min_tour_cost = tour_cost
                min_tour = current_tour
                
    return min_tour, min_tour_cost

# Calculate the best tour and its cost
tour, tour_cost = find_best_tour(dist_matrix, 13)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost:.2f}")