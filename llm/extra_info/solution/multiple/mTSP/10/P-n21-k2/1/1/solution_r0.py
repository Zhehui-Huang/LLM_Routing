import math
from typing import List, Tuple, Dict

def euclidean_distance(city1: Tuple[int, int], city2: Tuple[int, int]) -> float:
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(route: List[int], coordinates: Dict[int, Tuple[int, int]]) -> float:
    total_dist = 0.0
    for i in range(1, len(route)):
        total_dist += euclidean_distance(coordinates[route[i-1]], coordinates[route[i]])
    return total_dist

def tsp_two_robots(coordinates: Dict[int, Tuple[int, int]], num_robots: int = 2) -> Tuple[List[List[int]], List[float], float]:
    cities = list(coordinates.keys())
    depot = cities.pop(0)  # Remove depot to handle cities only for initial TSP solution
    
    # Find a trivial solution by visiting in numerical order just for example (not efficient)
    cities.sort()
    even_cities = [cities[i] for i in range(len(cities)) if i % num_robots == 0]
    odd_cities = [cities[i] for i in range(len(cities)) if i % num_robots != 0]
    tours = [[depot] + even_cities + [depot], [depot] + odd_cities + [depot]]
    
    # Calculate distances for each tour
    costs = [calculate_total_distance(tours[i], coordinates) for i in range(num_robots)]
    
    # Total combined cost
    overall_cost = sum(costs)
    
    return tours, costs, overall_cost

# Coordinates of the cities (including depot)
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

tours, costs, overall_cost = tsp_two_robots(coordinates)

# Output results
for i in range(len(tours)):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")