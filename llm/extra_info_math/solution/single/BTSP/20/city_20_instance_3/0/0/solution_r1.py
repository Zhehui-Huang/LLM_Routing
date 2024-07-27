import pulp
import math

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

N = len(cities)
distances = {(i, j): math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2) for i in range(N) for j in range(N) if i != j}

# Define the problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j) for (i, j) in distances.keys()), 0, 1, pulp.LpBinary)
M = pulp.LpVariable("M", lowBound=0, cat='Continuous')

# Objective
prob += M

# Constraints
for i in range(N):
    prob += pulp.lpSum(x[(i, j)] for j in range(N) if (i, j) in x) == 1  # leave each city only once
    prob += pulp.lpSum(x[(j, i)] for j in range(N) if (j, i) in x) == 1  # enter each city only once

for (i, j) in x:
    prob += x[(i, j)] * distances[(i, j)] <= M

# Subtour elimination
for S in range(2, N):
    for subset in combinations(range(1, N), S):
        prob += pulp.lpSum(x[(i, j)] for i in subset for j in subset if (i, j) in x) <= len(subset) - 1

# Solve the problem
solver = pulp.PULP_CBC_CMD(msg=False)
status = prob.solve(solver)

# Output results
tour = []
current_city = 0
sequence_cities = {current_city: 0}

while len(sequence_cities) < N:
    for j in range(N):
        if j != current_city and x[(current_city, j)].varValue == 1:
            sequence_cities[j] = 0
            tour.append(j)
            current_city = j
            break

if status == pulp.LpStatusOptimal:
    # Create the round trip by appending the start city
    tour.insert(0, 0)
    tour.append(0)

    # Calculating total distance and max distance between consecutive cities
    total_distance = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    max_distance = max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    
    print("Tour:", tour)
    print("Total travel cost:", total_distance)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("Could not find an optimal tour.")