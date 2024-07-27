from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# City coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# List of groups, each containing city indices (excluding the depot city)
groups = [[5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]]

# Total number of cities including the depot
num_cities = len(coordinates)

# Function to calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Create the problem
prob = LpProblem("RobotTourProblem", LpMinimize)

# Decision variables: x[i][j] is 1 if the tour goes directly from city i to city j, otherwise 0
x = [[LpVariable(f"x_{i}_{j}", cat=LpBinary) for j in range(num_cities)] for i in range(num_cities)]

# Objective function: Minimize the total travel distance
prob += lpSum(x[i][j] * distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j), "Minimize_total_travel_distance"

# Constraints: Each group must have exactly one outgoing edge to a node outside the group
for group in groups:
    prob += lpSum(x[i][j] for i in group for j in range(num_cities) if j not in group) == 1, f"Outgoing_from_group_{group}"

# Each group must have exactly one incoming edge from a node outside the group
for group in groups:
    prob += lpSum(x[i][j] for j in group for i in range(num_cities) if i not in group) == 1, f"Incoming_to_group_{group}"

# Flow conservation for all cities (excluding depot)
for i in range(1, num_cities):
    prob += lpSum(x[i][j] for j in range(num_cities) if i != j) - lpSum(x[j][i] for j in range(num_cities) if i != j) == 0, f"Flow_conservation_{i}"

# Solve the problem
prob.solve()

# Output the results
tour = []
current_city = 0
visited = set([0])
for _ in range(num_cities):
    for j in range(num_cities):
        if x[current_city][j].value() == 1:
            tour.append(j)
            current_city = j
            visited.add(j)
            break

# Avoiding subtour by joining the tour path to the starting city
tour.append(0)

# Calculate the total cost of the tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)