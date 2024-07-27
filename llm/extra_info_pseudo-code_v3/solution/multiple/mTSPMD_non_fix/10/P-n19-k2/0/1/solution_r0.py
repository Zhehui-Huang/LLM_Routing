import math
import random

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    c1, c2 = cities[city1], cities[city2]
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def nearest_neighbor_tour(start_city, unvisited_cities):
    """ Construct a tour starting from a given city using the nearest neighbor approach """
    tour = [start_city]
    current_city = start_city
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: euclidean_distance(current_city, x))
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour

# Number of robots and their start points
num_robots = 2
start_points = [0 for _ in range(num_robots)]

# Initial tours construction using NNS
initial_tours = []
unvisited_cities = set(cities.keys()) - {0}

for i in range(num_robots):
    start_city = start_points[i]
    tour = nearest_neighbor_tour(start_city, unvisited_cities)
    initial_tours.append(tour)

def calculate_tour_cost(tour):
    """ Calculate the total travel cost of a tour """
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Calculate tour costs and total cost
total_cost = 0

for i, tour in enumerate(initial_tours):
    tour_cost = calculate_tour_cost(tour + [tour[0]])  # Returning to the starting depot
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour + [tour[0]]}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")