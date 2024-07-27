import pulp
import math

# Helper function to compute Euclidean Distance
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Grouping cities
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Create the optimization problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij travel between city i and city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(x[(i, j)] * calc_distance(cities[i], cities[j]) for i in cities for j in cities if i != j)

# Constraints for exact one visit per group and connectivity
for group_id, group in groups.items():
    prob += pulp.lpSum(x[(i, j)] for i in group for j in set(cities.keys()) - set(group)) == 1
    prob += pulp.lpSum(x[(j, i)] for i in group for j in set(cities.keys()) - set(group)) == 1

# Flow conservation constraint
for k in cities:
    prob += (pulp.lpSum([x[(i, k)] for i in cities if i != k]) ==
             pulp.lpSum([x[(k, j)] for j in cities if k != j]))

# Solve the problem
prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Verify if we found an optimal solution
if pulp.LpStatus[prob.status] == 'Optimal':
    # Extract the path from the decision variables
    tour = [0]
    current = 0
    while True:
        next_city = None
        for j in cities:
            if j != current and pulp.value(x[(current, j)]) == 1:
                next_city = j
                tour.append(next_city)
                current = next_city
                break
        if next_city == 0:
            break

    # Calculate the total cost
    total_cost = sum(calc_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("Failed to find an optimal solution.")