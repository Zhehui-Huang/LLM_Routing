import math
import pulp

# City coordinates
city_coords = {
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
city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Calculating Euclidean distances between every pair of cities
def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + (city_coords[city1][1] - city_coords[city2][1])**2)

distances = {}
for i in city_coords:
    for j in city_coords:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Setting up the problem: Minimize total distance
problem = pulp.LpProblem("Minimize_Circuit_Distance", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in city_coords for j in city_patterncoords if i != j), cat=pulp.LpBinary)

# Objective
problem += pulp.lpSum(distances[(i, j)] * x[(i, j)] for i in city_coords for j in city_coords if i != j), "Minimize_Total_Distance"

# Constraints
# Build the flow constraints and subtour elimination constraints
# Exactly one incoming and one outgoing connection per selected node
for k, group in city_groups.items():
    problem += pulp.lpSum(x[(i, j)] for i in city_coords for j in group if i != j) == 1
    problem += pulp.lpSum(x[(i, j)] for i in group for j in city_coords if i != j) == 1

for i in city_coords:
    problem += pulp.lpSum(x[(j, i)] for j in city_coords if i != j) - pulp.lpSum(x[(i, k)] for k in city_coords if i != k) == 0

# Subtour elimination constraints using additional variables
u = pulp.LpVariable.dicts("u", (i for i in city_coords if i != 0), lowBound=0, upBound=len(city_coords)-1, cat=pulp.LpInteger)

for i in city_coords:
    for j in city_coords:
        if i != j and i != 0 and j != 0:
            problem += u[i] - u[j] + (len(city_coords)-1) * x[(i, j)] <= len(city_coords) - 2

# Solve the problem
problem.solve()

# Extracting the solution
tour = []
current_node = 0
tour.append(current_node)
found = True
while found:
    found = False
    for j in city_coords:
        if j != current_node and pulp.value(x[(current_node, j)]) == 1:
            tour.append(j)
            current_node = j
            found = True
            break

# Adding the return to the start
tour.append(0) 

# Calculate total travel cost
total_travel_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")