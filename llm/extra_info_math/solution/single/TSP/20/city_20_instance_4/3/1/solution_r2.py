import pulp
import math
import itertools

# City positions
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

n = len(cities)

# Define distance calculation
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function: Minimize the total travel cost
model += pulp.lpSum(distance(i, j) * x[i, j] for i in cities for j in cities if i != j)

# Constraints:
for i in cities:
    model += pulp.lpSum(x[i, j] for j in cities if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in cities if i != j) == 1

# Subtour elimination using Miller-Tucker-Zemlin
u = pulp.LpVariable.dicts("u", cities, lowBound=0, upBound=len(cities)-1, cat='Continuous')
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extracting the solution
tour = []
current_city = 0
while len(tour) < n:
    for j in cities:
        if j != current_city and pulp.value(x[(current_city, j)]) == 1:
            tour.append(j)
            current_city = j
            break
if current_city != 0:
    tour.append(0)  # ensure to return to depot

# Calculate total cost based on the tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")