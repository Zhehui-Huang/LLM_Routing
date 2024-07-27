import pulp
import math

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# City groups
groups = [
    [1, 4], [2, 6], [7], [5], [9], [8], [3]
]

# Distance function using Euclidean distance between two cities
def distance(ci, cj):
    xi, yi = cities[ci]
    xj, yj = cities[cj]
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

# Create a PuLP problem
problem = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Variable indicating whether path (i, j) is used
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities}

# Objective: Minimize total distance traveled
problem += pulp.lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j)

# Constraint: Each city must be visited exactly once, except for depot 0
for group in groups:
    # One outgoing from each group chosen
    problem += pulp.lpSum(x[g, j] for g in group for j in cities if j not in group) == 1
    # One incoming to each group chosen
    problem += pulp.lpSum(x[j, g] for g in group for j in cities if j not in group) == 1

# Subtour elimination constraints for subtour prevention
u = {i: pulp.LpVariable(f"u_{i}", lowBound=1, upBound=len(groups)) for i in cities if i != 0}
for group in groups:
    for i in group:
        for j in group:
            if i != j:
                problem += u[i] - u[j] + len(group) * x[i, j] <= len(group) - 1

# Ensure the tour starts and ends at depot (0)
problem += pulp.lpSum(x[0, j] for j in cities if j != 0) == 1
problem += pulp.lpSum(x[i, 0] for i in cities if i != 0) == 1

# Solve the problem
problem.solve()

# Retrieve the optimal tour order starting and ending at the depot
current = 0
tour = [current]
cost = 0.0
visited = set(tour)

while True:
    found = False
    for j in cities:
        if j != current and pulp.value(x[current, j]) == 1 and j not in visited:
            tour.append(j)
            cost += distance(current, j)
            current = j
            visited.add(current)
            found = True
            break
    if not found:
        tour.append(0)
        cost += distance(current, 0)
        break

# Print the solution
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")