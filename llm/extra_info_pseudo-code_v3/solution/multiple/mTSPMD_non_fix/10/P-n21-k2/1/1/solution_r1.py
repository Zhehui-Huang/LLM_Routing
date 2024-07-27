import math
import random

# City coordinates data
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

number_of_robots = 2
depots = [0, 1]

def euclidean_distance(a, b):
    """ Compute the Euclidean distance between two points """
    return math.sqrt((city_coords[a][0] - city_coords[b][0])**2 + (city_coords[a][1] - city_coords[b][1])**2)

def nearest_neighbor_tour(start_city, unvisited_cities):
    """ Generate a tour starting from a given city using the nearest neighbor heuristic """
    tour = [start_city]
    current_city = start_city
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city
    return tour

# Divide cities evenly for two robots starting from the depots
unvisited_cities = set(city_coords.keys()) - set(depots)
tours = []
for depot in depots:
    assigned_cities = random.sample(unvisited_cities, len(unvisited_cities)//number_of_robots)
    unvisited_cities -= set(assigned_cities)
    tours.append(nearest_neighbor_tour(depot, assigned_cities))

# Calculate travel cost for each tour and overall cost
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

robot_costs = [calculate_tour_cost(tour) for tour in tours]
overall_cost = sum(robot_costs)

# Output results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {robot_costs[i]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")