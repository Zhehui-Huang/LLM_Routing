import pulp
import math

# Define the cities coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

n = len(cities)  # Total nodes, including depot
m = 2  # Number of robots

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Setting up the optimization problem
problem = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, n), 0, n-1, pulp.LpContinuous)

# Objective function: Minimize the total distance traveled by all robots
problem += pulp.lpSum(distance(i, j) * x[(i, j, k)] for i in range(n) for j in range(n) if i != j for k in range(m))

# Constraints
# Each city (excluding the depot) is visited exactly once by exactly one robot
for j in range(1, n):
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j for k in range(m)) == 1

# Each robot departs from and arrives at the depot
for k in range(m):
    problem += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1  # Departing
    problem += pulp.lpSum(x[(j, 0, k)] for j in range(1, n)) == 1  # Arriving

# Flow conservation: enter and leave each city
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j) == pulp.lpSum(x[(j, i, k)] for i in range(n) if i != j)

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[(i, j, k)] <= n - 1

# Solve the problem
problem.solve()

# Check the solution
if problem.status == pulp.LpStatusOptimal:
    solution = {}
    travel_costs = []
    for k in range(m):
        path = [0]
        while len(path) < n:
            i = path[-1]
            next_cities = [j for j in range(n) if pulp.value(x[i, j, k]) == 1]
            if next_cities:
                path.append(next_cities[0])
            else:
                break
        path.append(0)  # Return to the depot
        solution[k] = path
        robot_cost = sum(distance(path[i], path[i + 1]) for i in range(len(path) - 1))
        travel_costs.append(robot_cost)
        print(f"Robot {k} Tour: {path}")
        print(f"Robot {k} Total Travel Cost: {robot_cost}")
    
    print(f"Overall Total Travel Cost: {sum(travel_costs)}")
else:
    print("No optimal solution found.")