import pulp
from math import sqrt

# Define coordinates for the depot and the cities
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# City groups
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize the Linear Programming problem
problem = pulp.LpProblem("VRP_Groups", pulp.LpMinimize)

# Decision variables: x[i][j] is 1 if the path from i to j is chosen, 0 otherwise
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(15) for j in range(15) if i != j], cat='Binary')

# Objective function: Minimize the total distance traveled
problem += pulp.lpSum(distance(i, j) * x[i, j] for i in range(15) for j in range(15) if i != j)

# Constraints
# Ensuring one visit from each group
for group in groups:
    # Exactly one outgoing connection from group cities to different group city or depot
    problem += pulp.lpSum(x[i, j] for i in group for j in range(15) if j not in group) == 1
    # Exactly one incoming connection to group cities from different group city or depot
    problem += pulp.lpSum(x[j, i] for i in group for j in range(15) if j not in group) == 1

# Flow conservation at nodes (ensure exactly one entry and one exit for each city not in depot)
for j in range(1, 15):
    problem += pulp.lpSum(x[i][j] for i in range(15) if i != j) == pulp.lpSum(x[j][i] for i in range(15) if i != j)

# Solve the MILP problem
problem.solve()

# Extract the solution
if pulp.LpStatus[problem.status] == 'Optimal':
    tour = []
    current_city = 0
    tour.append(current_city)
    total_travel_cost = 0

    # Construct the tour from decision variables
    for _ in range(7):  # we have 7 groups and each group will contribute one city to the tour
        next_cities = [j for j in range(15) if j != current_city and pulp.value(x[current_city, j]) == 1]
        if next_cities:
            next_city = next_cities[0]
            tour.append(next_city)
            total_travel_cost += distance(current_city, next_city)
            current_city = next_city

    # Return to the depot
    tour.append(0)
    total_travel_cost += distance(current_city, 0)

    print("Tour:", tour)
    print("Total travel cost:", round(total_travel_cost, 2))
else:
    print("No optimal solution found. The problem status is", pulp.LpStatus[problem.status])