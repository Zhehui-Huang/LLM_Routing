import numpy as np
from random import sample, random
from math import sqrt

def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

cities = {
    2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27),
    14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

depots = {
    0: (30, 40)
}

all_locations = {**depots, **cities}

def initialize_tours():
    city_ids = list(cities.keys())
    shuffle(city_ids)
    mid_point = len(city_ids) // 2
    return [city_ids[:mid_point], city_ids[mid_point:]]

def calculate_route_cost(route):
    cost = 0
    last_city = 0  # stating from depot 0
    for city in route:
        cost += euclidean distance(*all_locations[last_city], *all_locations[city])
        last_city = city
    return cost

def genetic_algorithm():
    # Initialize two routes randomly
    tours = initialize_tours()

    best_cost = float('inf')
    best_tours = None
    
    for _ in range(1000):  # Number of generations
        # Evaluate current tours
        current_cost1 = calculate_route_cost(tours[0])
        current_cost2 = calculate_route_cost(tours[1])
        total_cost = current_cost1 + current_cost2
        
        if total_cost < best_cost:
            best_cost = total_cost
            best_tours = [tours[0][:], tours[1][:]]
        
        # Mutate by swapping cities between routes randomly
        if random() > 0.5:
            city1 = sample(tours[0], 1)[0]
            city2 = sample(tours[1], 1)[0]
            tours[0].remove(city1)
            tours[1].remove(city2)
            tours[0].append(city2)
            tours[1].append(city1)
    
    return best_tours, calculate_route_cost(best_tours[0]), calculate_route_cost(best_tours[1]), best_cost

best_tours, cost1, cost2, overall_cost = genetic_algorithm()

print("Robot 0 Tour:", [0] + best_tours[0])
print("Robot 0 Total Travel Cost:", cost1)

print("Robot 1 Tour:", [0] + best_tours[1])
print("Robot 1 Total Travel Cost:", cost2)

print("Overall Total Travel Cost:", overall_cost)