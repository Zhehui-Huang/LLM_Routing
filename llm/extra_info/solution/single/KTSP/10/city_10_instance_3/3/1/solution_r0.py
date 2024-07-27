import itertools
import math

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate all combinations where 6 cities are chosen from cities 1-9 (excluding the depot city 0)
chosen_cities_combinations = itertools.combinations(range(1, 10), 6)

def calculate_tour_cost(cities_sequence):
    total_cost = 0
    for i in range(len(cities_sequence) - 1):
        total_cost += euclidean_vehicle_cost(cities_sequence[i], cities_sequence[i + 1])
    return total_cost

def euclidean_vehicle_cost(city1, city2):
    return euclidean_distance(cities[city1], cities[city2])

# Search the shortest tour
shortest_tour = None
min_cost = float('inf')

for combination in chosen_cities_combinations:
    full_cycle = [0] + list(combination) + [0]
    # Generate all permutations of the internal cities
    for perm in itertools.permutations(combination):
        current_tour = [0] + list(perm) + [0]
        current_cost = calculate_tour_cost(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            shortest_tour = current_tour

# Output the shortest tour and its cost
print("Tour:", shortest_tour)
print("Total travel cost:", min_cost)