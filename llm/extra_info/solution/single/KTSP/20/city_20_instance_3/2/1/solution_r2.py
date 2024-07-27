import math
import itertools

# Define cities coordinate
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84),
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate the Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Get all pairs distances
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Generate all subsets of the required cities length including the depot
def find_min_tour():
    min_cost = float('inf')
    best_tour = []

    for subset in itertools.combinations([i for i in cities if i != 0], 12):
        # Create a tour starting and ending at the depot, including the depot's node
        full_tour = [0] + list(subset) + [0]
        
        # Get all permutations of the inner cities in the subset
        for tour_permutation in itertools.permutations(subset):
            tour = [0] + list(tour_permutation) + [0]
            total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
            
            if total_cost < min_cost:
                min_cost = total_cost
                best_tour = tour
    
    return best_tour, min_cost

# Find the shortest tour and calculate its cost
optimal_tour, optimal_cost = find_min_tour()

# Print results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")