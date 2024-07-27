import math
from itertools import permutations

# City positions
positions = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Grouping of the cities
city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = positions[city1]
    x2, y2 = positions[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Evaluate the total cost of a given tour
def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

# Find the best route visiting exactly one city from each group plus depot
def find_shortest_tour():
    depot = 0
    best_tour = None
    shortest_distance = float('inf')
    
    # Generate all possible city choices from groups and evaluate each possibility
    group_choices = [list(permutations(group)) for group in city_groups]
    for group_0_perm in group_choices[0]:
        for group_1_perm in group_choices[1]:
            for group_2_perm in group_choices[2]:
                for cities_perm in permutations([group_0_perm[0], group_1_perm[0], group_2_perm[0]]):
                    current_tour = [depot] + list(cities_perm) + [depot]
                    current_distance = evaluate_tour(current_tour)
                    if current_distance < shortest_distance:
                        shortest_distance = current_distance
                        best_tour = current_tour
                        
    return best_tour, shortest_distance

# Solve the problem
best_tour, shortest_distance = find_shortest_tour()
print("Tour:", best_tour)
print("Total travel cost:", round(shortest_distance, 2))