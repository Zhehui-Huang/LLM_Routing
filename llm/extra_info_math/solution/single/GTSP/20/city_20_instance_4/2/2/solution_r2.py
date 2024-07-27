import pulp
import math

# Define the cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Define the groups
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Create variables for the problem
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", [g for g in range(len(groups))], lowBound=2, cat='Integer') 

# Initialize the problem
problem = pulp.LpProblem("GroupedTSP", pulp.LpMinimize)

# Objective Function: Minimize the total travel cost
problem += pulp.lpSum(euclidean_distance(i, j) * x[i, j] for i in cities for j in cities if i != j)

# Each cluster must have exactly one outgoing edge to a node outside the cluster
for group_index, group in enumerate(groups):
    problem += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1

# Each cluster must have exactly one incoming edge from a node outside the cluster
for group_index, group in enumerate(groups):
    problem += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

# Subtour elimination constraints
for i in range(1, len(groups)):
    for j in range(1, len(groups)):
        if i != j:
            problem += (u[i] - u[j] + len(groups)*pulp.lpSum(x[p, q] for p in groups[i] for q in groups[j]) <= len(groups) - 1)

# Solve the problem
problem.solve()

# Output the results
if pulp.LpStatus[problem.status] == "Optimal":
    tour = []
    current_city = 0
    tour.append(current_city)
    while True:
        next_cities = [j for j in cities if pulp.value(x[current_city, j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)
        current_city = next_city
        if current_city == 0:
            break
    print(f"Tour: {tour}")
    total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    print(f"Total travel cost: {total_distance:.2f}")
else:
    print("No optimal solution found.")