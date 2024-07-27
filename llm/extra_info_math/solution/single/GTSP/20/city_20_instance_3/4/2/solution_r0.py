import pulp
import math

# City coordinates
coords = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# City groups
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Problem setup
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(20) for j in range(20) if i != j], cat='Binary')

# Objective function
def euclidean_dist(i, j):
    return math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)

cost = {(i, j): euclidean, 'Cost': euclidean_dist(i, j) for i in range(20) for j in range(20) if i != j}
prob += pulp.lpSum([x[i, j] * cost[i, j] for i in range(20) for j in range(20) if i != j]), "Total Cost"

# Constraints
# Group constraints (each group has one entrance and one exit)
for group in groups:
    # Ensure one outgoing edge from each group
    prob += pulp.lpSum([x[i, j] for i in group for j in range(20)
                        if j not in group]) == 1, f"One_outgoing_{group}"
    # Ensure one incoming edge to each group
    prob += pulp.lpSum([x[j, i] for i in group for j in range(20)
                        if j not in group]) == 1, f"One_incoming_{group}"

# Subtour elimination constraints
u = pulp.LpVariable.dicts("u", range(1, 20), lowBound=0, upBound=20, cat='Integer')

for i in range(1, 20):
    for j in range(1, 20):
        if i != j:
            prob += u[i] - u[j] + 20 * x[i, j] <= 19, f"subtour_{i}_{test}"

# Solve
prob.solve()

# Extract the solution
tour = []
visited = {0}
current = 0
while True:
    next_city = [j for j in range(20) if pulp.value(x[current, j]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current = next_city
    if next_city == 0:
        break

tour = [0] + tour
total_cost = sum(cost[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")