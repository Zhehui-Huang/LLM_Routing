import math

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# City groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate Euclidean distances
def distance(city1, city2):
    x_diff = cities[city1][0] - cities[city2][0]
    y_diff = cities[city1][1] - cities[city2][1]
    return math.sqrt(x_diff**2 + y_diff**2)

# Generate all possible valid tours (one city from each group + depot city at start and end)
def generate_tours():
    from itertools import product
    all_combinations = list(product(*groups))
    return [[0] + list(comb) + [0] for comb in all_combinations]

# Calculate the total tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i+1])
    return total_cost

# Search for the shortest tour
def find_shortest_tour():
    all_tours = generate_tours()
    min_cost = float('inf')
    best_tour = None
    for tour in all_tours:
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

best_tour, min_cost = find_shortest_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")