from itertools import permutations
import math

# Given cities and groups
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Function to calculate the Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Find the closest city from each group to the depot
closest_cities = []
for group in groups:
    min_distance = float('inf')
    chosen_city = None
    for city in group:
        dist = distance(0, city)
        if dist < min_distance:
            min_distance = dist
            chosen_city = city
    closest_cities.append(chosen_city)

# Generate all permutations of the chosen cities
min_tour_cost = float('inf')
best_tour = None
for perm in permutations(closest_cities):
    current_tour = [0] + list(perm) + [0]
    current_cost = sum(distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
    if current_cost < min_tour_cost:
        min_tour_cost = current_cost
        best_tour = current_tour

# Output the best tour found and its total cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_tour_cost:.2f}")