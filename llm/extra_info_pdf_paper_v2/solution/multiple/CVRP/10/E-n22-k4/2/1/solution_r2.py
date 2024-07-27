import math

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 
           1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Robot specifications
num_robots = 4
capacity = 6000

# Calculate distances
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

distance_matrix = [[calculate_distance(i, j) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Implementing a simple VRP
def greedy_vrp():
    routes = []
    remaining_cities = set(range(1, len(coordinates)))
    remaining_capacity = [capacity] * num_robots

    # Initialize routes for each robot starting at the depot
    for i in range(num_robots):
        routes.append([0]) # Start at the depot

    while remaining_cities:
        for robot in range(num_robots):
            if not remaining_cities:
                break
            current_city = routes[robot][-1]
            best_next_city = None
            min_distance = float('inf')
            for city in remaining_cities:
                if demands[city] <= remaining_capacity[robot] and distance_matrix[current_city][city] < min_distance:
                    best_next_city = city
                    min_distance = distance_matrix[current_city][city]
            
            if best_next_city is not None:
                routes[robot].append(best_next_city)
                remaining_capacity[robot] -= demands[best_next_city]
                remaining_cities.remove(best_next_city)

    # Close the routes by returning to the depot
    for route in routes:
        route.append(0)
    
    return routes

routes = greedy_vrp()

# Calculate the travel costs
def calculate_route_cost(route):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

overall_total_cost = 0
for idx, route in enumerate(routes):
    route_cost = calculate_route_cost(route)
    overall_total_content += route_cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_total_cost:.2f}")