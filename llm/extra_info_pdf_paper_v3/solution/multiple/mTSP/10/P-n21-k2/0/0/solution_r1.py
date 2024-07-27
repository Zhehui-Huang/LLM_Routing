import math
import numpy as np
 
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
 
# Calculate the full nearest neighbor path starting from the depot
def nearest_neighbor_tour(start, cities, num_cities):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
   
    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
   
    tour.append(start)  # returning to the depot
    return tour
 
# Calculate the cost of the given tour based on distance
def calculate_tour_cost(tour, cities):
    cost = 0
    for i in range(len(tour)-1):
        cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    return cost
 
# Split the tour into two for the robots
def split_tour(tour, num_robots):
    n = len(tour) - 1  # excluding the return to depot in count
    split_index = n // 2 + 1
    tours = [tour[:split_index+1], tour[split_index:] + [tour[0]]]
    return tours

# Main operational block
cities = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
          6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
          12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
          18: (62, 63), 19: (63, 69), 20: (45, 35)}

full_tour = nearest_neighbor_tour(0, cities, len(cities))
robot_tours = split_tour(full_tour, 2)

total_cost = 0
for robot, tour in enumerate(robot_tours):
    cost = calculate_tour_cost(tour, cities)
    total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_temp_cost}")