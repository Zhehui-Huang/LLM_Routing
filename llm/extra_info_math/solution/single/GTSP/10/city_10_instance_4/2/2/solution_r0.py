import pulp
import math

# Define the problem data
city_coordinates = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

city_groups = {
    0: [1, 4],
    1: [2, 6],
    2: [7],
    3: [5],
    4: [9],
    5: [8],
    6: [3]
}

# Function to calculate the Euclidean distance between cities
def euclidean_distance(i, j):
    return math.sqrt((city_coordinates[i][0] - city_attributes[j][0])**2 + (city_attributes[i][1] - city_attributes[j][1])**2)

# Generate the cost matrix
num_cities = len(city_coordinates)
cost_matrix = [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Set up the optimization problem
prob = pulp.LpProblem("RobotTourProblem", pulp.LpMinimize)

# Decision variables: x_ij where i, j belongs to different groups
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j),
                          cat='Binary')

# Objective Function
prob += pulp.lpSum(cost_matrix[i][j] * x[(i, j)] for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
# Each group has exactly one outgoing and one incoming link
for group, cities in city_groups.items():
    prob += pulp.lpSum(x[(i, j)] for i in cities for j in range(num_cities) if j not in cities) == 1
    prob += pulp.lpSum(x[(j, i)] for i in cities for j in range(num_cities) if j not in cities) == 1

# Flow conservation constraints
for i in range(num_cities):
    prob += pulp.lpSum(x[(j, i)] for j in range(num_cities) if j != i) == pulp.lpSum(x[(i, j)] for j in range(num_cities) if j != i)

# Solve the problem
prob.solve()

# Extract the tour
tour = [0]
visited = set(tour)
current = 0
while True:
    next_city = None
    for j in range(num_cities):
        if pulp.value(x[(current, j)]) == 1 and j not in visited:
            next_city = j
            break
    if next_city is None:
        break
    tour.append(next_city)
    visited.add(next_city)
    current = next_city

# Make sure to include the return to the start
tour.append(0)

# Calculate the total travel cost
total_cost = sum(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")