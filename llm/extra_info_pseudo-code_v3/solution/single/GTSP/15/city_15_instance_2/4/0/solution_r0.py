import math
from itertools import product

# City coordinates
city_coords = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Groups of cities
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of tours
min_tour_cost = float('inf')
best_tour = []

for tour in product(*groups):
    full_tour = [0] + list(tour) + [0]
    total_cost = sum(distance(full_tour[i], full_tour[i + 1]) for i in range(len(full_tour) - 1))
    
    if total_cost < min_tour_cost:
        min_tour_cost = total_cost
        best_tour = full_tour

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", round(min_tour_cost, 2))