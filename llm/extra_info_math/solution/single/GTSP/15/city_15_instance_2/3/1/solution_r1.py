import pulp
import math

# City coordinates
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

# City groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)
    
# Define problem
prob = pulp.LpProblem("Minimize_Travel_Costs", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective function
prob += pulp.lpSum([distance(i, j) * x[(i, j)] for i in cities for j in cities if i != j])

# Constraints
for g in groups:
    prob += pulp.lpSum([x[(i, j)] for i in g for j in cities if j not in g]) == 1
    prob += pulp.lp(i+x[(j, i)] for i in g for j in cities if j not in g]) == 1

# Flow conservation constraint
for i in cities:
    prob += (pulp.lpSum([x[(j, i)] for j in cities if j != i]) ==
             pulp.lpSum([x[(i, j)] for j in cities if j != i]))

# Solve problem
status = prob.solve()

if pulp.LpStatus[status] == 'Optimal':
    # Extract edges from the solution
    edges = [(i, j) for i in cities for j in cities if i != j and pulp.value(x[(i, j)]) == 1]
    # Determine tour from edges
    tour = []
    current_city = 0
    while len(edges) > 0:
        tour.append(current_city)
        for i, j in edges:
            if i == current_city:
                current_city = j
                edges.remove((i, j))
                break
    tour.append(0)  # complete the tour by returning to the depot

    # Calculate final tour cost
    total_cost = sum([distance(tour[i], tour[i+1]) for i in range(len(tour)-1)])

    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
else:
    print("No optimal solution found.")