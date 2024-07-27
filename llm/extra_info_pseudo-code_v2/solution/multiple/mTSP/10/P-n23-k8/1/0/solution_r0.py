import math
import random

# Coordinates of the cities
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
    22: (56, 37),
}

# Number of robots
num_robots = 8

# Calculate distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Simple heuristic: Divide cities approximately equally and use nearest neighbour for initial tours
def assign_initial_routes():
    cities_per_robot = (len(cities) - 1) // num_robots
    tours = []
    remaining_cities = list(cities.keys())[1:]  # exclude the depot city 0
    
    for i in range(num_robots):
        tour = [0]  # start at depot
        while len(tour) - 1 < cities_per_robot and remaining_cities:
            if len(remaining_cities) > 0:
                next_city = min(remaining_cities, key=lambda x: distance(tour[-1], x))
                remaining_cities.remove(next_city)
                tour.append(next_city)
        tour.append(0)  # return to depot
        tours.append(tour)
    
    # If any cities are left (due to integer division), add them to existing tours
    for city in remaining_cities:
        min_tour = min(tours, key=len)
        min_tour.insert(-1, city)  # Insert before returning to depot
    
    return tours

# 2-opt algorithm to improve each tour
def optimize_tour(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:
                    continue
                if distance(tour[i-1], tour[i]) + distance(tour[j], tour[j+1]) > \
                   distance(tour[i-1], tour[j]) + distance(tour[i], tour[j+1]):
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improved = True
    return tour

# Calculate total tour cost
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Assign initial routes to robots
initial_tours = assign_initial_routes()

# Optimize each initial tour
optimized_tours = [optimize_tour(tour) for tour in initial_tours]

# Display the results
overall_cost = 0
for idx, tour in enumerate(optimized_tours):
    tour_cost = calculate_tour_cost(tour)
    overall_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {round(tour_cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")