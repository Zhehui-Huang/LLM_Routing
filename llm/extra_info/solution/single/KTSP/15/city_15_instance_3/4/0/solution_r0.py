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

# Function to find a greedy tour starting from the depot
def nearest_neighbor_tour(start, cities, num_cities):
    tour = [start]
    unvisited = set(cities.keys()) - {start}
    
    while len(tour) < num_cities:
        current = tour[-1]
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current], cities[x]))
        tour.append(next_city)
        unvisited.remove(next_city)

    tour.append(start)  # complete the loop
    return tour

# Function to calculate the total cost of a tour
def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_metric


# Combination of cities selection
min_cost = float('inf')
best_tour = None
all_combinations = itertools.combinations(range(1, 15), 9)  # Start from 1 to exclude the depot

for combo in all_combinations:
    selected_cities = {0}  # include the depot
    selected_cities.update(combo)
    selected_cities_dict = {key: cities[key] for key in selected_cities}
    tour = nearest_neighbor_tour(0, selected_cities_dict, len(selected_cities_dict))
    total_cost = calculate_total_cost(tour, selected_cities_dict)
    
    if total_cost < min_cost:
        min_cost = total_cost
        best_tour = tour

# Output the best tour and the total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")