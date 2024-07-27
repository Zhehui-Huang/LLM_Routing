from itertools import permutations, combinations
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_distance(tour, coords):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(coords[tour[i]][0], coords[tour[i]][1], coords[tour[i + 1]][0], coords[tour[i + 1]][1])
    return total_distance

def optimal_tsp_tour(cities, coords, num_cities_to_visit=5):
    depot_city = 0
    all_combinations = combinations(range(1, len(cities)), num_cities_to_visit - 1)
    best_tour = None
    best_distance = float('inf')

    for combination in all_combinations:
        city_set = [depot_city] + list(combination)
        for perm in permutations(city_set):
            tour = list(perm) + [depot_city]
            current_distance = calculate_total_distance(tour, coords)
            if current_distance < best_distance:
                best_tour = tour
                best_distance = current_distance

    return best_tour, best_distance

# City coordinates
city_coords = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), 
               (70, 14), (97, 44), (17, 69), (95, 89)]

# Cities (indices)
cities = list(range(10))

# Finding the optimal tour and its total travel cost.
tour, total_cost = optimal_tsp_tour(cities, city_coords)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")