import numpy as np
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76),
}

# Number of cities to visit including the depot
k = 7

# Calculate distances between each pair of cities
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Distance matrix
distances = np.zeros((len(cities), len(cities)))
for i in cities:
    for j in cities:
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Heuristic: Greedy Algorithm for simplicity (not optimal for larger problems)
def find_shortest_tour():
    min_tour = None
    min_cost = float('inf')
    
    # Generate all subsets of k cities including the depot
    for subset in permutations(list(cities.keys())[1:], k-1):
        # Always include the depot at the beginning
        tour = [0] + list(subset)[:k-2]  # k-2 because depot is already included
        tour.append(0)  # Return to depot
        
        # Calculate the cost of this tour
        cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        # Check if this tour is the shortest found so far
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
    
    return min_tour, min_cost

# Execute the heuristic search
tour, total_cost = find_shortest_tour()

# Output the results as specified
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")