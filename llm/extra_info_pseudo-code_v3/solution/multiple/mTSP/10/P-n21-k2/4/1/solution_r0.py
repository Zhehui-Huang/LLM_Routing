import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates for each city including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# This function calculates the total travel cost for a given path
def calculate_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += euclidean(coordinates[path[i]], coordinates[path[i+1]])
    return cost

# Initial greedy approach to generate a start solution
def greedy_solution(num_robots, depot, cities):
    tours = [[] for _ in range(num_robots)]
    remaining_cities = set(cities)
    current_locations = [depot] * num_robots

    try:
        while remaining_cities:
            for robot in range(num_robots):
                if remaining_cities:
                    next_city = min(remaining_cities, key=lambda x: euclidean(coordinates[current_locations[robot]], coordinates[x]))
                    tours[robot].append(next_city)
                    current_locations[robot] = next_city
                    remaining_cities.remove(next_city)
    except Exception as e:
        print("Failed during initial greedy solution generation:", e)

    # Adding depot at the end of each robot tour
    for tour in tours:
        tour.append(depot)

    return [[depot] + tour for tour in tours]

# Split into two robots assignment, here we use a simple equal split method
def simple_split_solution(cities):
    half = len(cities) // 2
    return cities[:half], cities[half:]

# Generate initial solution and solve
def solve_multiple_tsp(num_robots, depot, cities):
    cities_without_depot = [i for i in range(len(coordinates)) if i != depot]
    split1, split2 = simple_split_solution(cities_without_develop)
    initial_tours = [
        [depot] + split1 + [depot],
        [depot] + split2 + [depot]
    ]

    costs = [calculate_cost(tour) for tour in initial_tours]
    overall_cost = sum(costs)

    # Output the results
    for idx, tour in enumerate(initial_tours):
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {costs[idx]}")
    
    print(f"Overall Total Travel Cost: {overall_cost}")

# Solve the MTSP with 2 robots starting from depot city 0
solve_multiple_tsp(2, 0, list(range(1, 21)))