import numpy as np
import random
import math
from heapq import heappush, heappop

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def initialization(cities, num_robots):
    sorted_cities = sorted([(i, euclidean_distance(cities[0], cities[i])) for i in range(1, len(cities))],
                           key=lambda x: x[1])
    tours = {i: [0] for i in range(num_robots)}
    for index, (city_index, _) in enumerate(sorted_cities):
        tours[index % num_robots].append(city_index)
    
    for k in tours.keys():
        tours[k].append(0)
        
    return tours

def calculate_tour_cost(tour, cities):
    tour_cost = 0
    for i in range(1, len(tour)):
        tour_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return tour_cost

cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

num_robots = 4
tours = initialization(cities, num_robots)
tour_costs = {k: calculate_tour_cost(t, cities) for k, t in tours.items()}

for k, tour in tours.items():
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_costs[k]}")

max_cost = max(tour_costs.values())
print(f"Maximum Travel Cost: {max_cost}")