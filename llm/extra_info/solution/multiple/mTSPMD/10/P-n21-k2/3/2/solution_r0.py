import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def construct_tour(cities, depot):
    tour = [depot]
    remaining_cities = set(cities) - {depot}
    current_city = depot
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city
    tour.append(depot)
    return tour

def calculate_total_distance(tour, city_coordinates):
    return sum(euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour)-1))

def two_opt(tour, city_coordinates):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_total_distance(new_tour, city_coordinates) < calculate_total_distance(best, city_coordinates):
                    best = new_tour
                    improved = True
        tour = best
    return best

# City coordinates indexed by city number
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Construct initial tours starting from each depot
initial_tour_0 = construct_tour(cities=city_coordinates.keys(), depot=0)
initial_tour_1 = construct_tour(cities=city_coordinates.keys(), depot=1)

# Optimize tours using 2-opt technique
optimized_tour_0 = two_opt(initial_tour_0, city_coordinates)
optimized_tour_1 = two_opt(initial_tour_1, city_coordinates)

# Calculate distances
total_cost_0 = calculate_total_distance(optimized_tour_0, city_coordinates)
total_cost_1 = calculate_total_distance(optimized_tour_1, city_coordinates)
overall_total_cost = total_cost_0 + total_cost_1

# Output results
print('Robot 0 Tour:', optimized_tour_0)
print('Robot 0 Total Travel Cost:', total_cost_0)
print('Robot 1 Tour:', optimized_tour_1)
print('Robot 1 Total Travel Cost:', total_cost_1)
print('Overall Total Travel Cost:', overall_total_cost)