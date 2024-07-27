import pulp
import math

# Fixed coordinates including the depot
cities = [
    (16, 90),  # Depot
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

# Function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Define the problem
problem = pulp.LpProblem("TSP_Special", pulp.LpMinimize)

# Decision variables x[(i, j)] for each possible route between cities
x = {}
for i in range(len(cities)):
    for j in range(len(cities)):
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat="Binary")

# Objective: Minimize total travel cost
objective = pulp.lpSum(distance(cities[i], cities[j]) * x[(i, j)] for i in range(len(cities)) for j in range(len(cities)) if i != j)
problem += objective

# Constraints for each group to have exactly one outgoing and incoming connection
for group in city_groups:
    problem += pulp.lpSum(x[(i, j)] for i in group for j in range(len(cities)) if j not in group) == 1
    problem += pulp.lpSum(x[(j, i)] for i in group for j in range(len(cities)) if j not in group) == 1

# Adding a flow conservation constraint for each city except the depot
for i in range(1, len(cities)):
    problem += pulp.lpSum(x[(i, j)] for j in range(len(cities)) if i != j) - pulp.lpSum(x[(j, i)] for j in range(len(cities)) if i != j) == 0

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Checking the problem status
if status != pulp.LpStatusOptimal:
    print("Problem not solved to optimality")
else:
    print("Optimal solution found")

# If optimal, extract tour
if status == pulp.LpStatusOptimal:
    tour = []
    current_city = 0
    tour.append(current_city)
    total_cost = 0
    for _ in range(len(city_groups)):
        next_cities = [j for j in range(len(cities)) if pulp.value(x[(current_city, j)]) == 1]
        if len(next_cities) == 1:
            next_city = next_cities[0]
            tour.append(next_city)
            total_cost += distance(cities[current_city], cities[next_city])
            current_city = next_city
    
    # Add return to depot
    tour.append(0)
    total_cost += distance(cities[current_city], cities[0])

    # Output results
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))