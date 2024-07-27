import math

# Define city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

# Robot parameters
number_of_robots = 8
capacity_of_each_robot = 40
depot = 0

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_distance_matrix(coords):
    n = len(coords)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return dist_matrix

distance_matrix = calculate_distance_matrix(coordinates)

def clark_wright_savings_algorithm():
    n = len(coordinates)
    savings_list = []
    for i in range(1, n):
        for j in range(i + 1, n):
            savings = distance_matrix[depot][i] + distance_matrix[depot][j] - distance_matrix[i][j]
            savings_list.append((savings, i, j))
    savings_list.sort(reverse=True, key=lambda x: x[0])

    routes = []
    used_capacity = [0] * number_of_robots
    for _, i, j in savings_list:
        if demands[i] + demands[j] <= capacity_of_each_robot:
            assigned = False
            for route in routes:
                last = route[-2]
                if used_capacity[route[-1]] + demands[i] <= capacity_of_each_robot and distance_matrix[last][i] == distance_matrix[last][depot] + distance_matrix[depot][i]:
                    if used_capacity[route[-1]] + demands[j] <= capacity_of_each_robot:
                        route.insert(-1, i)
                        route.insert(-1, j)
                        used_capacity[route[-1]] += demands[i] + demands[j]
                        assigned = True
                        break
            if not assigned:
                if len(routes) < number_of_robots:
                    robot_id = len(routes)
                    routes.append([depot, i, j, depot, robot_id])
                    used_capacity.append(demands[i] + demands[j])
    return routes

def calculate_total_route_cost(routes):
    total_cost = 0
    for route in routes:
        robot_id = route.pop()
        cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        print(f"Robot {robot_id} Tour: {route}")
        print(f"Robot {robot.required} Total Travel Cost: {cost}")
        total_cost += cost
    return total_cost

routes = clark_wright_savings_algorithm()
total_cost = calculate_total_route_cost(routes)
print(f"Overall Total Travel Cost: {total_cost}")