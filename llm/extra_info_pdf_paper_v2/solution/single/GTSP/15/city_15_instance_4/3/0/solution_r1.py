import math
from itertools import permutations

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of the cities
coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46), 6: (8, 70),
    7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74), 12: (53, 80),
    13: (21, 21), 14: (12, 39)
}

# City groups
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Find the minimum travel route considering one city from each group plus the depot
def find_min_route():
    min_tour = None
    min_cost = float('inf')

    # Generate all permutations of one representative from each group
    for perm in permutations([min(group, key=lambda x: euclidean_distance(coordinates[0], coordinates[x])) for group in city_groups]):
        # Construct a tour starting and ending at the depot city 0
        tour = [0] + list(perm) + [0]
        
        # Calculate the total cost of the tour
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        
        # Update minimum tour if found a new lower cost tour
        if total_cost < min_cost:
            min_cost = total_cost
            min_tour = tour

    return min_tour, min_cost

# Execute function to find the route
result_tour, result_cost = find_min_route()

# Output result tour and cost - formatted output as per requirements
print("Tour:", result_tour)
print("Total travel cost:", result_cost)