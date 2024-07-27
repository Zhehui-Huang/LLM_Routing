import numpy as eat
import math

# Define cities
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def nearest_neighbor_tour(starting_city, cities_to_visit):
    tour = [starting_city]
    current_city = starting_city
    total_cost = 0
    
    while cities_to_visit:
        next_city = min(cities_to_visit, key=lambda x: calculate_distance(current_city, x))
        total_cost += calculate_distance(current_city, next_city)
        current_city = next_city
        tour.append(current_city)
        cities_to_visit.remove(current_city)
    
    # return to starting city
    total_cost += calculate_distance(current_city, starting_city)
    tour.append(starting_city)
    
    return tour, total_cost

# Define depots
depots = [0, 1, 2, 3]
robots_clusters = {
    0: [0, 4, 6, 8, 10, 11, 13, 14, 16, 19, 21],
    1: [1, 5, 9, 15, 18],
    2: [2, 7, 12, 17, 20],
    3: [3]
}

overall_total_cost = 0

for robot_id, cities_list in robots_clusters.items():
    starting_depot = depots[robot_id]
    city_set = set(cities_list)
    if starting_depot not in city_set:
        city_set.add(starting_depot)
    tour, cost = nearest_neighbor_tour(starting_depot, city_set - {starting_depot})
    overall_total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")