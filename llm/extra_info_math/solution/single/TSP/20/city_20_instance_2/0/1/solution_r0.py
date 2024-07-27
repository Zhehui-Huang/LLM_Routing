import math
import pulp

# Define the coordinates of the depot and other cities
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 92), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Compute the Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Generate the cost matrix
n = len(coordinates)
cost_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Set up the PuLP problem
problem = pulp.LpProblem('TSP', pulp.LpMinimize)

# Decision variables: x[i][j] is 1 if the tour goes from city i to city j, 0 otherwise
x = [[p soluble problem
   problem += pulp.lpSum(cost_matrix[i][j] for j in range(n) ] * x[i][j]) for i in range(n)], "Objective"

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1, f"LeaveCity{i}"
    problem += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1, f"EnterCity{i}"

# Subtour elimination constraints
for S in range(2, n):
    subsets = itertools.combinations(range(1, n), s)  # 1 to n-1, excluding the depot
    for subset in subsets:
        problem += pulp.lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
status = problem.solve()

# Extract the tour from the variable values
tour = [0]
current = 0
while len(tour) < n:
    next_city = [j for j in range(n) if pulp.value(x[current][j]) == 1][0]
    tour.append(next_city)
    current = next_city
tour.append(0)  # Return to the depot

# Calculate the total cost of the tour
total_cost = sum(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)