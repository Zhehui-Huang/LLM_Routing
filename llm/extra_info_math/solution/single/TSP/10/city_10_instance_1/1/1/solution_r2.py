import pulp
import numpy as np

# Define city coordinates (0-based index where index 0 is the depot)
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Number of cities including the depot
n = len(cities)

# Euclidean distance calculator
def euclidean_distance(pt1, pt2):
    return np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

# Cost dictionary
cost = {(i, j): euclidean_distance(cities[i], cities[j])
        for i in range(n) for j in range(n) if i != j}

# LP Problem Initialization
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_{ij} = 1 if the tour includes going from i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), 
                          cat=pulp.LpBinary, lowBound=0, upBound=1)

# Objective
problem += pulp.lpSum(x[(i, j)] * cost[(i, j)] for i in range(n) for j in range(n) if i != j)

# Constraints
# Enter each city exactly once
for j in range(1, n):  # start from 1 to exclude depot
    problem += pulp.lpSum(x[(i, j)] for i in range(n) if i != j) == 1

# Leave each city exactly once
for i in range(1, n):  # start from 1 to exclude depot
    problem += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1

# Subtour Elimination Constraints
u = pulp.LpVariable.dicts('u', range(1, n), lowBound=0, cat=pulp.LpContinuous)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1) * x[(i, j)] <= (n-2)

# Solve the problem
status = problem.solve()

if status == pulp.LpStatusOptimal:
    print("Tour Found")
    solution = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[(i, j)]) == 1]
    
    path = [0]
    current_city = 0
    while len(path) < n:
        for next_city in range(n):
            if (current_city, next_city) in solution:
                path.append(next_city)
                solution.remove((current_city, next_city))
                current_city = next_load
                break
                
    path.append(0)  # Completing the cycle to return to starting city (depot)
    
    total_distance = sum(cost[(path[i], path[i+1])] for i in range(len(path)-1))
    print(f"Tour: {path}")
    print(f"Total travel cost: {total_distance}")
else:
    print("No optimal solution found.")