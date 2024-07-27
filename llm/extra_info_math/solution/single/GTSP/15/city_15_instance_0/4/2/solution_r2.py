import pulp
import math

# Define the function to calculate Euclidean distance between two points
def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

# Coordinate definitions and groupings
locations = [
    (9, 93),   # Depot City 0
    (8, 51),   # Group 1, City 1
    (74, 99),  # Group 0, City 2
    (78, 50),  # Group 1, City 3
    (21, 23),  # Group 2, City 4
    (88, 59),  # Group 1, City 5
    (79, 77),  # Group 2, City 6
    (63, 23),  # Group 0, City 7
    (19, 76),  # Group 1, City 8
    (21, 38),  # Group 2, City 9
    (19, 65),  # Group 0, City 10
    (11, 40),  # Group 0, City 11
    (3, 21),   # Group 2, City 12
    (60, 55),  # Group 1, City 13
    (4, 39)    # Group 0, City 14
]

# Total number of cities including the depot
n = len(locations)

# Group definitions including depot
group_ids = {
    0: [0, 2, 7, 10, 11, 14],
    1: [0, 1, 3, 5, 8, 13],
    2: [0, 4, 6, 9, 12]
}

# Create variables
prob = pulp.LpProblem("TSP_Variant", pulp.LpMinimize)

# Decision variables: x_ij = 1 if travel from i to j, else 0
x = pulp.LpVariable.dicts("travel", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function: Minimize total travel distance
prob += pulp.lpSum(euclidean_distance(locations[i], locations[j]) * x[i, j] for i in range(n) for j in range(n) if i != j)

# Visit each group exactly once
for group_id, members in group_ids.items():
    if group_id == 0:  # Only consider groups when traveling from depot
        continue
    prob += pulp.lpSum(x[0][j] for j in members if j != 0) == 1  # exactly one city from the depot

# Ensure one travel to and from each node
for j in range(n):
    prob += pulp.lpSum(x[i][j] for i in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j][i] for i in range(n) if i != j) == 1

# Subtour Prevention Constraints (MTZ formulation)
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=1, upBound=n-1, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n-1) * x[i][j] <= n-2

# Solve the problem
prob.solve()

# Retrieve the results
tour = [0]
current_city = 0
while True:
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[current_city][j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_Provide concise insightstips:city)
    current_city = next_city
    if current_city == 0:
        break

total_distance = sum(euclidean_distance(locations[tour[i]], locations[tour[i + 1]]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)