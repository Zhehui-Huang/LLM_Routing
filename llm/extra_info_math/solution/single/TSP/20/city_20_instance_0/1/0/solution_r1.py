import pulp
import math
import itertools

# Coordinates for the cities
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Number of cities
n = len(cities)

# Compute Euclidean distance between two cities
def distance(city1, city2):
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if the path goes from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective: Minimize total travel distance
problem += pulp.lpSum(x[i, j] * distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints
# Leave each city only once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, 'leave_%s'%i

# Enter each city only once
for j in range(n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1, 'enter_%s'%j

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Output the solution if optimal
if pulp.LpStatus[status] == 'Optimal':
    tour = []
    tour_cost = pulp.value(problem.objective)
    # Create the tour path
    current_city = 0
    visited = [0] * n
    visited[0] = 1
    for _ in range(n-1):
        for j in range(n):
            if current_city != j and x[current_city, j].varValue == 1:
                tour.append(current_city)
                current_city = j
                break
    tour.append(current_city)
    tour.append(0)  # return to depot
    print("Tour:", tour)
    print("Total travel cost:", round(tour_cost, 2))
else:
    print("No optimal solution found.")