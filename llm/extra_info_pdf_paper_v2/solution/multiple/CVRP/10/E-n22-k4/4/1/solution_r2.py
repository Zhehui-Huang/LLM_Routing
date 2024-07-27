import math

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
    1800, 700
]

# Robot details
number_of_robots = 4
robot_capacity = 6000
depot_index = 0

# Precompute distances between all pairs of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Clarke-Wright Savings Algorithm implementation
def clarkewright_savings_algorithm():
    # Calculate savings for each pair of cities
    savings = []  # tuples of (saving, i, j)
    for i in range(1, len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            s = distance_matrix[depot_index][i] + distance_matrix[depot_index][j] - distance_matrix[i][j]
            savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])

    # Initialize routes for each robot
    routes = {i: [depot_index] for i in range(number_of_robots)}
    load = {i: 0 for i in range(number_of_robots)}
    city_assigned = {i: False for i in range(1, len(coordinates))}

    for s, i, j in savings:
        if city_assigned[i] or city_assigned[j]:
            continue
        for r in range(number_of_robots):
            if not city_assigned[i] and not city_assigned[j] and load[r] + demands[i] + demands[j] <= robot_capacity:
                routes[r].extend([i, j, depot_index])
                load[r] += demands[i] + demands[j]
                city_assigned[i] = city_assigned[j] = True
                break
    
    # Assign remaining cities
    for city in range(1, len(coordinates)):
        if not city_assigned[city]:
            for r in range(number_of_robots):
                if load[r] + demands[city] <= robot_capacity:
                    if routes[r][-1] == depot_index:
                        routes[r].insert(-1, city)
                    else:
                        routes[r].extend([city, depot_index])
                    load[r] += demands[city]
                    city_assigned[city] = True
                    break
    
    return routes

def calculate_cost_and_output(routes):
    total_cost = 0
    results = []
    
    for r, route in routes.items():
        cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        total_cost += cost
        results.append(f"Robot {r} Tour: {route}\nRobot {r} Total Travel Cost: {cost}")
        
    results.append(f"Overall Total Travel Cost: {total_cost}")
    return '\n'.join(results)

# Run Clarke-Wright algorithm and calculate the results
routes = clarkewright_savings_algorithm()
output = calculate_cost_and_output(routes)
print(output)