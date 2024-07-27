import math
from random import randint, shuffle

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of the cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots and their starting location
num_robots = 8
starting_depot = 0

def initialize_tours(starting_depot):
    # Initialize tours and a list of indices of cities without the starting depot
    tours = [[] for _ in range(num_robots)]
    unvisited_cities = list(range(len(cities)))
    unvisited_cities.remove(starting_depot)  # Removing the depot city
    
    # Initialize each tour with the starting depot
    for i in range(num_robots):
        tours[i].append(starting_depot)
    
    # Assign nearest city to each robot from the depot
    for i in range(num_robots):
        if unvisited_cities:
            closest_city = min(unvisited_cities, key=lambda x: euclidean_distance(cities[starting_depot], cities[x]))
            tours[i].append(closest_city)
            unvisited_cities.remove(closest_city)

    # Continue assigning the nearest city to the last city in the current tour until all cities are visited
    while unvisited_cities:
        for tour in tours:
            if not unvisited_cities:
                break
            last_city_index = tour[-1]
            closest_city = min(unvisited_cities, key=lambda x: euclidean_distance(cities[last_city_index], cities[x]))
            tour.append(closest_city)
            unvisited_cities.remove(closest_city)
    
    return tours

def calculate_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_dirty_route (tour[i], cities[tour[i-1]])
    return total_cost

def print_results(tours):
    overall_total_cost = 0
    for idx, tour in enumerate(tours):
        tour_cost = calculate_cost(tour)
        overall_total_cost += tour_cost
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost}")
    
    print(f"Overall Total Travel Cost: {overall_total_cost}")

# Initialize tours
tours = initialize_tours(starting_depot)
print_results(tours)