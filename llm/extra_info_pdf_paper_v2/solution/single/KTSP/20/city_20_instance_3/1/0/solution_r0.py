import math
import random

# Define the cities' coordinates with city index as keys.
city_positions = {
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
    19: (19, 72),
}

def euclidean_distance(city1, city2):
    x1, y1 = city_positions[city1]
    x2, y2 = city_positions[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Number of cities to visit including the depot city (k-value).
k = 13

# Initialize variables
num_cities = len(city_positions)
all_cities = set(city_positions.keys())
best_tour = None
best_cost = float('inf')

def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i-1], tour[i])
    cost += euclidean_distance(tour[-1], tour[0])  # Closing the loop
    return cost

def local_search(tour):
    # Performs local optimization swapping cities within the tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 1):
            for j in range(i + 1, len(tour)):
                new_tour = tour[:i] + [tour[j]] + tour[i+1:j] + [tour[i]] + tour[j+1:]
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < calculate_tour_cost(tour):
                    tour = new_tour
                    improved = True
    return tour

# Randomly pick k cities to form an initial tour including the depot city.
initial_tour = [0] + random.sample(list(all_cities - {0}), k - 1)
initial_tour = local_search(initial_tour)
initial_cost = calculate_tour_cost(initial_tour)
print(f"Initial tour: {initial_tour}")
print(f"Initial cost: {initial_cost}")

# Perform GVNS
for iteration in range(1000):
    # Perturbation: randomly pick a non-tour city and a tour city and swap them
    external_cities = list(all_cities - set(initial_tour))
    city_to_add = random.choice(external_cities)
    city_to_remove = random.choice(initial_tour[1:])  # Avoid removing the depot

    new_tour = [city_to_add if x == city_to_remove else x for x in initial_tour]
    new_tour = local_search(new_tour)
    new_cost = calculate_tour_cost(new_tour)
    
    if new_cost < best_cost:
        best_tour = new_tour
        best_cost = new_cost

# Reporting the best results
best_tour.append(best_tour[0])  # To close the tour
print("Best tour:", best_tour)
print("Total travel cost:", best_cost)