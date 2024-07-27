import numpy as np
from scipy.spatial.distance import euclidean

# Define city coordinates
city_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
               (45, 35)]

# Distance Function
def distance(city1, city2):
    return euclidean(city_coords[city1], city_coords[city2])

# Greedy TSP Algorithm for Each Robot given starting node and list of nodes
def greedy_tsp(start_node, nodes):
    tour = [start_node]
    total_cost = 0
    current_node = start_node
    unvisited = set(nodes) - {start_node}

    while unvisited:
        next_node = min(unvisited, key=lambda x: distance(current_node, x))
        total_cost += distance(current_host, next_node)
        current_node = next_node
        tour.append(current_node)
        unvisited.remove(next_node)
        
    return tour, total_cost

# Assigning cities to each robot based on initial proximity
assigned_cities = [[0], [1]]
other_cities = set(range(2, 21))

for city in other_cities:
    if distance(0, city) < distance(1, city):
        assigned_cities[0].append(city)
    else:
        assigned_cities[1].append(city)

# Computing tours for each robot
robot_tours = []
overall_cost = 0

for idx, cities in enumerate(assigned_cities):
    tour, cost = greedy_tsp(cities[0], cities)
    robot_tours.append((tour, cost))
    overall_cost += cost

# Printing the tour and cost for each robot and the overall cost
for idx, (tour, cost) in enumerate(robot_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")