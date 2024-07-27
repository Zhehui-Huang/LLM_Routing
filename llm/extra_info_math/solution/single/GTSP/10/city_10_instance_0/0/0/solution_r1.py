import pulp
import math

# Define cities and their coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Groups of cities
groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Number of groups
k = len(groups)

# Calculate Euclidean distances between cities
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Cost dictionary
costs = {}
for i in cities:
    for j in cities:
        if i != j:
            costs[(i, j)] = distance(cities[i], cities[j])

# Setup problem
prob = pulp.LpProblem("robot_tour", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum([costs[(i, j)] * x[(i, j)] for i in cities for j in cities if i != j]), "Total_Cost"

# Constraints for meeting group visit requirements
for index, group in enumerate(groups):
    prob += pulp.lpSum([x[i, j] for i in group for j in cities if j not in group]) == 1, f"One_outgoing_from_group_{index}"
    prob += pulp.lpSum([x[j, i] for i in group for j in cities if j not in group]) == 1, f"One_incoming_to_group_{index}"

# Flow conservation constraints
for i in cities:
    prob += (
        pulp.lpSum(x[i, j] for j in cities if j != i) ==
        pulp.lpSum(x[j, i] for j in cities if j != i)
    ), f"Flow_conservation_at_node_{i}"

# Subtour elimination constraints
u = pulp.LpVariable.dicts("u", range(1, 1 + k), lowBound=0, cat='Continuous')
for p in range(k):
    for q in range(k):
        if p != q:
            prob += (
                u[p+1] - u[q+1] + k * pulp.lpSum(x[i, j] for i in groups[p] for j in groups[q])
                + (k-2) * pulp.lpSum(x[j, i] for i in groups[p] for j in groups[q]) <= k-1
            ), f"Subtour_{p}_{q}"

# Solve problem
status = prob.solve()

if status == pulp.LpStatusOptimal:
    print("Status:", pulp.LpStatus[status])
    
    # Prepare output (using results)
    tour = [0]
    current_city = 0
    visited = set([0])
    for _ in range(len(groups) + 1):
        next_cities = [j for j in cities if j not in visited and pulp.value(x[current_city, j]) == 1]
        if next_cities:
            next_city = next_cities[0]
            tour.append(next_city)
            visited.add(next_city)
            current_city = next_city

    # Closing the loop back to depot
    tour.append(0)

    # Get total travel cost
    total_cost = pulp.value(prob.objective)

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("An optimal solution was not found.")