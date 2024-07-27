import pulp
import math

# City coordinates (index 0 is the depot)
cities = [
    (16, 90), # Depot
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# City groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Set up the LP problem
problem = pulp.LpProblem("MinCost_TSP_Variant", pulp.LpMinimize)

# x[(i, j)] = 1 if route (i, j) is used
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(cities)) for j in range(len(cities)) if i != j), cat="Binary")

# Constraint for one outgoing connection from each group
for group in city_groups:
    problem += pulp.lpSum(x[(i, j)] for i in group for j in range(len(cities)) if j not in group) == 1

# Constraint for one incoming connection to each group
for group in city_groups:
    problem += pulp.lpSum(x[(j, i)] for i in group for j in range(len(cities)) if j not in group) == 1

# Flow conservation
for city in range(1, len(cities)):
    problem += (pulp.lpSum(x[(j, city)] for j in range(len(cities)) if j != city) 
                == pulp.lpSum(x[(city, j)] for j in range(len(cities)) if j != city))

# Objective function
problem += pulp.lpSum(distance(cities[i], cities[j]) * x[(i, j)] for i in range(len(cities)) for j in range(len(cities)) if i != j)

# Subtour Elimination
u = pulp.LpVariable.dicts("u", (i for i in range(1, len(cities))), lowBound=0, cat="Continuous")

for i in range(1, len(cities)):
    for j in range(1, len(cities)):
        if i != j:
            problem += u[i] - u[j] + (len(cities) - 1) * x[(i, j)] <= len(cities) - 2

# Solve the problem
problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract the tour
tour = [0]
current = 0
total_cost = 0

for _ in range(len(city_groups)):
    next_city = next(j for j in range(len(cities)) if pulp.value(x[(current, j)]) == 1 and current != j)
    total_cost += distance(cities[current], cities[next_city])
    tour.append(next_city)
    current = next_city

tour.append(0)  # Returning to the depot
total_cost += distance(cities[current], cities[0])

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)