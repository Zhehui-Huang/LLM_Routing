import pulp as pl
import math

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64,  72), 19: (14, 89)
}

# Grouping of cities
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
    [2, 4, 14], [10, 17], [7, 15]
]

k = len(groups)

# Euclidean distance function
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Problem setup
model = pl.LpProblem("Robot_Tour_Problem", pl.LpMinimize)

# Variables
x = pl.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')
u = pl.LpVariable.dicts('u', list(cities.keys()), lowBound=0, cat='Continuous')

# Objective
model += pl.lpSum(distance(i, j) * x[i,j] for i in cities for j in cities if i != j)

# Constraints
for group in groups:
    model += pl.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    model += pl.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

for i in cities:
    model += pl.lpSum(x[j, i] for j in cities if i != j) == pl.lpSum(x[i, k] for k in cities if i != k)

# Subtour prevention constraints
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + k * x[i, j] <= k - 1

# Solve the model
model.solve()

# Output tour and its total cost
tour = [0]
current = 0
while True:
    next_city = [j for j in cities if j != current and pl.value(x[current, j]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current = next_city
    if next_city == 0:
        break

total_cost = pl.value(model.objective)

if tour[-1] != 0:
    tour.append(0)  # Make sure we return to the depot

print("Tour:", tour)
print("Total travel cost:", total_cost)