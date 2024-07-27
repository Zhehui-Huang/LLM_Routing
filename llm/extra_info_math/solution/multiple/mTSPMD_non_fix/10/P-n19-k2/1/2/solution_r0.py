import pulp
import math

# Coordinates of cities with index
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35),
}

# Calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Number of depots and nodes (cities)
n = len(cities)
depots = {0, 1}
robots = 2

# Create the optimization problem
problem = pulp.LpProblem("Multiple_TSP_Problem", pulp.LpMinimize)

# Binary variables indicating if arc (i, j) is used on a route from city i to j
x = pulp.LpVariable.dicts("x",
                          ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')

# Position of the city in the tour
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, cat='Continuous')

# Objective: Minimize the total distance traveled
problem += pulp.lpSum(distance(i, j) * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Each city j must be entered and left exactly once
for j in range(n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for i in range(n) if i != j) == 1

# Subtour elimination
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i, j] <= n-1

# Each robot starts from depot 0 initially
problem += pulp.lpSum(x[0, j] for j in range(n) if j != 0) == robots

# Solve the problem
status = problem.solve()

# Output results
if status == pulp.LpStatusOptimal:
    print("Optimal solution found.")
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[i, j]) > 0.5:
                print(f"Robot travels from city {i} to city {j}")
else:
    print("No optimal solution found.")