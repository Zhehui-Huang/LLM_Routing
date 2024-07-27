import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_and_max_cost(tour, positions):
    total_cost = 0
    max_cost = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(positions[tour[i]], positions[tour[i+1]])
        total_cost += dist
        if dist > max_cost:
            max_cost = dist
    return total_cost, max_cost

# Cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Generate all possible tours
all_tours = permutations(range(1, len(cities)))  # Exclude the depot in permutations

best_tour = None
min_max_distance = float('inf')
best_total_cost = None

for tour in all_tours:
    tour = [0] + list(tour) + [0]  # Start and end at the depot (city 0)
    total_cost, max_distance = calculate_total_and_max_cost(tour, cities)
    
    if max_distance < min_max_distance:
        min_max_max_distance = max_distance
        best_tour = tour
        best_total_cost = total_cost

if best_tour:
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {best_total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
else:
    print("No feasible tour found")