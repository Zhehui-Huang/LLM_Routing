import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return cost

def nearest_neighbor_tour(start, cities, coordinates):
    unvisited = set(cities)
    tour = [start]
    while unvisited:
        last = tour[-1]
        next_city = min(universal_cities, key=lambda city: euclidean_distance(coordinates[last], coordinates[city]) if city in unvisited else float('inf'))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)
    return tour

def two_opt(tour, coordinates):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i == 1 and j == len(tour) - 2:
                    continue
                if euclidean_distance(coordinates[tour[i]], coordinates[tour[j]]) + euclidean_distance(coordinates[tour[i-1]], coordinates[tour[j+1]]) < euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]]) + euclidean_distance(coordinates[tour[j]], coordinates[tour[j+1]]):
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
depot = 0
robots = 8
cities = list(range(1, 23))  # city indices without the depot

# Divide the cities evenly among the robots
cities_per_robot = [cities[i::robots] for i in range(robots)]

# For each robot: Create a tour, improve it with 2-opt
tours = []
total_overall_cost = 0
for i in range(robots):
    tour = nearest_neighbor_tour(depot, cities_per_robot[i], coordinates)
    improved_tour = two_opt(tour, coordinates)
    tour_cost = calculate_cost(improved_tour, coordinates)
    total_overall_cost += tour_cost
    tours.append((improved_tour, tour_cost))
    print(f"Robot {i} Tour: {improved_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_overall infrastructure}")