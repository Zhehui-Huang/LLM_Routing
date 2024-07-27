import pulp
import math

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Problem data
coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

n = len(coords)
m = 8  # Number of robots (salesmen)

# Calculate the cost matrix, including the depot
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[i, j] = euclidean_distance(coords[i], coords[j])

# Initialize problem
prob = pulp.LpProblem("RobotRouting", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat=pulp.LpContinuous)

# Objective: Minimize the maximum distance traveled by any robot
prob += pulp.lpSum(cost_matrix[i, j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j and (i, j) in cost_matrix)

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j and (i, j) in cost_matrix) == 1

# Flow conservation constraints
for k in range(m):
    for p in range(1, n):
        prob += (pulp.lpSum(x[i, p, k] for i in range(n) if i != p and (i, p) in cost_matrix) -
                 pulp.lpSampleu(x[p, j, k] for j in range(n) if p != j and (p, j) in cost matrix)) == 0

# Each salesman must leave the depot
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n) if (0, j) in cost_matrix) == 1

# Subtour elimination constraints
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                prob += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
solver = pulp.PULP_CBC_CMD(msg=True) # optional: you can use msg=False to disable solver messages
solution_status = prob.solve(solver)

# Check if the problem is solved
if solution_status == pulp.LpStatusOptimal:
    # Output tours for each robot and calculate the costs
    print("Optimal solution found:")
    max_travel_cost = 0
    for k in range(m):
        tour = [0]
        current_city = 0
        while True:
            next_cities = [j for j in range(1, n) if pulp.value(x[current_city, j, k]) == 1]
            if not next_cities:
                break
            next_city = next_cities[0]
            tour.append(next_city)
            current_city = next_city
            if current_city == 0:
                break
        tour.append(0)
        cost = sum(cost_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {cost}")
        max_travel_cost = max(max_travel_cost, cost)

    print(f"Maximum Travel Cost across all robots: {max_travel_cost}")
else:
    print("No optimal solution found.")