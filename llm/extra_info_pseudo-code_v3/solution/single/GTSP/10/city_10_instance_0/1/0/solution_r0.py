import itertools
import math

# City coordinates
coordinates = [
    (50, 42),  # Depot 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# City groups
groups = [
    [1, 2, 6],  # Group 0
    [3, 7, 8],  # Group 1
    [4, 5, 9]   # Group 2
]

# Calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Generate all possible tours that visit one city from each group and return to the depot
def find_shortest_tour():
    shortest_tour = None
    min_cost = float('inf')
    
    for selection in itertools.product(*groups):
        # Adding the depot city to the start and the end of the tour
        full_tour = [0] + list(selection) + [0]
        cost = sum(distance(full_tour[i], full_tour[i + 1]) for i in range(len(full_tour) - 1))
        
        if cost < min_cost:
            min_cost = cost
            shortest_tour = full_tour
    
    return shortest_tour, min_cost

# Finding and displaying the shortest tour
optimal_tour, total_cost = find_shortest_tour()
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")