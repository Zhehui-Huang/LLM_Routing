import pulp
import math

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Function to calculate the Euclidean distance
def distance(coord1, coord2):
    return round(math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2), 2)

# Creating distance matrix
n = len(cities)
distance_matrix = {}
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = distance(cities[i], cities[j])

# Define the problem
model = pulp.LpProblem("TSP_Robots", pulp.LpMinimize)

# Variables: x[i][j] is 1 if city i is connected to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective
model += pulp.lpSum(distance_matrix[i, j] * x[i, j] for i in cities for j in cities if i != j)

# Constraints

# Each city is visited exactly once
for j in cities:
    model += pulp.lpSum(x[i, j] for i in cities if i != j) == 1, f"enter_{j}"
    model += pulp.lpSum(x[j, i] for i in cities if i != j) == 1, f"leave_{j}"

# Subtour elimination (Miller-Tucker-Zemlin formulation)
u = pulp.LpVariable.dicts("u", (i for i in cities), lowBound=0, upBound=len(cities) - 1, cat='Integer')
for i in cities:
    for j in cities:
        if i != j and (i != 0 and j != 0):  # exclude depot
            model += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Solve the model
model.solve(pulp.PULP_CBC_CMD(msg=1))

if model.status == pulp.LpStatusOptimal:
    print(f"Status: {pulp.LpStatus[model.status]}")
    total_cost = 0
    for k in range(8):  # each robot from each depot
        tour = [k]
        next_city = k
        costs = []
        visited = set(tour)
        while True:
            next_cities = [(j, distance_matrix[next_city, j]) for j in cities if not j in visited and j != next_city]
            if not next_cities:
                break
            next_city, cost = min(next_cities, key=lambda x: x[1])
            visited.add(next_city)
            tour.append(next_city)
            costs.append(cost)
            if len(tour) > 1 and tour[-1] == k:
                break
        tour.append(k)
        costs.append(distance_matrix[tour[-2], k])
        total_cost += sum(costs)
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {sum(costs)}")
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("The problem does not have an optimal solution.")