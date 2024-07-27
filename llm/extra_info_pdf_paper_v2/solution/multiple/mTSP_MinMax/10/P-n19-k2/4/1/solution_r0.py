import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_tour_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
          (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Basic heuristic to distribute cities among two robots
def initial_solution(num_robots, cities):
    num_cities = len(cities)
    segment = (num_cities - 1) // num_robots
    tours = []
    for i in range(num_robots):
        tours.append([0] + list(range(1 + i * segment, 1 + min((i + 1) * segment, num_cities - 1))) + [0])
    return tours

tours = initial_solution(2, cities)
for tour in tours:
    print("Initial Tour:", tour, "Cost:", total_tour_distance(tour, cities))