import itertools
import math

# City coordinates
cities = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# City groups
groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Calculate Euclidean distance between two cities
def distance(city_a, city_b):
    xa, ya = cities[city_a]
    xb, yb = cities[city_b]
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

# Evaluate the tour cost
def evaluate_tour(tour):
    total_distance = distance(tour[-1], tour[0])  # Closing the tour
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i + 1])
    return total_distance

# Brute-force search for the shortest tour
def find_shortest_tour():
    minimum_cost = float('inf')
    best_tour = None
    
    for combination in itertools.product(*groups):
        all_tours = itertools.permutations(combination)
        for tour in all_tours:
            current_tour = [0] + list(tour) + [0]  # Start and end at depot
            current_cost = evaluate_tour(current_tour)
            if current_cost < minimum_online_cost:
                minimum_cost = current_cost
                best_tour = current_tour
    
    return best_tour, minimum_cost

# Find the tour and print the result
shortest_tour, tour_cost = find_shortest_tour()
print("Tour:", shortest_tour)
print("Total travel cost:", round(tour_cost, 2))