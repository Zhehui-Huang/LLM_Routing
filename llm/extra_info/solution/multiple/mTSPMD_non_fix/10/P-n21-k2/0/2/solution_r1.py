import numpy as np
from scipy.spatial.distance import euclidean
from collections import defaultdict

# Define city coordinates
city_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
               (45, 35)]

# Assign depots
depots = [0, 1]

# Distance function
def calculate_distance(city1, city2):
    return euclidean(city_coords[city1], city_coords[city2])

# Greedy algorithm based on each robot starting from corresponding depot
def greedy_tsp(start_city, available_cities):
    tour = [start_city]
    current_city = start_city
    while available_cities:
        next_city = min(available_cities, key=lambda x: calculate_distance(current_city, x))
        tour.append(next_city)
        current_city = next_city
        available_cities.remove(next_city)
    return tour, sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Divide cities amongst robots based on nearest depot
city_assignments = {i: [] for i in range(len(depots))}
for city in range(len(city_coords)):
    if city in depots:
        continue
    nearest_depot = min(depots, key=lambda x: calculate_distance(x, city))
    city_assignments[nearest_depot].append(city)

# Calculate tours and costs
tours = {}
total_travel_cost = 0
for depot in depots:
    assigned_cities = [depot] + city_assignments[depot]
    tour, tour_cost = greedy_tsp(depot, set(assigned_cities))
    tours[depot] = (tour, tour_cost)
    total_travel_cost += tour_cost

# Output results
for robot_id, depot in enumerate(depots):
    tour, cost = tours[depot]
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {total_travel_count}")