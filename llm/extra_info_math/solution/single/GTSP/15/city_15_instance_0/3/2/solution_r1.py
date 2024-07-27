from math import sqrt
import pulp

# City coordinates
locations = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# City groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Function to calculate Euclidean distance between two points
def euclidean_distance(pt1, pt2):
    return sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Constructing the complete graph and distance matrix
num_cities = len(locations)
distances = [[euclidean more from one to another
distances = [[euclidean_distance(locations[i], locations[j]) for j in range(num_cities)] for i in range(num_cities)]

# Creating optimization problem
prob = pulp.LpProblem("MinimizeTravelCost", pulp.LpMinimize)

# Variables: x_ij = 1 if path from city i to j is chosen, otherwise 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), cat=pulp.LpBinary)

# Objective: Minimize the total travel distance
prob += pulp.lpSum(distances[i][j] * x[i,j] for i in range(num_cities) for j in range(num_cities) if i != j), "Minimize_Total_Travel_Distance"

# Subtour elimination auxiliary variables (for cities excluding the depot)
u = pulp.LpVariable.dicts("u", range(1, num_cities), lowBound=0, cat=pulp.LpContinuous)

# Constraints
# Each group must be entered and exited exactly once
for group in groups.values():
    prob += pulp.lpSum(x[i, j] for i in group for j in range(num_cities) if j not in group) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in range(num_cities) if j not in group) == 1

# Flow conservation except the depot
for i in range(1, num_cities):
    prob += (pulp.lpSum(x[i, j] for j in range(num_cities) if i != j) - pulp.lpSum(x[j] for j in range(num_cities) if i != j)) == 0

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            prob += u[i] - u[j] + (num_cities-1) * x[i, j] <= num_cities-2

# Solve the optimization problem
prob.solve()

# Results and output
if pulp.LpStatus[prob.status] == 'Optimal':
    tour = [0]
    current_city = 0
    while True:
        for j in range(num_cities):
            if j != current_city and pulp.value(x[current_city, j]) == 1:
                tour.append(j)
                current_city = j
                break
        if current_city == 0:  # back to depot
            break
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")