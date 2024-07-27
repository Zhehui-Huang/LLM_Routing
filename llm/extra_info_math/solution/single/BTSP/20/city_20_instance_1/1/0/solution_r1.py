import pulp
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

n = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem variable:
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables:
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective:
z = pulp.LpVariable("z", lowBound=0)
prob += z

# Constraints:
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave i
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter i

for i in range(n):
    for j in range(n):
        if i != j:
            prob += distance_matrix[i][j] * x[i, j] <= z

# Subtour elimination constraints (using Miller-Tucker-Zemlin formulation):
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n*x[i, j] <= n-1

# Solve the problem
prob.solve()

# Extract the solution:
tour = []
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Order tour starting from 0
ordered_tour = []
current_location = 0
while len(ordered_tour) < n:
    for arc in tour:
        if arc[0] == current_location:
            ordered_tour.append(arc[0])
            current_location = arc[1]
            tour.remove(arc)
            break
ordered_tour.append(0)  # Completing the tour to return to the start

# Compute total and maximum travel costs:
total_cost = sum(distance_matrix[ordered_tour[i]][ordered_tour[i+1]] for i in range(n))
max_distance = max(distance_matrix[ordered_tour[i]][ordered_tour[i+1]] for i in range(n))

print("Tour: {}".format(ordered_tour))
print("Total travel cost: {:.2f}".format(total_cost))
print("Maximum distance between consecutive cities: {:.2f}".format(max_distance))