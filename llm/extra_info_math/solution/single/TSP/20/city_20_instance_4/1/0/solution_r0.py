import pulp
import math

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculating Euclidean distances
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = {(i, j): euclidean for i in cities for j in cities if i != j}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Defining the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}

# Objective
prob += pulp.lpSum(distances[i, j] * x[i, j] for i in cities for j in cities if i != j)

# Constraints
for i in cities:
    # Arriving at each city
    prob += pulp.lpSum(x[j, i] for j in cities if i != j) == 1
    # Departing each city
    prob += pulp.lpSum(x[i, j] for j in cities if i != j) == 1

# Subtour elimination
for i in range(1, len(cities)):
    for j in range(i+1, len(cities)):
        prob += x[i, j] + x[j, i] <= 1

# Solving the problem
prob.solve()

# Extracting the solution
tour = [0]
current = 0
while len(tour) < len(cities):
    for j in cities:
        if x[current, j].varValue == 1 and j not in tour:
            tour.append(j)
            current = j
            break
tour.append(0)

# Calculating the total tour travel cost
total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")