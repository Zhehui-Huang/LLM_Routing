import numpy as np
from scipy.spatial.distance import pdist, squareform
import random

# City coordinates data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Calculate the Euclidean pairwise distances matrix
dist_matrix = squareform(pdist(coordinates, 'euclidean'))

def find_nearest(current_city, cities_left):
    """Find the nearest city from the current city."""
    nearest_city = min(cities_left, key=lambda city: dist_matrix[current_city, city])
    return nearest_city

def generate_tours(num_robots, coordinates):
    num_cities = len(coordinates)
    cities = list(range(1, num_cities))  # exclude the depot (0)
    random.shuffle(cities)
    
    # Divide cities approximately evenly among robots
    tours = [[] for _ in range(num_robots)]
    for i, city in enumerate(cities):
        tours[i % num_robots].append(city)
    
    # Adding depot at the start and end of each tour
    for tour in tours:
        tour.insert(0, 0)  # start at depot
        tour.append(0)     # end at depot

    return tours

def route_cost(route):
    """ Calculate total distance of a route """
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route)-1))

# Generate initial solution tours
tours = generate_tours(num_robots, coordinates)

# Calculate the travel cost of each tour and the maximum travel cost
tour_costs = {f"Robot {i} Total Travel Cost": route_cost(tour) for i, tour in enumerate(tours)}
tour_output = {f"Robot {i} Tour": tour for i, tour in enumerate(tours)}
max_travel_cost = max(tour_costs.values())

# Output the tours and costs
for key, value in tour_output.items():
    print(f"{key}: {value}")
for key, value in tour_costs.items():
    print(f"{key}: {value}")
print(f"Maximum Travel Cost: {max_travel_cost}")