import numpy as np
import random

class City:
    def __init__(self, index, coordinate):
        self.index = index
        self.coordinate = coordinate
        
    def distance_to(self, city):
        return np.sqrt((self.coordinate[0] - city.coordinate[0])**2 + (self.coordinate[1] - city.coordinate[1])**2)

class Robot:
    def __init__(self, robot_id, start_depot, cities):
        self.robot_id = robot_id
        self.start_depot = start_depot
        self.cities = cities
        self.route = [start_depot]

    def tour(self):
        unvisited = set(self.cities) - set(self.route)
        current_city = self.start_depot
        while unvisited:
            next_city = min(unvisited, key=lambda city: city.distance_to(current_city))
            self.route.append(next_city)
            current_city = next_city
            unvisited.remove(next_city)
        self.route.append(self.start_depot)  # return to start depot

    def total_travel_cost(self):
        cost = 0
        for i in range(1, len(self.route)):
            cost += self.route[i].distance_to(self.route[i-1])
        return cost

    def get_route_indices(self):
        return [city.index for city in self.route]

# Set up the cities and robots
city_coords = [
    (30, 40), (37, 52), (49, 49),
    (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]
cities = [City(index, coord) for index, coord in enumerate(city_coords)]
depots = cities[:8]  # assuming the first 8 cities are depots
robots = [Robot(i, depots[i], cities[8:]) for i in range(8)]

# Compute tours for each robot
overall_total_cost = 0
for robot in robots:
    robot.tour()
    tour_cost = robot.total_travel_cost()
    overall_total_cost += tour_cost
    print(f"Robot {robot.robot_id} Tour: {robot.get_route_indices()}")
    print(f"Robot {robot.robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")