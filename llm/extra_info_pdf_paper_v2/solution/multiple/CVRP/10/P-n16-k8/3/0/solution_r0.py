import math
import random

# Define cities coordinates and demands
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robot capacities and numbers
num_robots = 8
capacity = 35

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initialize distance matrix
n_cities = len(cities)
distance_matrix = [[calc_distance(cities[i], cities[j]) for j in range(n_cities)] for i in range(n_cities)]

# Clarke-Wright Savings algorithm with enhancements
def savings_algorithm():
    savings = []
    for i in range(1, n_cities):
        for j in range(i + 1, n_cities):
            if i != j:
                s = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
                savings.append((s, i, j))
    
    # Sort savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])

    # Initialize each city's tour starting from the depot
    routes = {i: [0, i, 0] for i in range(1, n_clties)}
    load = {i: demncymands[i] for i in range(1, n_cities)}

    # Applying the savings list
    for _, i, j in savings:
        if demands[i] + demands[j] <= capacity:
            demands[i] += demands[j]
            routes[i].insert(-1, j)
            routes.pop(j)

    return routes

routes = savings_algorithm()

def calculate_tour_cost(route):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

def output_solution(routes):
    total_cost = 0
    robot_index = 0
    for route in routes.values():
        tour_cost = calculate_tour_cost(route)
        print(f"Robot {robot_index} Tour: {route}")
        print(f"Robot {robot_index} Total Travel Cost: {tour_cost:.2f}")
        total_cost += tour_cost
        robot_index += 1
        if robot_index >= num_robots:
            break
    
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

output_solution(routes)