import pulp
import math

# City coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# City groups
groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Helper function to calculate Euclidean distance
def distance(i, j):
    return math.sqrt((cities[j][0] - cities[i][0]) ** 2 + (cities[j][1] - cities[i][1]) ** 2)

# Define the problem
prob = pulp.LpProblem("ShortestTour", pulp.LpMinimize)

# Decision variable: x_ij is 1 if travels from city i to city j, otherwise 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective Function: Minimize the total distance traveled
prob += pulp.lpSum(x[(i, j)] * distance(i, j) for i in cities for j in cities if i != j), "TotalTravelCost"

# Constraint: Enter and exit each group exactly once
for group in groups.values():
    prob += pulp.lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1, f"OneExitFromGroup_{group}"
    prob += pulp.lpSum(x[(j, i)] for i in group for j in cities if j not in group) == 1, f"OneEntryToGroup_{group}"

# Flow conservation: Enter and exit each city exactly once
for k in cities:
    prob += pulp.lpSum(x[(i, k)] for i in cities if i != k) == pulp.lpSum(x[(k, j)] for j in cities if j != k), f"FlowConservation_{k}"

# Solve the Problem
prob.solve()

# Check if a valid solution exists
if pulp.LpStatus[prob.status] == 'Optimal':
    tour = []
    current_city = 0
    tour.append(current_city)
    visited = set([0])

    while True:
        for j in cities:
            if j not in visited and x[(current_city, j)].varValue == 1:
                tour.append(j)
                visited.add(j)
                current_city = j
                break
        if current city == 0:
            break
            
    total_cost = pulp.value(prob.objective)
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found.")