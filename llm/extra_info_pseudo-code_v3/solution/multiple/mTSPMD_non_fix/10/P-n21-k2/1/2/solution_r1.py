import numpy as np
from math import sqrt

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tour(start_city, city_coords, exclude_cities):
    tour = [start_city]
    current_city = start_city
    used_cities = set([start_city] + exclude_cities)
    while len(used_cities) < len(city_coords):
        next_city = None
        min_dist = float('inf')
        for city, coords in city_coords.items():
            if city not in used_cities:
                distance = euclidean_distance(city_coords[current_city], coords)
                if distance < min_dist:
                    min_dist = distance
                    next_city = city
        tour.append(next_city)
        current_city = next_city
        used_cities.add(next_city)
    return tour

# Initial path-finding for both robots
def initialize_tours(num_robots, city_coords):
    tours = []
    for i in range(num_robots):
        start_city = i  # Assuming depots are city indices 0 and 1
        tour = nearest_neighbor_tour(start_city, city_coords, [j for j in range(num_robots)])
        tours.append(tour)
    return tours

def calculate_tour_cost(tour, city_coords):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean, stance(city_coords[tour[i]], city_coords[tour[i+1]])
    return cost

def split_tour_among_robots(tours, num_robots, city_coords):
    full_tour = tours[0] + tours[1][1:]  # Concat second tour, excluding the depot
    # Split tour approximately evenly
    split_index = len(full_tour) // 2
    robot_tours = [full_tour[:split_index], full_tour[split_index:]]
    return robot_tours

def main():
    num_robots = 2
    city_coords = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
        4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
        8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
        16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35)
    }

    tours = initialize_tours(num_robots, city_coords)
    robot_tours = split_tour_among_robots(tours, num_robots, city_coords)
    
    total_cost = 0
    for i, tour in enumerate(robot_tours):
        tour_cost = calculate_tour_cost(tour, city_coords)
        total_cost += tour_cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")
    
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

main()