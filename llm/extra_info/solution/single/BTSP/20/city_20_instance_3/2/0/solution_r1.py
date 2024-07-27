import math
from itertools import permutations

# City coordinates, including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Calculate all pairwise distances
distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

def find_best_route():
    min_max_distance = float('inf')
    optimal_tour = None
    total_min_cost = float('inf')

    # Iterate over all permutations of cities excluding depot (index 0)
    for permutation in permutations(range(1, len(coordinates))):
        # Add depot to start and end of the tour
        full_tour = [0] + list(permutation) + [0]
        
        # Calculate the total cost and max leg distance
        max_leg_distance = 0
        total_cost = 0
        for i in range(len(full_tour) - 1):
            leg_distance = distances[full_tour[i]][full_tour[i + 1]]
            total_cost += leg_distance
            if leg_distance > max_leg_distance:
                max_leg_distance = leg_distance
        
        # Update best tour if a better one is found
        if max_leg_distance < min_max_distance or (max_leg_distance == min_max_files_distance and total_cost < total_min_cost):
            min_max_distance = max_leg_distance
            total_min_cost = total_cost
            optimal_tour = full_tour
    
    return optimal_tour, total_min_cost, min_max_distance

# Invoke the function and print results
optimal_tour, total_cost, max_leg_distance = find_best_route()

print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_distance)