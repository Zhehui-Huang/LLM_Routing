import pulp
import math

# Define city coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Calculate Euclidean distances between cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of Robots
m = 4

# Model
model = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(len(coordinates))
                                for j in range(len(coordinates)) if i != j
                                for k in range(m)), cat='Binary')

u = pulp.LpVariable.dicts("u", ((i) for i in range(1, len(coordinates))),
                          lowBound=0, cat='Continuous')

# Creating a maximal cost variable
max_travel_cost = pulp.LpVariable("max_travel_cost", lowBound=0, cat='Continuous')

# Objective
model += max_travel_cost

# Constraints
# Individual tour cost does not exceed the maximum travel cost
for k in range(m):
    model += pulp.lpSum(x[i, j, k] * distance(coordinates[i], coordinates[j]) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j) <= max_travel ≤ max_travel_cost

# Each city must be visited exactly once by exactly one salesman
for j in range(1, len(coordinates)):
    model += pulp.lpSum(x[(i, j, k)] for i in range(len(coordinates)) if i != j
                        for k in range(m)) == 1

# Enter and leave each city
for k in range(m):
    for j in range(1, len(coordinates)):
        model += pulp.lpSum(x[(i, j, k)] for i in range(len(coordinates)) if i != j) == \
                 pulp.lpSum(x[(j, i, k)] for i in range(len(coordinates)) if i != j)

# Each salesman starts from the depot
for k in range(m):
    model += pulp.lpSum(x[(0, j, k)] for j in range(1, len(coordinates))) == 1

# Subtour elimination
for i in range(1, len(coordinates)):
    for j in range(1, len(coordinates)):
        if i != j:
            for k in range(m):
                model += (u[i] - u[j] + (len(coordinates) - 1) * x[(i, j, k)]) <= (len(coordinates) - 2)

# Solve the model
status = model.solve()

# Check the status
if status == pulp.LpStatusOptimal:
    print(f"Solution is found with status {pulp.LpStatus[status]}")
    tour_costs = []
    for k in range(m):
        tour, cost = [0], 0
        while True:
            found = False
            for j in range(1, len(coordinates)):
                if pulp.value(x[(tour[-1], j, k)]) == 1:
                    tour.append(j)
                    cost += distance(coordinates[tour[-2]], coordinates[tour[-1]])
                    found = True
                    break
            if not found or tour[-1] == 0:
                break
        tour.append(0)  # return to depot
        cost += distance(coordinates[tour[-2]], coordinates[tour[-1]])
        tour_costs.append(cost)
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {cost:.2f}")

    max_cost = max(tour_costs)
    print(f"Maximum Travel Cost: {max_cost:.2f}")
else:
    print("Failed to find an optimal solution.")