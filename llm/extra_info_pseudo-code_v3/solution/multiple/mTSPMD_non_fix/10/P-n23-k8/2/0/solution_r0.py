import math
from random import randint, shuffle

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Coordinates of the cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots and their starting location
num_robots = 8
starting_depot = 0

# Initial assignment of tours using a simplified nearest neighbor strategy (Greedy allocation)
def initialize_tours(starting_depot):
    tours = [[] for _ in range(num_robots)]
    unvisited_cities = set(range(len(cities)))  # Set of all cities
    unvisited_cities.remove(starting_depot)  # Removing the depot city since it's the starting city
    current_city = [starting_depot] * num_robots

    # Each robot starts from the starting depot
    for i in range(num_robots):
        tours[i].append(starting_depot)
    
    # Nearest Neighbour allocation
    while unvisited_cities:
        for i in range(num_robots):
            if not unvisited_cities:
                break
            # Find the nearest unvisited city to the last city in the current tour
            last_city = current_city[i]
            next_city = min(unvisited_cities, key=lambda city: euclidean_distance(city[i], cities[last_city]))
            tours[i].append(next_city)
            unvisited_cities.remove(next_city)
            current_city[i] = next_city

    return tours

def calculate_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_cost

def print_results(tours):
    total_travel_cost = 0
    robot_results = []
    
    for idx, tour in enumerate(tours):
        tour_cost = calculate_cost(tour)
        total_travel_cost += tour_cost
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost}")
        robot_results.append((tour, tour_cost))
    
    print(f"Overall Total Travel Cost: {total_travel/\

# Initialize tours
tours = initialize_tours(starting_depot)
print_results(tours)