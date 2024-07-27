from pulp import *
import math

# Define the cities with their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initialize the problem
prob = LpProblem("Minimize_Distance", LpMinimize)

# Define decision variables
x = LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function
prob += lpSum(x[i, j] * distance(cities[i], cities[j]) for i in cities for j in cities if i != j)

# Constraints
# Each city is connected exactly once
for j in cities:
    prob += lpSum(x[i, j] for i in cities if i != j) == 1, f"Enter_{j}"
    prob += lpSum(x[j, i] for i in cities if i != j) == 1, f"Leave_{j}"

# Exactly num_robots leave from the initial depot
prob += lpSum(x[0, j] for j in cities if j != 0) == num_robots, "Robots_from_depot"

# Solve the model
prob.solve()

# Collect results if successful
if LpStatus[prob.status] == 'Optimal':
    routes = {i: [] for i in range(num_robots)}
    node_visited = {i: False for i in cities}
    route_costs = {}

    current_node = 0
    for k in range(num_robots):
        path = []
        total_cost = 0
        while True:
            next_city = [j for j in cities if j != current_node and x[current_node, j].varValue == 1][0]
            path.append(next_city)
            total_cost += distance(cities[current_node], cities[next_city])
            current_node = next_city
            if current_node == 0:
                break
        routes[k] = path
        route_costs[k] = total_cost

    # Displaying the output
    total_cost_all_routes = 0
    for robot_id, city_list in routes.items():
        if city_list:
            tour_path = [0] + city_list + [0]
            print(f"Robot {robot_id} Tour: {tour_path}")
            print(f"Robot {robot_id} Total Travel Cost: {route_costs[robot;)_id]}")
            total_cost_all_routes += route_costs[robot_id]
    print(f"Overall Total Travel Cost: {total_cost_all_routes}")

else:
    print(f"Failed to find a solution. Status: {LpStatus[prob.status]}")