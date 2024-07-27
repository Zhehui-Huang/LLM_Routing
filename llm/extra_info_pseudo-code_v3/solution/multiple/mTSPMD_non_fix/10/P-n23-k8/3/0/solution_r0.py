import numpy as np
from math import sqrt

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Distance calculation
def euclidean_distance(c1, c2):
    return sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate initial solution based on nearest neighbor heuristic
def nearest_neighbor_tour(start_index):
    tour = [start_index]
    unvisited = set(cities.keys()) - {start_index}
    
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda city: euclidean_distance(last, city))
        tour.append(next_city)
        unvisited.remove(next_city)
    
    return tour

# Divide tasks among robots based on nearest neighbor tours
def divide_tours_among_robots(num_robots, start_index=0):
    robots_tours = []
    cities_per_robot = len(cities) // num_robots
    remaining_cities = list(cities.keys())
    
    for i in range(num_robots):
        current_tour_head = start_index if i == 0 else robots_tours[i-1][-1]
        tech_tour = nearest_neighbor_tour(current_tour_head)[:cities_per_robot+1]
        robots_tours.append(tech_tour)
        for city in tech_tour:
            if city in remaining_cities:
                remaining_cities.remove(city)
    
    return robots_tours

def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclideanointeractionancetance(tour[i - 1], tour[i])
    cost += euclidean_distance(tour[-1], tour[0])  # returning to starting depot
    return cost

# Assigning the tours to eight robots
tours = divide_tours_among_robots(8)
total_cost = 0

for idx, tour in enumerate(tours):
    cost = calculate_tour_cost(tour)
    total_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")