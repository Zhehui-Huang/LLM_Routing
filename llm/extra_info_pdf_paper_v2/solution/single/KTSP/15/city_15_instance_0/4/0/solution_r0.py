from itertools import combinations
import math

# Define the city coordinates
cities = [
    (9, 93),   # Depot
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance between two points
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_tour_cost(tour):
    # Calculate the total cost of the given tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Find the best tour visiting exactly 4 cities including the depot
min_cost = float('inf')
best_tour = None

for combo in combinations(range(1, len(cities)), 3):
    tour = [0] + list(combo) + [0]  # Start and end at the depot
    cost = calculate_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)