import pulp
import math
import itertools

# Given city coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

n = len(coordinates)  # Number of cities including depot

# Create the problem variable:
problem = pulp.LpProblem('TSP_Minimize_Max_Distance', pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
d_max = pulp.LpVariable("d_max", lowBound=0, cat='Continuous')

# Objective
problem += d_max

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination
for m in range(2, n):
    for subset in itertools.combinations(range(1, n), m): # Not including depot in subsets
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * euclidean_distance(i, j) <= d_max

# Solve the problem using the CBC solver
solver = pulp.PULP_CBC_CMD(msg=True)
result = problem.solve(solver)

# Check if there is an optimal solution
if pulp.LpStatus[problem.status] == 'Optimal':
    tour = []
    current_location = 0
    steps_remaining = n-1
    
    while steps_remaining > 0:
        for j in range(n):
            if j != current_location and pulp.value(x[current_location, j]) == 1:
                tour.append(j)
                current_location = j
                steps_remaining -= 1
                break
                
    tour = [0] + tour + [0]  # Include the return to depot

    # Calculate total travel cost and maximum distance
    total_travel_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    max_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

    # Display results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {pulp.value(d_max):.2f}")
else:
    print("No optimal solution found.")