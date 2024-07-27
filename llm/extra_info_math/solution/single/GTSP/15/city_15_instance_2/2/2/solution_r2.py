import pulp
import math

# Helper function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Define the cities with their coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Define the city groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Define variables
group_nodes = [0] + [i for i, group in enumerate(groups, start=1) for _ in group]
city_indices = [0] + [city for group in groups for city in group]
N = len(city_indices)

# Index mapping
index_to_city = {i: city for i, city in enumerate(city_indices)}

# Setting up the problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in range(N) for j in range(N) if i != j}

# Objective function
prob += pulp.lpSum(distance(cities[index_to_city[i]], cities[index_to_city[j]]) * x[i, j] for i in range(N) for j in range(N) if i != j)

# Constraints

# Establish that exactly one link exits from each group node (incoming and outgoing)
for k in range(1, len(groups)+1):
    nodes_in_group = [i for i, x in enumerate(group_nodes) if x == k]
    prob += pulp.lpSum(x[i, j] for i in nodes_in_group for j in range(N) if j not in nodes_in_group) == 1
    prob += pulp.lpSum(x[j, i] for i in nodes_in_group for j in range(N) if j not in nodes_in_group) == 1

# Ensure that the path enters and leaves each node exactly once
for i in range(1, N):
    prob += pulp.lpSum(x[i, j] for j in range(N) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(N) if i != j) == 1

# Solving the problem
result_status = prob.solve()

# Output results
if result_status == pulp.LpStatusOptimal:
    tour = []
    while True:
        if not tour:
            active = 0
        else:
            active = next_idx
        
        for j in range(N):
            if pulp.value(x[active, j]) == 1:
                tour.append(index_to_city[j])
                next_idx = j
                break
        if next_idx == 0:
            break
    
    total_cost = pulp.value(prob.objective)
    print("Tour:", [0] + tour)
    print("Total travel cost:", total_cost)
else:
    print("Failed to solve the problem optimally")