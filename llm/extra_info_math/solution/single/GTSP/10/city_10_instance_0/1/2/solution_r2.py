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
    return math.sqrt((cities[j][0] - cities[i][0])**2 + (cities[j][1] - cities[i][1])**2)

# Define the problem
prob = pulp.LpProblem("ShortestTour", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective Function
prob += pulp.lpSum(x[(i, j)] * distance(i, j) for i in cities for j in cities if i != j), "TotalTravelCost"

# Constraints
# Each group should have exactly one exit and one entry
for group_id, group in groups.items():
    prob += pulp.lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1, f"exit_group_{group_id}"
    prob += pulp.lpSum(x[(j, i)] for i in group for j in cities if j not in group) == 1, f"enter_group_{group_id}"

# Flow conservation for each city
for k in cities:
    prob += pulp.lpSum(x[(i, k)] for i in cities if i != k) == pulp.lpSum(x[(k, j)] for j in cities if j != k), f"flow_{k}"

# Solve the problem
prob.solve()

# Extract the solution
if pulp.LpStatus[prob.status] == 'Optimal':
    tour = [0]
    current_city = 0

    while True:
        next_cities = [j for j in cities if j != current_city and pulp.value(x[(current_city, j)]) == 1]
        if not next_cutter_city or next_city[0] == 0:
            tour.append(0)
            break
        next_city = next_cheater_city[0]
        tour.append(next_city)
        current_city = y
    total_cost = pulp.value(prob.objective)
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found.")