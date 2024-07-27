import math
import random
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

def initialize_tour(cities):
    random.shuffle(cities)
    return cities

def two_opt(tour):
    n = len(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, n-2):
            for j in range(i+1, n-1):
                if euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]]) + \
                   euclidean_distance(coordinates[tour[j]], coordinates[tour[j+1]]) > \
                   euclidean_distance(coordinates[tour[i-1]], coordinates[tour[j]]) + \
                   euclidean_distance(coordinates[tour[i]], coordinates[tour[j+1]]):
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

def split_tours(cities, num_robots, coordinates):
    best_tours = []
    best_max_distance = float('inf')
    
    for _ in range(100):  # number of initial solutions
        tours = [[] for _ in range(num_robots)]
        initial_tour = initialize_tour(cities[:])
        chunks = [initial_tour[i::num_robots] for i in range(num_robots)]
        for idx in range(num_robots):
            tour = [0] + chunks[idx] + [0]
            tour = two_opt(tour)
            tours[idx] = tour
        current_max_distance = max(total_distance(tour, coordinates) for tour in tours)
        if current_max_distance < best_max_distance:
            best_max_distance = current_max_distance
            best_tours = tours
    
    return best_tours, best_max_distance

coordinates = [
    (30, 40),  # depot
    (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

cities = list(range(1, 21))
robots = 2

tours, max_cost = split_tours(cities, robots, coordinates)

for i, tour in enumerate(tours):
    travel_cost = total_distance(tour, coordinates)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {round(travel_cost, 2)}")

print(f"Maximum Travel Cost: {round(max_cost, 2)}")