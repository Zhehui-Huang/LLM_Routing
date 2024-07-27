from itertools import cycle
import numpy as np
import random

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def find_closest_unvisited(current_city, unvisited, cities):
    distances = {city: euclidean_distance(cities[current_city], cities[city]) for city in unvisited}
    return min(distances, key=distances.get)

def greedy_tour(start_city, cities):
    tour = [start_city]
    unvisited = set(range(len(cities))) - {start_city}
    while unvisited:
        next_city = find_closest_unvisited(tour[-1], unvisited, cities)
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start_city)  # Return to depot
    return tour

def calculate_tour_cost(tour, cities):
    cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    return cost

cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
depots = [0, 1, 2, 3, 4, 5, 6, 7]
robots = len(depots)
robot_tours = {}
robot_costs = {}
overall_cost = 0

for depot_index, depot in enumerate(depots):
    available_cities = set(range(len(cities))) - set(depots)
    robot_tour = greedy_tour(depot, cities)
    tour_cost = calculate_tour_cost(robot_tour, cities)
    robot_tours[depot_index] = robot_tour
    robot_costs[depot_index] = tour_cost
    overall_cost += tour_cost

for robot_id in range(robots):
    print(f"Robot {robot_id} Tour: {robot_tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {robot_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_cost}")