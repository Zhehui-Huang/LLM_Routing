import numpy as np
import random
from math import sqrt

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# City coordinates including depot cities
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

def nearest_neighbor_solution(start_depot=0, city_coords=city_coords):
    unvisited_cities = set(city_coords.keys()) - {start_depot}
    tour = [start_depot]
    current_city = start_depot

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: euclidean_distance(city_coords[current_city], city_coords[x]))
        tour.append(next_city)
        current_city = next_city
        unvisited_cities.remove(next_city)
    
    return tour

# Start robots at different depots
num_robots = 2
depots = [0, 1]
tours = [nearest_neighbor_solution(depots[i]) for i in range(num_robots)]

# Check to avoid overlap between robot tours by unique assignment
total_cities = set(range(len(city_coords)))
assigned_cities = set(city for tour in tours for city in tour)
unassigned_cities = list(total_cities - assigned_cities)

while unassigned_cities:
    for tour in tours:
        if not unassigned_cities:
            break
        city = tour[-1]
        next_city = unassigned_cities.pop(0)
        tour.append(next_city)

# Calculate Tour Costs
def calculate_tour_cost(tour, city_coords):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    return cost

tour_costs = [calculate_tour_cost(tour, city_coords) for tour in tours]

# Output Results
total_travel_cost = sum(tour_costs)

for i, (tour, cost) in enumerate(zip(tours, tour_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_cost:.2f}")