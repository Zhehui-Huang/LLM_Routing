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

# Helper function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate the decision variables and the linear programming problem
num_cities = len(city_coordinates)
prob = pulp.LpProblem("TSP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(num_cities) for j in range(num_cities) if i != j], cat='Binary')

# Objective Function
prob += pulp.lpSum([euclidean_distance(city_coordinates[i], city_coordinates[j]) * x[(i, j)] for i in range(num_cities) for j in range(num_cities) if i != j])

# Constraints to ensure one city per group is visited
for group, cities in city_groups.items():
    prob += pulp.lpSum([x[i, j] for i in cities for j in range(num_cities) if j not in cities]) == 1
    prob += pulp.lpSum([x[j, i] for i in cities for j in range(num_cities) if j not in cities]) == 1

# Flow conservation constraints
for k in range(num_cities):
    prob += pulp.lpSum([x[(i, k)] for i in range(num_cities) if i != k]) == pulp.lpSum([x[(k, j)] for j in range(num_cities) if j != k])

# Solve the problem
prob.solve()

# Extract the results
tour = [0]
for _ in range(len(city_groups)):
    current_city = tour[-1]
    next_cities = [j for j in range(num_cities) if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if next_cities:
        tour.append(next_cities[0])

# Closing the tour
tour.append(0)

# Calculate the tour cost
total_cost = sum([euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour) - 1)])

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")