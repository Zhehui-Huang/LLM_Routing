import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Coordinates of the cities indexed by city number
coordinates = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
               (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# City groups
city_groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

# Function to calculate Euclidean distance
def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Number of city groups
k = len(city_groups)

# Total number of cities including the depot
n_cities = len(coordinates)

# Generate cost matrix
cost_matrix = { (i, j): euclidean_dist(coordinates[i], coordinates[j]) for i in range(n_cities) for j in range(n_cities) if i != j }

# Create the optimization model
model = LpProblem("Robot_Travel_Planning", LpMinimize)

# Setup variables
x = {(i, j): LpVariable(cat=LpBinary, name=f"x_{i}_{j}") for i in range(n_cities) for j in range(n_cities) if i != j}
u = {p: LpVariable(name=f"u_{p}", lowBound=0) for p in range(2, k+1)}

# Objective function: Minimize total cost of travel
model += lpSum(cost_matrix[i, j] * x[i, j] for i in range(n_cities) for j in range(n_cities) if i != j), "Total_Travel_Cost"

# Constraints

# Each group p must connect exactly one edge to nodes outside group p
for p, group in enumerate(city_groups, 1):
    model += lpSum(x[i, j] for i in group for j in range(n_cities) if j not in group) == 1, f"One_outgoing_from_group_{p}"
    model += lpSum(x[j, i] for i in group for j in range(n_cities) if j not in group) == 1, f"One_incoming_to_group_{p}"

# Flow conservation constraints
for i in range(n_cities):
    model += (lpSum(x[j, i] for j in range(n_cities) if j != i) == lpSum(x[i, j] for j in range(n_cities) if j != i)), f"Flow_conservation_at_node_{i}"

# Sub-tour elimination constraints
for p in range(2, k+1):
    for q in range(2, k+1):
        if p != q:
            model += (u[p] - u[q] + k * lpSum( x[i, j] for i in city_groups[p-1] for j in city-theta
                groups[q-1] ) + (k-2) * lpSum(x[j, i] for i in city_groups[p-1] for j in city_groups[q-1]) <= k - 1), f"Subtour_elimination_{p}_{q}"

# Solve the model
model.solve()

# Extract the solution
tour_solution = []
current_city = 0
visited = set()
visited.add(current_city)

for _ in range(n_cities):
    for next_city in range(n_cities):
        if next_city != current_city and x[current_city, next_city].varValue == 1:
            tour_solution.append(next_city)
            visited.add(next_city)
            current_city = next_city
            break

# Append the depot city
tour_solution.insert(0, 0)
tour_solution.append(0)

# Calculate the total travel cost of the tour
total_cost = sum(cost_matrix[tour_solution[i], tour_solution[i+1]] for i in range(len(tour_solution) - 1))

# Output the result
print(f"Tour: {tour_solution}")
print(f"Total travel cost: {total_cost}")