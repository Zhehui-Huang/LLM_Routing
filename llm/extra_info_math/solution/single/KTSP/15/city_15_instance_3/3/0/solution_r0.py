import math
import random

# Define cities coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

def generate_random_tour(depot, num_cities, total_cities):
    tour = [depot] + random.sample(list(total_cities - {depot}), num_cities - 1)
    tour.append(depot)  # Complete the cycle by returning to the depot
    return tour

# Set parameters
num_cities = 10
total_cities = set(range(15))  # Including the depot city
trials = 100000
best_tour = None
best_cost = float('inf')

# Find the best tour
for _ in range(trials):
    tour = generate_random_tour(0, num_cities, total_cities)
    cost = calculate_tour_cost(tour)
    if cost < best_cost:
        best_cost = cost
        best_tour = tour

# Output the best tour found and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")