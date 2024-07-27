import math
from itertools import permutations

# Define the coordinates of each city
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

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible tours that start and end at the depot city 0
def generate_tours():
    all_other_cities = list(cities.keys())[1:]
    return [
        [0] + list(perm) + [0]
        for perm in permutations(all_other_cities)
    ]

# Evaluate each tour by calculating the total cost and finding the max distance
def evaluate_tours(tours):
    best_tour = None
    best_tour_cost = float('inf')
    best_tour_max_distance = float('inf')

    for tour in tours:
        total_cost = 0
        max_distance = 0
        
        for i in range(len(tour) - 1):
            distance = calc_distance(tour[i], tour[i+1])
            total_cost += distance
            if distance > max_distance:
                max_distance = distance
        
        if max_distance < best_tour_max_distance:
            best_tour = tour
            best_tour_cost = total_cost
            best_tour_max_distance = max_distance

    return best_tour, best_tour_cost, best_tour_max_distance

all_tours = generate_tours()
best_tour, best_tour_cost, best_tour_max_distance = evaluate_tours(all_tours)

# Output result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_tour_max_distance:.2f}")