import math
import pulp

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35)
}

# Distance Calculation Function
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Number of Robots and Depots
num_robots = 2
depots = [0, 1]
num_cities = len(cities)

# Create the optimization problem
model = pulp.LpProblem("Minimize_Total_Travel_Cost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("Route", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
u = pulp.LpVariable.dicts("Position", (i for i in cities), lowBound=2, upBound=num_cities, cat='Integer')

# Objective Function
model += pulp.lpSum(distance(i, j) * x[(i, j)] for i in cities for j in cities if i != j)

# Constraints
for j in cities:
    if j not in depots:
        # Ensure customer nodes are visited exactly once
        model += pulp.lpSum(x[(i, j)] for i in cities if i != j) == 1
        model += pulp.lpSum(x[(j, i)] for i in cities if i != j) == 1

# Subtour elimination constraints (SEC) for non-depot cities
for i in cities:
    for j in cities:
        if i != j:
            model += u[i] - u[j] + (num_cities - 1) * x[(i, j)] <= num_cities - 2

# Subtour constraints at depot for robots
for k in depots:
    model += pulp.lpSum(x[(k, j)] for j in cities if j != k) == num_robots
    model += pulp.lpSum(x[(j, k)] for j in cities if j != k) == num_robots

# Solve the problem
solver = pulp.PULP_CBC_CMD(msg=False)
model.solve(solver)

# Extract the routes
routes = {robot: [] for robot in depots}
for robot in depots:
    for (i, j) in x:
        if x[(i, j)].varValue == 1:
            routes[robot].append((i, j))

# Convert arc list to path list and calculate the costs
robot_tour_details = []
overall_total_travel_cost = 0

for robot, arcs in routes.items():
    if arcs:
        # Start from depot
        current_location = robot
        start_depot = robot
        tour = [current_location]
        tour_cost = 0
        while arcs:
            for arc in arcs:
                if arc[0] == current_location:
                    tour_cost += distance(arc[0], arc[1])
                    current_location = arc[1]
                    tour.append(current_location)
                    arcs.remove(arc)
                    break
        tour.append(start_depot)  # Return to start depot if needed
        tour_cost += distance(current_location, start_depot)
        robot_tour_details.append((robot, tour, tour_cost))
        overall_total_travel_cost += tour_cost

# Output result
for robot, tour, cost in robot_tour_details:
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_travel_cost}")