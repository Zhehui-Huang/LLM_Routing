import pulp
import math

# Define the coordinates of each city
cities = {
    0: (79, 15),  # Depot
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

# City groups where each list contains the cities in the group
city_groups = {
    0: [1, 4],
    1: [2, 6],
    2: [7],
    3: [5],
    4: [9],
    5: [8],
    6: [3]
}

# Compute Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Create a distance matrix
distances = {}
for u in cities:
    for v in cities:
        if u != v:
            distances[(u, v)] = distance(cities[u], cities[v])

# Create the optimization problem
problem = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective Function
problem += pulp.lpSum([distances[i, j] * x[i, j] for i in cities for j in cities if i != j])

# Constraints for ensuring one exit and one entry per group (Constraints 2 & 3)
for group in city_groups.values():
    problem += pulp.lpSum([x[i, j] for i in group for j in cities if j not in group]) == 1
    problem += pulp.lpSum([x[j, i] for i in group for j in cities if j not in group]) == 1

# In-flow and out-flow conservation (Constraint 4)
for k in cities:
    problem += pulp.lpSum([x[i, k] for i in cities if i != k]) == pulp.lpSum([x[k, j] for j in cities if k != j])

# Solve the problem
problem.solve()

# If the problem is solved, print the tour and total travel cost
if pulp.LpStatus[problem.status] == 'Optimal':
    tour = [0]
    current_location = 0
    while len(tour) < 8:  # Since we need 1 city from each group plus the depot
        next_location = [j for j in cities if j not in tour and x[current_location, j].varValue == 1]
        if next_location:
            next_location = next_location[0]
            tour.append(next_location)
            current_location = next_location
        else:
            break
    tour.append(0)  # Return to depot

    cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {cost:.2f}")
else:
    print("No optimal solution found.")