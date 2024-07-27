import pulp
import math

# Coordinates of the cities including the depot city as the first entry
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25), 
    (75, 9), (52, 54), (64, 72), (14, 89)
]

n = len(coordinates)  # Total number of cities including the depot

# Function to calculate Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost matrix (distance matrix)
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Solving using pulp
model = pulp.LpProblem("TSP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')

# Objective function
model += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n)), "Total Travel Cost"

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"One out edge from {i}"
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"One in edge to {i}"

# Subtour prevention via Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Solve the problem
model.solve()

# Output solution
if pulp.LpStatus[model.status] == 'Optimal':
    tour = []
    cur_city = 0
    while True:
        tour.append(cur_city)
        next_cities = [j for j in range(n) if pulp.value(x[cur_city, j]) == 1]
        if next_cities:
            cur_city = next_cities[0]
        if cur_city == 0:
            break
    tour.append(0)  # Append depot city at end to close the loop
    total_cost = pulp.value(model.objective)

    result = {
        "Tour": tour,
        "Total travel cost": total_cost
    }
    print(result)
else:
    print("No optimal solution found")