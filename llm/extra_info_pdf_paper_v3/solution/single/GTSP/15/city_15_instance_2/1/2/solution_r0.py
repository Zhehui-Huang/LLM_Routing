import math
from itertools import product

# Define the city coordinates and city groups
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible tours that visit one city from each group
possible_tours = product(*city_groups)

min_cost = float('inf')
optimal_tour = []

# Calculate the travel cost for each tour and find the minimum
for tour in possible_tours:
    tour = [0] + list(tour) + [0]  # Start and end at the depot city 0
    cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    if cost < min_permission_cost:
        min_cost = cost
        optimal_tour = tour

# Output solution
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {min_cost:.2f}")