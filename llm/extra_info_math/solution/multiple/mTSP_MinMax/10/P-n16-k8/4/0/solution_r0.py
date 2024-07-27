import pulp
import math

# Given data
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
num_robots = 8
n = len(coordinates)  # Total cities
num_cities = n - 1  # Exclude depot

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j])
             for i in coordinates.keys() for j in coordinates.keys() if i != j}

# Problem instance
model = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Decision variables
x = {(i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary')
     for i in range(n) for j in range(n) for k in range(num_robots) if i != j}

u = {i: pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in range(1, n)}

# Objective: minimize the maximum travel cost among robots
max_distance = pulp.LpVariable("max_distance")
model += max_distance

# Constraints
# Each city is visited exactly once by exactly one robot
for j in range(1, n):
    model += sum(x[i, j, k] for i in range(n) for k in range(num_robots) if i != j) == 1

# Ensure each salesman leaves and returns to the depot
for k in range(num_robots):
    model += sum(x[0, j, k] for j in range(1, n)) == 1  # Leave depot
    model += sum(x[j, 0, k] for j in range(1, n)) == 1  # Return to depot

# Flow conservation for each salesman at each city
for k in range(num_robots):
    for j in range(1, n):
        model += (sum(x[i, j, k] for i in range(n) if i != j) ==
                  sum(x[j, i, k] for i in range(n) if i != j))

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(num_robots):
                model += (u[i] - u[j] + n * x[i, j, k] <= n - 1)

# Distance constraints under the max_distance
for k in range(num_robots):
    model += sum(distances[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= max_distance

# Solve the problem using PuLP's choice of solver
model.solve()

# Output results
if model.status == pulp.LpStatusOptimal:
    print(f"Status: {pulp.LpStatus[model.status]}")
    total_tour_cost = [[0] * num_robots for i in range(num_robots)]

    for k in range(num_robots):
        tour = [0]
        while True:
            for j in range(n):
                if pulp.value(x[tour[-1], j, k])==1:
                    tour.append(j)
                    total_tour_cost[k] += distances[tour[-2], tour[-1]]
                    break
            if tour[-1] == 0:  # Back to the depot
                break

        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {total_tour_cost[k]}")

    print(f"Maximum Travel Cost: {pulp.value(max_distance)}")
else:
    print("The problem is infeasible.")