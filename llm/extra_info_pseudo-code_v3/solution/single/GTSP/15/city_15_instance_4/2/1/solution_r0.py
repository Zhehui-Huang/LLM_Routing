import itertools
import math

# City coordinates indexed by city number
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Groups of cities
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Generate all possible tours by choosing one city from each group
all_possible_tours = itertools.product(*groups)

# Evaluate all possible tours starting and ending at the depot city (0)
best_tour = None
min_cost = float('inf')
for partial_tour in all_possible_tours:
    complete_tour = [0] + list(partial_tour) + [0]
    tour_cost = calculate_tour_cost(complete_tour)
    if tour_cost < min_cost:
        min_cost = tour_cost
        best_tour = complete_tour

# Output the best tour found and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)