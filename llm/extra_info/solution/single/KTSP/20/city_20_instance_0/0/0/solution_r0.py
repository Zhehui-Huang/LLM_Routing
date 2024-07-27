import itertools
import math

# Define city coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all combinations of 3 cities excluding the depot city
combinations = itertools.combinations(range(1, 20), 3)

# Variables to track the best tour
min_cost = float('inf')
best_tour = None

# Test each combination to find the minimum cost tour
for combo in combinations:
    # Calculate the tour: depot -> city1 -> city2 -> city3 -> depot
    tour = [0] + list(combo) + [0]
    
    # Calculate total cost for this tour
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(tour[i], tour[i+1])
    
    # Check if this tour has a lower cost than the current best
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour found and its total cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(min_cost, 2)}")