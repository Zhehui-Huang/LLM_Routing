import math
from random import shuffle

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
    """ Initializes the tours for each robot using a nearest neighbor heuristic """
    # Initialize tours with the starting depot
    tours = [[starting_deport] for _ in range(num_robots)]
    unvisited_cities = list(range(len(cities)))
    unvisited_cities.remove(starting_depot)  # Starting depot is already in the tour
    
    # Distribute the nearest cities to each robot initially
    while unvisited_cities:
        for tour in tours:
            if not unvisited_cities:
                break
            current_city = tour[-1]
            nearest_city = min(unvisited_cities, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
            tour.append(nearest_city)
            unvisited_cities.remove(nearest_city)

    return tours

def calculate_cost(tour):
    """ Calculate the travel cost for a given tour """
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_cost

def print_results(tours):
    """ Print the tours and costs for each robot and provide the total travel cost """
    total_travel_cost = 0
    for idx, tour in enumerate(tours):
        tour_cost = calculate_cost(tour)
        total_travel_cost += tour_cost
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost}")
    
    print(f"Overall Total Travel Cost: {total_travel_cost}")

# Initialize tours and print results
tours = initialize_tours(starting_depot)
print_results(tours)