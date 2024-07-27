import pulp
import math
import itertools

def euclid_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities coordinates
coordinates = {
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

n = len(coordinates)
cost = {(i, j): euclid_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n)}

# Problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective
prob += pulp.lpSum(cost[i, j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += (pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1)
    prob += (pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1)

# Subtour Elimination
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve
prob.solve()

# Check if a feasible solution was found
if pulp.LpStatus[prob.status] == 'Optimal':
    # Finding the tour from the decision variables
    tour = []
    current = 0
    count = 0
    while count < n:
        for i in range(n):
            if x[current, i].varValue == 1:
                tour.append(current)
                current = i
                count += 1
                break

    # Append the return to the depot
    tour.append(0)

    # Calculate the total cost
    total_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
else:
    print("No optimal solution found. Status:", pulp.LpStatus[prob.status])