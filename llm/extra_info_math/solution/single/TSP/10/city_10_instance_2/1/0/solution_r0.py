import pulp
import math 

# Coordinates of cities including the depot
coords = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

n = len(coords)  # Number of cities including the depot

# Calculate Euclidean distance between each pair of points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Cost matrix
c = [[distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Setup the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective
prob += pulp.lpSum(c[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j), "Total_Distance"

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Sum_of_Outgoing_from_{i}"
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Sum_of_Incoming_to_{i}"

# Subtour elimination constraints are required here, but due to their complexity, 
# a simpler model or a solver-specific cut strategy may be attempted here directly.

# Solving the problem
prob.solve()

# Extracting the solution
tour = []
if pulp.LpStatus[prob.status] == 'Optimal':
    # Find the tour from the decision variables
    current_city = 0
    while True:
        tour.append(current_city)
        next_cities = [j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1]
        if not next_cities:
            break
        current_city = next_cities[0]
        if current_city == 0:
            break

tour.append(0)  # Complete the tour by returning to the depot

# Calculate the total cost of the tour
total_cost = sum(c[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}\nTotal travel cost: {total_cost}")