import math
from itertools import permutations

# Define the cities coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def euclidean_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost
    
min_cost = float('inf')
best_tour = []

# Consider all combinations of 3 cities (besides depot city) from the available cities.
for combo in permutations(range(1, 15), 3):
    current_tour = [0] + list(combo) + [0]  # 0 is the depot city
    current_cost = calculate_tour_cost(current_tour)
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = current_tour

print("Tour:", best_tour)
print("Total travel cost:", min_cost)