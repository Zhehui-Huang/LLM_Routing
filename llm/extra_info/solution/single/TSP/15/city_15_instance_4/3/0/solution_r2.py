import math
from itertools import permutations

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46),
    6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# All cities except the depot
non_depot_cities = list(cities.keys())[1:]

# Generate all possible tours considering the robot must return to the depot
best_tour = None
min_cost = float('inf')

for perm in permutations(non_depot_cities):
    current_cost = 0
    current_tour = [0] + list(perm) + [0]  # Start and end at the depot
    
    for i in range(len(current_tour) - 1):
        current_cost += distance(current_tour[i], current_tour[i + 1])
    
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = current_tour

# Output the best tour and the corresponding travel cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))