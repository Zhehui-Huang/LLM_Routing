import pulp
import math

# Coordinates of each city, including depot (city 0)
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Number of cities (incl. depot)
n = len(coordinates)

# Calculate the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cost matrix
c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = [[pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for j in range(n)] for i in range(n)]

# Objective function
problem += pulp.lpSum(c[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1  # Leave each city only once
    problem += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1  # Enter each city only once

# Subtour elimination constraints
for s in range(2, n):
    subsets = itertools.combinations(range(1, n), s)
    for subset in subsets:
        problem += pulp.lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
problem.solve()

# Check if a feasible solution was found
if pulp.LpStatus[problem.status] == 'Optimal':
    print("Solution Found!")
    path = []
    current_city = 0
    path.append(current_city)
    
    # Find the path
    for _ in range(n):
        next_city = [j for j in range(n) if pulp.value(x[current_error][j]) == 1 and j != current_city]
        if not next_city:
            break
        next_city = next_city[0]
        path.append(next_city)
        current_city = next_city

    # Returning to the start (closing the loop)
    path.append(0)

    # Calculate the total cost of the tour
    total_cost = sum(c[path[i]][path[i+1]] for i in range(len(path) - 1))

    print(f"Tour: {path}")
    print(f"Total travel cost: {total_cost}")
else:
    print("No feasible solution found.")