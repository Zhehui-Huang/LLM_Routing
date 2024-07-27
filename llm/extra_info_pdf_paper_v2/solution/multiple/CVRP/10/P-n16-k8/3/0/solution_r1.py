import math
from collections import defaultdict

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
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initialize distance matrix
n_cities = len(cities)
distance_matrix = [[calc_distance(cities[i], cities[j]) for j in range(n_cities)] for i in range(n_cities)]

# Enhanced Clarke-Wright Savings algorithm
def savings_algorithm():
    savings_list = []
    for i in range(1, n_cities):
        for j in range(i + 1, n_cities):
            if i != j:
                s = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
                savings_list.append((s, i, j))
    
    # Sort savings in descending order
    savings_list.sort(reverse=True, key=lambda x: x[0])

    routes = defaultdict(list)
    available_capacity = {k: capacity for k in range(num_robots)}
    city_assigned = [False] * n_cities

    for _, i, j in savings_list:
        if not city_assigned[i] and not city_assigned[j] and demands[i] + demands[j] <= capacity:
            # Find an available robot for this pair
            for robot in range(num_robots):
                if available_capacity[robot] >= demands[i] + demands[j]:
                    routes[robot].extend([i, j])
                    available_capacity[robot] -= (demands[i] + demands[j])
                    city_assigned[i] = city_assigned[j] = True
                    break

    # Allocate remaining cities
    for city in range(1, n_cities):
        if not city_assigned[city]:
            for robot in range(num_robots):
                if available_capacity[robot] >= demands[city]:
                    routes[robot].append(city)
                    available_capacity[robot] -= demands[city]
                    city_assigned[city] = True
                    break

    return routes

routes = savings_algorithm()

def calculate_tour_cost(route):
    total_cost = 0
    current = 0  # start at the depot
    for city in route:
        total_cost += distance_matrix[current][city]
        current = city
    total_cost += distance_matrix[current][0]  # return to depot
    return total_cost

def output_solution(routes):
    total_cost = 0
    for robot, route in routes.items():
        if route:
            full_route = [0] + route + [0]
            tour_cost = calculate_tour_cost(route)
            print(f"Robot {robot} Tour: {full_route}")
            print(f"Robot {robot} Total Travel Cost: {tour_cost:.2f}")
            total_cost += tour_cost

    print(f"Overall Total Travel Cost: {total_cost:.2f}")

output_solution(routes)