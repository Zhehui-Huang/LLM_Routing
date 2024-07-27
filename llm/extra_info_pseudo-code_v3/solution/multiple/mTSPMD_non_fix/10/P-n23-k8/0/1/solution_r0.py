import math
import random

# Cities coordinates
city_coords = [
    (30, 39), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

def euclidean_distance(coord1, coord2):
    return math.hypot(coord1[0] - coord2[0], coord1[1] - coord2[1])

# Initialize tours
def nns_initial_solution(num_robots, city_coords):
    num_cities = len(city_coords)
    tours = [[] for _ in range(num_robots)]
    remaining_cities = list(range(1, num_cities))
    depots = list(range(num_robots))

    # Assign initial cities to each depot
    for depot in depots:
        nearest_city, min_dist = min(
            ((city, euclidean_distance(city_coords[depot], city_coords[city])) for city in remaining_cities),
            key=lambda x: x[1]
        )
        tours[depot].append(depot)
        tours[depot].append(nearest_city)
        remaining_cities.remove(nearest_city)

    # Continuously assign nearest city to each tour
    while remaining_cities:
        for tour in tours:
            if not remaining_cities:
                break
            last_city = tour[-1]
            nearest_city, min_dist = min(
                ((city, euclidean_distance(city_coords[last_city], city_coords[city])) for city in remaining_cities),
                key=lambda x: x[1]
            )
            tour.append(nearest_city)
            remaining_cities.remove(nearest_city)

    return tours

def calculate_tour_cost(tour, city_coords):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    return cost

num_robots = 8
tours = nns_initial_solution(num_robots, city_coords)

# Output results
total_travel_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour, city_coords)
    total_travel_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_travel_box}")