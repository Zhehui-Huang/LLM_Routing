import math
import itertools

# Function to calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# All city coordinates
cities = {
    0: (16, 90), 1: (43, 99),  2: (80, 21),  3: (86, 92),  4: (54, 93),
    5: (34, 73), 6: (6, 61),   7: (86, 69),  8: (30, 50),  9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate the total cost of a tour
def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Finding the best tour using a greedy strategy plus all combinations for exactly 10 cities (including the depot)
min_cost = float('inf')
best_tour = None
all_combinations = itertools.combinations(range(1, 15), 9)  # Create combinations excluding the depot

for combo in all_combinations:
    tour = [0] + list(combo) + [0]  # Start and end at the depot
    total_cost = calculate_total_cost(tour, cities)
    
    if total_cost < min_cost:
        min_cost = total_cost
        best_tour = tour

# Output the best tour and the total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")