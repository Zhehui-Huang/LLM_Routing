import math
import pulp

# Define the city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Initialize parameters
num_cities = len(coordinates)
num_robots = 8
depot = 0

# Function to calculate the Euclidean distance between cities
def euclidean_distance(index1, index2):
    return math.sqrt((coordinates[index1][0] - coordinates[index2][0]) ** 2 + (coordinates[index1][1] - coordinates[index2][1]) ** 2)

# Setup the problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables: x[i][j] is 1 if the route from i to j is taken
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(num_cities) for j in range(num_cities)], cat=pulp.LpBinary)

# Objective: minimize total distance traveled
problem += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in range(num_cities) for j in range(num_cities))

# Constraint: Enter and leave each city exactly once (except the depot)
for j in range(num_cities):
    if j != depot:
        problem += pulp.lpSum(x[i, j] for i in range(num_cities) if i != j) == 1
        problem += pulp.lpSum(x[j, i] for i in range(num_cities) if i != j) == 1

# Constraint: Number of robots leaving and returning to the depot
problem += pulp.lpSum(x[depot, j] for j in range(num_cities) if j != depot) == num_robots

# Solving the problem
problem.solve()

# Check the solution and display it
if pulp.LpStatus[problem.status] == 'Optimal':
    print("Optimal solution found:")
    total_travel_cost = 0

    for i in range(num_cities):
        for j in range(num_cities):
            if pulp.value(x[i, j]) == 1:
                cost = euclidean_distance(i, j)
                total_travel_cost += cost
                print(f"Route from {i} to {j} with cost {cost:.2f}")
                
    print(f"Overall Total Travel Cost: {total_travel_cost:.2f}")

else:
    print("No optimal solution found.")