import pulp
import math

# City coordinates indexed from 0 through 19, total 20 cities
coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

N = len(coordinates)

# Distance calculation between each pair of cities
def distance(i, j):
    xi, yi = coordinates[i]
    xj, yj = coordinates[j]
    return math.sqrt((xi - xj)**2 + (yi - yj)**2)

# Define the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(N) for j in range(N) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(N)), lowBound=0, upBound=N-1, cat='Continuous')

# Objective: Minimize the maximum distance traveled in any single trip between cities
prob += pulp.lpSum(x[(i, j)] * distance(i, j) for i in range(N) for j in range(N) if i != j)

# Constraints
for i in range(N):
    prob += pulp.lpSum(x[(i, j)] for j in range(N) if i != j) == 1  # Leave each city only once
    prob += pulp.lpSum(x[(j, i)] for j in range(N) if i != j) == 1  # Enter each city only once

# Subtour elimination (Miller-Tucker-Zemlin formulation)
for i in range(1, N):
    for j in range(1, N):
        if i != j:
            prob += u[i] - u[j] + N * x[(i, j)] <= N - 1

# Solve the problem
status = prob.solve()

# Collect the result
tour = []
if pulp.LpStatus[status] == 'Optimal':
    for i in range(N):
        next_city = [j for j in range(N) if i != j and pulp.value(x[(i, j)]) == 1]
        if next_city:
            tour.append(next_city[0])

    # Return to starting point
    tour = [0] + tour + [0]
    
    # Calculate total and maximum distances
    total_dist = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    max_dist = max(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_dist)
    print("Maximum distance between consecutive cities:", max_dist)
else:
    print("Failed to find an optimal solution.")