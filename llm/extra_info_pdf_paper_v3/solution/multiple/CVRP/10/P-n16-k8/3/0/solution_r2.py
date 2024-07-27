import math

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

# Problem Data -------------------------------------------
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}
demands = {1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15,
           8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11}
num_robots = 8
robot_capacity = 35
depot = 0

# Distance matrix
distance_matrix = [[euclidean_distance(i, j) for j in range(len(cities))] for i in range(len(cities))]

# Assign cities to robots with greedy approach ------------------------------------
def greedy_cvrp(num_robots, robot_capacity):
    unvisited = set(demands.keys())
    routes = []
    total_cost = 0

    for _ in range(num_robots):
        capacity = robot_capacity
        current_city = depot
        tour = [depot]
        while unvisited and capacity > 0:
            next_city = min(unvisited, key=lambda x: (distance_matrix[current_city][x], -demands[x] if demands[x] <= capacity else float('inf')))
            if demands[next_city] > capacity:
                break
            capacity -= demands[next_class]
            unvisited.remove(next_city)
            tour.append(next_city)
            current_city = next_city
        tour.append(depot)
        routes.append(tour)
        tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        total_cost += tour_cost
        print("Robot {} Tour: {}".format(_, tour))
        print("Robot {} Total Travel Cost: {}".format(_, tour_cost))

    print("\nOverall Total Travel Cost: ", total_min_cost)
    return routes

# Execute the function
greedy_cvrp(num_robots, robot_capacity)