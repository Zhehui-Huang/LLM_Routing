import math
import random

# City coordinates
cities = {
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

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    num_iterations = 1000
    num_cities_in_tour = 10
    all_cities = list(cities.keys())

    for _ in range(num_iterations):
        selected_cities = [0] + random.sample([c for c in all_cities if c != 0], num_cities_in_tour - 1)
        best_local_tour = None
        best_local_cost = float('inf')
        
        # Permutate through the selected cities to find the best local tour
        for _ in range(100):
            random.shuffle(selected_cities[1:])  # Shuffle only non-depot cities
            current_tour = selected_cities + [0]  # Return to depot
            current_cost = total_tour_cost(current_tour)
            if current_cost < best_local_cost:
                best_local_tour = current_tour
                best_local_cost = current_cost

        if best_local_cost < best_cost:
            best_tour = best_local_tour
            best_cost = best_local_cost

    return best_tour, best_cost

best_tour, best_cost = find_shortest_tour()
best_cost = round(best_cost, 2)  # Rounding the cost for cleaner output

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")