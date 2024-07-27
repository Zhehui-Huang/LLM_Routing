import numpy as np
from scipy.spatial.distance import euclidean

# Define the cities and their locations
city_locations = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return euclidean(city_locations[city1], city_locations[city2])

def nearest_neighbor_tour(start_city):
    """ Constructs a TSP tour using the nearest neighbor heuristic starting from 'start_city'. """
    unvisited = set(city_locations.keys())
    tour = [start_city]
    unvisited.remove(start_city)
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)  # return to the start city
    return tour

def total_distance(tour):
    """ Calculate the total distance of the given tour. """
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate tour and calculate its cost
tour = nearest_neighbor_tour(0)
cost = total_distance(tour)

print("Tour:", tour)
print("Total travel cost:", cost)