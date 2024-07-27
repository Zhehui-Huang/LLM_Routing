import itertools
import math

# Define the coordinates of the cities including the depot
city_coordinates = [
    (53, 68),  # Depot City 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Define the groups of cities
city_groups = [
    [5, 6, 7],  # Group 0
    [2, 3],     # Group 1
    [1, 9],     # Group 2
    [4, 8]      # Group 3
]

def euclidean_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 + 
                     (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

# Calculate all pairwise distances
distances = {}
for i in range(len(city_coordinates)):
    for j in range(len(city_coordinates)):
        distances[(i, j)] = euclidean_distance(i, j)

def find_minimum_tour():
    # Generate all possible combinations of cities taking one from each group
    all_combinations = list(itertools.product(*city_groups))
    
    min_tour = None
    min_cost = float('inf')
    
    # Test every combination
    for combination in all_combinations:
        # All permutations of the selected cities from groups
        for perm in itertools.permutations(combination):
            # Include the depot in the beginning and end
            tour = [0] + list(perm) + [0]
            # Calculate the cost of this tour
            cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
            # Update minimum tour if this one is better
            if cost < min_cost:
                min_cost = cost
                min_tour = tour
    
    return min_tour, min_cost

# Calculate the minimum tour and its cost
optimal_tour, total_cost = find_minimum_tour()

# Output the results as required
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)