import math
from itertools import product

# City details
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# City groups
city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Function to calculate the Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate all permutations of selecting one city from each group
selected_permutations = list(product(*city_groups))

# Calculate the shortest route that visits one city from each group and returns to the depot
min_cost = float('inf')
best_tour = None

for perm in selected_permutations:
    # Calculate the cost of the route starting and ending at the depot
    route = [0] + list(perm) + [0]
    cost = sum(calc_distance(route[i], route[i + 1]) for i in range(len(route) - 1))
    
    if cost < min_cost:
        min_cost = cost
        best_tour = route

# Output the best route and its total travel cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))