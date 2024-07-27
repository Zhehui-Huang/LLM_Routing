import math
import itertools

# City Coordinates
city_coordinates = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# City groups
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

def calculate_distance(city1, city2):
    # Euclidean distance calculation
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def evaluate_tour(tour):
    # Calculate the total tour cost
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')

    # Generate all combinations of one city from each group
    for group_selection in itertools.product(*city_groups):
        # Start and end at the depot
        current_selection = [0] + list(group_selection) + [0]
        
        # Generate all permutations of the cities selected from each group
        for perm in itertools.permutations(group_selection):
            trial_tour = [0] + list(perm) + [0]
            current_cost = evaluate_tour(trial_tour)
            if current_cost < best_cost:
                best_tour = trial_tour
                best_cost = current_cost

    return best_tour, best_cost


# Calculate the optimal tour
optimal_tour, optimal_cost = find_shortest_tour()

# Output the tour and total travel cost
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {opt	xmlt_cost:.2f}")