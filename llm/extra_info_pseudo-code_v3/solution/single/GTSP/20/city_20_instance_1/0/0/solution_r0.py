import math
from itertools import product

# City and groups data
depot = (14, 77)
cities = [
    (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), 
    (98, 76), (6, 19), (26, 29), (49, 23), (78, 76), 
    (68, 45), (50, 28), (69, 9), (21, 79), (69, 9)
]
city_groups = [
    [5, 6, 7, 11, 17], [1, 4, 8, 13, 16], [2, 10, 15, 18, 19], [3, 9, 12, 14]
]

# Calculate distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Precompute all distances for efficiency
all_distances = {}
for i in range(len(cities)):
    for j in range(i, len(cities)):
        d = distance(cities[i], cities[j])
        all_distances[(i+1, j+1)] = d
        all_distances[(j+1, i+1)] = d

# Initial configuration: very high cost
min_cost = float('inf')
best_tour = []

# Generate all combinations to explore
for combination in product(*city_groups):
    # Calculate the cost of the full tour: depot -> city from each group -> depot
    tour = [0] + list(combination) + [0]
    cost = 0
    for k in range(len(tour) - 1):
        if tour[k] == 0 or tour[k+1] == 0:  # depot to a city
            city_coords = cities[tour[k+1]-1] if tour[k+1] != 0 else cities[tour[k]-1]
            depot_to_city = distance(depot, city_coords)
            cost += depot_to_city
        else:  # city to city
            cost += all_distances[(tour[k], tour[k+1])]
    
    # If the found cost is lesser, update the best tour and min cost
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the shortest tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)