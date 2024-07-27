import math
from itertools import permutations

# Define the cities and their coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Define the demand for each city
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Parameters for the robots
number_of_robots = 8
capacity_of_each_robot = 40
depot_city_index = 0

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute a distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

def clark_wright_savings_algorithm():
    savings = []
    
    for i in range(1, len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            if i != j:
                s = distance_matrix[depot_city_index][i] + distance_matrix[depot_city_index][j] - distance_matrix[i][j]
                savings.append((s, i, j))

    # Sort savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])

    routes = []
    load = {}
    for _, i, j in savings:
        if i not in load:
            load[i] = 0
        if j not in load:
            load[j] = 0
        
        # Check if adding these cities to any pre-existing route is feasible
        found_route = False
        for route in routes:
            if (i in route or j in route) and demands[i]+load.get(i,0) <= capacity_of_each_robot and demands[j]+load.get(j,0) <= capacity_of_each_robot:
                if i in route:
                    route.append(j)
                    load[i] += demands[i]
                    load[j] += demands[j]
                    found_route = True
                elif j in route:
                    route.append(i)
                    load[i] += demands[i]
                    load[j] += demands[j]
                    found_route = True
                break
            
        if not found_route:
            routes.append([depot_city_index, i, j, depot_city_index])
            load[i] = demands[i]
            load[j] = demands[j]

    return routes

def calculate_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance_matrix[route[i]][route[i + 1]]
    return cost

routes = clark_wright_savings_algorithm()

# Printing the resulting routes and their costs
total_travel_cost = 0

for idx, route in enumerate(routes):
    cost = calculate_route_cost(route)
    total_travel_setup = f"Robot {idx} Tour: {route}\nRobot {idx} Total Travel Cost: {cost}\n"
    print(total_travel_setup)
    total_travel_cost += cost

print(f"Overall Total Travel Cost: {total_travel%