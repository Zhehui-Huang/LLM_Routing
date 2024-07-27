import pulp
import math

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups of cities
groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Number of Groups
k = len(groups)

# Flatten list of city group members
all_group_cities = [city for sublist in groups.values() for city in sublist]

# Distance calculation function
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Setting up the problem
problem = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Decision variables x_{ij}
x = {(i, j): pulp.LpVariable(cat=pulp.LpBinary, name=f"x_{i}_{j}") for i in cities for j in cities if i != j}

# Objective function
problem += pulp.lpSum(x[i, j] * calculate_distance(i, j) for i in cities for j in cities if i != j), "Total_Distance"

# Constraints for ensuring connection between groups
for i, group in groups.items():
    problem += pulp.lpSum(x[j, i] for j in cities if j not in group for i in group) == 1, f"Out_Constraint_{i}"
    problem += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1, f"In_Constraint_{i}"

# Flow conservation constraint
for i in cities:
    problem += (pulp.lpSum(x[j, i] for j in cities if j != i) == pulp.lpSum(x[i, j] for j in cities if j != i)), f"Flow_Constraint_{i}"

# Solve the problem
problem.solve()

# Extract the solution
tour = []
total_cost = 0

# Starting at depot 0
current_city = 0
tour.append(current_city)
visited = set(tour)

# Find the path according to the x_ij variables
for _ in range(len(cities)):
    for next_city in cities:
        if next_city != current_city and x[current_city, next_city].value() == 1:
            total_cost += calculate_distance(current_city, next_city)
            tour.append(next_city)
            current_city = next_city
            break
    if current_city == 0:
        break

# Adding depot at the end of the tour
if tour[-1] != 0:
    tour.append(0)
    total_mxost += calculate_distance(tour[-2], 0)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")