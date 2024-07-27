import math
import itertools

# City coordinates
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
          (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
          (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

# Groups of cities
groups = [[7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], [1, 9, 14, 19], [5, 6, 17]]

# Function to calculate Euclidean distance
def euclidean_distance(idx1, idx2):
    x1, y1 = cities[idx1]
    x2, y2 = cities[idx2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Potential solution search using a simple combinatorial approach
def find_shortest_path():
    # Generate all combinations of cities, taking one from each group
    all_combinations = itertools.product(*groups)
    best_cost = float('inf')
    best_path = []

    # Traverse through all products of combinations
    for combination in all_combinations:
        # Start from the depot, visit one city from each group in order, and go back to the depot
        path = [0] + list(combination) + [0]
        cost = sum(euclidean_distance(path[i], path[i+1]) for i in range(len(path) - 1))
        
        if cost < best_cost:
            best_cost = cost
            best_path = path

    return best_path, best_cost

# Execute the solution finder
tour, total_cost = find_shortest_path()

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")