import pulp
import math

# City and group definitions
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create problem instance
problem = pulp.LpProblem("TSP_VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective function
problem += pulp.lpSum(x[i, j] * euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j)

# Constraints
# Exactly one city from each group + depot forms a tour, visit exactly one city from each group
for g in groups:
    # each group must have one outgoing edge to any city not in the group
    problem += pulp.lpSum(x[i, j] for i in g for j in set(cities) - set(g)) == 1
    # each group must have one incoming edge from any city not in the group
    problem += pulp.lpSum(x[j, i] for i in g for j in set(cities) - set(g)) == 1

# Flow conservation
for i in cities:
    problem += pulp.lpSum(x[j, i] for j in cities if j != i) == pulp.lpSum(x[i, j] for j in cities if i != j)

# Solve the problem
status = problem.solve()

# Extract the solution
if status == pulp.LpStatusOptimal:
    print(f"Status: {pulp.LpStatus[status]}")
    result_solution = []
    current_city = 0
    tour_cost = 0
    visited = set([current_city])
    result_solution.append(current_city)

    while len(result_solution) < len(groups) + 2:
        found = False
        for next_city in cities:
            if next_city != current_city and x[current_city, next_city].value() == 1:
                tour_cost += euclidean_distance(cities[current_city], cities[next_city])
                current_city = next_city
                visited.add(current_city)
                result_solution.append(current_city)
                found = True
                break
        if not found:
            break

    result_solution.append(0)  # return to the depot
    tour_cost += euclidean_distance(cities[current_city], cities[0])

    print(f"Tour: {result_solution}")
    print(f"Total travel cost: {tour_cost}")
else:
    print("No solution found.")