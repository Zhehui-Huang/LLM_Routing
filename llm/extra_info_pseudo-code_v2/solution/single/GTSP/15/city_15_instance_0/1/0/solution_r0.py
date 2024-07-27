import itertools
import math

# Position coordinates of cities
cities = {
    0: (9, 93),   # Depot city
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

# Groups of cities
city_groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Function to calculate Euclidean distance between two points
def euclidean_distance(a, b):
    ax, ay = cities[a]
    bx, by = cities[b]
    return math.sqrt((ax - bx)**2 + (ay - by)**2)

# Function to calculate total tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(tour[i-1], tour[i])
    return total_cost

# Get all combinations of visiting one city from each group
potential_combinations = list(itertools.product(city_groups[0], city_groups[1], city_groups[2]))

# Finding the shortest tour
best_tour = None
min_cost = float('inf')

for combination in potential_combinations:
    all_tours = itertools.permutations(combination)
    for tour in all_tours:
        tour_with_depot = [0] + list(tour) + [0]
        tour_cost = calculate_tour_cost(tour_with_depot)
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = tour_with_depot

# Output the tour and the total travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)