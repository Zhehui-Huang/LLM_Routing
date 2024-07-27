import itertools
from pulp import LpProblem, LpVariable, LpMinimize, LpBinary, lpSum, LpStatus

# Helper function to calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Coordinates of the cities
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

n = len(cities)  # Number of cities

# Compute pairwise distances
distances = {(i, j): distance(ci, cj) for i, ci in cities.items() for j, cj in cities.items()}

# Create the problem
prob = LpProblem("MinimaxTSP", LpMinimize)

# Decision variables x_ij
x = LpVariable.dicts("x", [(i,j) for i in cities for j in cities if i != j], 0, 1, LpBinary)

# Auxiliary variable for the maximum distance in a single travel step
max_dist = LpVariable("max_dist", lowBound=0)

# Objective function
prob += max_dist

# Constraints
# Each city must be entered and exited exactly once
for i in cities:
    prob += lpSum(x[j, i] for j in cities if j != i) == 1
    prob += lpSum(x[i, j] for j in cities if j != i) == 1

# Subtour elimination
subsets = [s for s in itertools.combinations(cities, r) for r in range(2, n)]
for s in subsets:
    prob += lpSum(x[i, j] for i in s for j in s if i != j) <= len(s) - 1

# Maximizing distance condition
for i, j in x:
    prob += x[i, j] * distances[i, j] <= max_dist

# Solve the problem
status = prob.solve()

# Check for an optimal solution
if LpStatus[status] == 'Optimal':
    # Extract the solution
    solution = {(i,j): x[i,j].varValue for i, j in x}
    tour = []
    current = 0
    while len(tour) < n:
        for k, v in solution.items():
            if k[0] == current and v > 0.99:
                current = k[1]
                tour.append(current)
                break

    # Make tour cyclic
    tour = [0] + tour

    # Compute total cost and maximum distance
    total_distance = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    max_trip_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_distance)
    print("Maximum distance between consecutive cities:", max_trip_distance)
else:
    print("No optimal solution found.")