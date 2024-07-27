import math
from itertools import product

# Define coordinates for each city, including the depot
coordinates = [
    (29, 51), # Depot
    (49, 20), # City 1
    (79, 69), # City 2
    (17, 20), # City 3
    (18, 61), # City 4
    (40, 57), # City 5
    (57, 30), # City 6
    (36, 12), # City 7
    (93, 43), # City 8
    (17, 36), # City 9
    (4, 60),  # City 10
    (78, 82), # City 11
    (83, 96), # City 12
    (60, 50), # City 13
    (98, 1)   # City 14
]

# Define the groups, each list contains indices of cities in the group
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Calculate the shortest cycle visiting one city from each group starting and ending at the depot
def find_shortest_tour():
    min_tour = None
    min_cost = float('inf')
    
    # Generate all permutations of one city from each group
    for scenario in product(*groups):
        # Include the depot city at the start and end
        complete_tour = [0] + list(scenario) + [0]
        
        # Compute the travel cost of the tour
        cost = sum(euclidean_distance(complete_tour[i], complete_tour[i + 1]) for i in range(len(complete_tour) - 1))
        
        if cost < min_cost:
            min_cost = cost
            min_tour = complete_tour
            
    return min_tour, min_cost

# Result
tour, total_cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)