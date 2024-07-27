import math
from typing import List, Tuple

def euclidean_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cities' coordinates; index represents city id
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
          (43, 67), (58, 48), (58, 27), (37, 69)]

depot_cities = list(range(8))  # City ids of depots

# Function to find nearest depot for each city
def assign_cities_to_depots(cities: List[Tuple[int, int]], depots: List[int]):
    assignments = {depot: [] for depot in depots}
    for city_id, coords in enumerate(cities):
        if city_id in depots:
            assignments[city_id].append(city_id)
        else:
            nearest_depot = min(depots, key=lambda d: euclidean_distance(cities[d], coords))
            assignments[nearest_depot].append(city_id)
    return assignments

# Assigning cities to depots
city_assignments = assign_cities_to_depots(cities, depot_cities)

# Function to solve TSP for given cities
def solve_tsp(cities: List[Tuple[int, int]], tour: List[int]) -> Tuple[List[int], float]:
    from itertools import permutations
    min_cost = float('inf')
    best_route = []
    perms = permutations(tour[1:])
    for perm in perms:
        cost = 0
        last_city = tour[0]
        route = [tour[0]] + list(perm) + [tour[0]]
        for city in route[1:]:
            cost += euclidean_distance(cities[last_city], cities[city])
            last_city = city
        if cost < min_cost:
            min_cost = cost
            best_route = route
    return best_route, min_cost

# Process each robot's tour
total_cost = 0
for depot, tour_cities in city_assignments.items():
    optimal_tour, tour_cost = solve_tsp(cities, tour_cities)
    print(f"Robot {depot} Tour: {optimal_tour}")
    print(f"Robot {depot} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")