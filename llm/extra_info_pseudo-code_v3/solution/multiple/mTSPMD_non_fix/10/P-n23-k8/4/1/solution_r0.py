import math
import random
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

def initial_solution(depot_indices, num_robots):
    depots = {index: cities[index] for index in depot_indices}
    other_cities = {index: cities[index] for index in cities if index not in depot_indices}
    tours = {r: [list(depots.keys())[r]] for r in range(num_agents)}

    # Assign nearest non-depot city to each depot
    for robot, tour in tours.items():
        start_city = tour[0]
        nearest_city, min_distance = None, float('inf')
        for city, coords in other_cities.items():
            distance = euclidean_distance(cities[start_city], coords)
            if distance < min_distance:
                nearest_city, min_distance = city, distance
        if nearest_city:
            tours[robot].append(nearest_city)
            del other_cities[nearest_city]
    
    # Greedy allocation of remaining cities
    while other_cities:
        for robot, tour in tours.items():
            last_city = tour[-1]
            nearest_city, min_distance = None, float('inf')
            for city, coords in other_cities.items():
                distance = euclidean_distance(cities[last_city], coords)
                if distance < min_distance:
                    nearest_city, min_distance = city, distance
            if nearest_city:
                tours[robot].append(nearest_city)
                del other_cities[nearest_city]
    
    # Calculate initial tour costs
    cost = {}
    total_cost = 0
    for robot, tour in tours.items():
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_category[idx][tour[i], tour[i+1]]
        cost[robot] = round(tour_cost, 2)
        total_cost += tour_cost
        print(f"Robot {robot} Tour: {tour}")
        print(f"Robot {robot} Total Travel Cost: {cost[robot]}")

    print(f"Overall Total Travel Cost: {round(total_cost, 2)}")

    return tours

# Configuration
num_agents = 8
depot_indices = [0, 1, 2, 3, 4, 5, 6, 7]

# Generate and print the results of the initial solution
tours = initial_solution(depot_indices, num_agents)