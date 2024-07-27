import math
from itertools import combinations

# Define the city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def euclidean_distance(city1, city2):
    return math.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

def compute_cost(tour):
    total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_cost

# Generate all combinations of 15 cities (excluding the depot)
city_combinations = combinations([i for i in range(1, 20)], 15)

min_cost = float('inf')
best_tour = None

for combo in city_combinations:
    # Tour starts and ends at the depot, includes the depot and 15 others
    full_tour = [0] + list(combo) + [0]
    current_cost = compute_cost(full_tour)
    
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = full_tour

# Output the results
print(f'Tour: {best_tour}')
print(f'Total travel cost: {min_cost}')