import math
import random

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_distance(tour, city_coordinates):
    total_distance = 0.0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    return total_distance

def generate_initial_solution(depot, cities, k):
    selected_cities = [depot]
    selected_cities.extend(random.sample(cities, k - 1))
    selected_cities.append(depot)
    return selected_cities

def two_opt(route, city_coordinates):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]
                if calculate_total_distance(new_route, city_coordinates) < calculate_total_distance(best, city_coordinates):
                    best = new_route
                    improved = True
        route = best
    return best

def multi_start_heuristic(city_coordinates, depot_index, k, iterations):
    best_tour = None
    best_cost = float('inf')
    cities = list(range(len(city_coordinates)))
    cities.remove(depot_index)
    
    for _ in range(iterations):
        initial_tour = generate_initial_solution(depot_index, cities, k)
        improved_tour = two_opt(initial_tour, city_coordinates)
        cost = calculate_total_distance(improved_tour, city_coordinates)
        if cost < best_cost:
            best_tour = improved_tour
            best_cost = cost
    return best_tour, best_cost

# City Coordinates
city_coordinates = [
    (3, 26),   # Depot City 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

result_tour, result_cost = multi_start_heuristic(city_coordinates, 0, 10, 100)
print("Tour:", result_tour)
print("Total travel cost:", result_cost)