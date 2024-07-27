import numpy as np
from math import sqrt
import random
import time

# City coordinates with city index as key
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

# Number of robots
num_robots = 8

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_distance(tour, city_coordinates):
    return sum(euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour) - 1))

def initialization(num_robots, cities):
    tours = {i: [0] for i in range(num_robots)}
    remaining_cities = list(cities.keys())[1:]  # exclude the depot city
    random.shuffle(remaining_cities)
    for i, city in enumerate(remaining_cities):
        tours[i % num_robots].append(city)
    for tour in tours.values():
        tour.append(0)
    return tours

def gvns(cities, num_robots, max_iter=1000):
    tours = initialization(num_robots, cities)
    
    for _ in range(max_iter):
        # Shaking: Randomly pick a tour and two cities to swap
        tour_ids = list(tours.keys())
        random.shuffle(tour_ids)
        
        for tour_id in tour_ids:
            if len(tours[tour_id]) > 3:  # To avoid swapping in very short tours
                i, j = sorted(random.sample(range(1, len(tours[tour_id]) - 1), 2))
                tours[tour_id][i], tours[tour_id][j] = tours[tour_id][j], tours[tour_id][i]

        # Local search: simple 2-opt swap inside each tour
        for tour_id in tour_ids:
            tour = tours[tour_id]
            improved = True
            while improved:
                improved = False
                for i in range(1, len(tour) - 2):
                    for j in range(i+1, len(tour) - 1):
                        if j - i == 1:  # Skip adjacent edges
                            continue
                        # Perform 2-opt swap
                        new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                        if calculate_tour_distance(new_tour, cities) < calculate_tour_distance(tour, cities):
                            tour[:] = new_tour
                            improved = True

    return tours

# Run GVNS
final_tours = gvns(cities, num_robots)

# Results
max_cost = 0
for idx, tour in final_tours.items():
    cost = calculate_tour_distance(tour, cities)
    max_cost = max(max_cost, cost)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")