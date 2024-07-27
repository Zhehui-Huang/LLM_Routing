import itertools
import math

# City coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Euclidean distance function
def calculate_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate all city combinations  
all_combinations = itertools.combinations(range(1, 20), 12)  # All combinations of 12 cities out of 19

min_cost = float('inf')
best_tour = None

# Explore all combinations
for combination in all_combinations:
    full_tour = [0] + list(combination) + [0]  # Including depot city as start and end
    perm_tours = itertools.permutations(list(combination))  # Permutations of the cities
    
    for tour in perm_tours:
        tour_with_depot = [0] + list(tour) + [0]
        cost = sum(calculate_distance(tour_with_depot[i], tour_with_depot[i + 1]) for i in range(len(tour_with_depot) - 1))
        
        if cost < min_cost:
            min_cost = cost
            best_tour = tour_with_depot

# Print best tour found and its cost
print(f'Tour: {best_tour}')
print(f'Total travel cost: {min_cost}')