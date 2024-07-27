import math
from itertools import product

# City coordinates
city_coords = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
               (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
               (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Groups of cities
city_groups = [[1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate all-pairs distances
distances = {}
for i in range(len(city_coords)):
    for j in range(len(city_coords)):
        distances[(i, j)] = euclidean_distance(city_coords[i], city_coords[j])

# Generate all possible tours that visit one city from each group
def find_minimal_tour():
    min_tour = None
    min_cost = float('inf')
    
    # Iterate through all combinations by selecting one city from each group
    for group_selection in product(*city_groups):
        # Always include the depot (0) at the beginning and end
        tour = [0] + list(group_selection) + [0]
        # Calculate the total cost of this tour
        cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
        
        if cost < min_cost:
            min_cost = cost
            min_tour = tour
            
    return min_tour, min_cost

# Compute the optimal tour and its cost
optimal_tour, total_cost = find_minimal_tour()

# Output results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")