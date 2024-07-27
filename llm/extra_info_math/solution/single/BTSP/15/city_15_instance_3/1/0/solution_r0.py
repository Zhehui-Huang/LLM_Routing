import pulp
import math

# Cities' coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

n = len(cities)

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create the problem
prob = pulp.LpProblem("TSP_Min_Max_Inter_City_Distance", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat=pulp.LpBinary)
u = {i: pulp.LpVariable(f"u_{i}", lowBound=1, upBound=n, cat=pulp.LpInteger) for i in cities}
z = pulp.LpVariable("z", lowBound=0, cat=pulp.LpContinuous)

# Objective: minimize the maximum distance in the tour
prob += z, "Minimize the maximum distance between any two consecutive cities"

# Subject to:
# Incoming and outgoing flow constraints
for k in cities:
    prob += pulp.lpSum(x[i, k] for i in cities if i != k) == 1, f"sum_entering_{k}"
    prob += pulp.lpSum(x[k, j] for j in cities if j != k) == 1, f"sum_leaving_{k}"

# Subtour Elimination Constraints
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + n * x[i, j] <= n - 1, f"subtour_cnstr_{i}_{j}"

# Maximum distance constraints
for i in cities:
    for j in cities:
        if i != j:
            prob += x[i, j] * distance(i, j) <= z, f"max_dist_{i}_{j}"

# Solve the problem
status = prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract the results and compute the tour
if pulp.LpStatus[status] == 'Optimal':
    edges = [(i, j) for i in cities for j in cities if i != j and pulp.value(x[i, j]) == 1]
    tour = []
    current_city = 0
    while len(edges) > 0:
        for edge in edges:
            if edge[0] == current_city:
                tour.append(current_city)
                current_city = edge[1]
                edges.remove(edge)
                break
    tour.append(0)  # Return to the depot

    # Calculate the total cost and the maximum distance
    total_cost = sum([distance(tour[i], tour[i+1]) for i in range(len(tour)-1)])
    max_distance = max([distance(tour[i], tour[i+1]) for i in range(len(tour)-1)])
    
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("An optimal solution has not been found.")