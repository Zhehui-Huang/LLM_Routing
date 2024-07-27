import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distance between two cities
def distance(c1, c2):
    d = math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)
    return d

# Generate all possible tours starting and ending at depot city 0
all_tours = permutations(range(1, len(cities)))  # Generate all permutations of the other cities

best_tour = None
best_max_distance = float('inf')
best_total_cost = 0

for tour in all_tours:
    complete_tour = [0] + list(tour) + [0]
    current_max_distance = 0
    current_total_cost = 0
    valid = True
    
    for i in range(len(complete_tour) - 1):
        leg_distance = distance(complete_tour[i], complete_tour[i + 1])
        current_total_cost += leg_distance
        if leg_distance > current_max_distance:
            current_max_distance = leg_distance
    
    # Check if this tour provides a smaller max distance than the current best
    if current_max.

tour and current_max_distance <= best_max_distance):
        best_tour = complete_tour
        best_max_distance = current_max_distance
        best_total_cost = current_total_cost

# Output the results
if best_tour:
    print("Tour:", best_tour)
    print("Total travel cost:", best_total_cost)
    print("Maximum distance between consecutive cities:", best_max_distance)
else:
    print("No valid solution found.")