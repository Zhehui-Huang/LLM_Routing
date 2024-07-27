import pulp
import math

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

groups = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

num_groups = len(groups)

# Calculating distances
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Distance matrix
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Problem
prob = pulp.LpProblem("VRP_Selective_Groups", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i,j) for i in cities for j in cities if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", list(range(1, 21)), lowBound=0, cat='Continuous')

# Objective
prob += pulp.lpSum([distances[(i,j)] * x[(i,j)] for i in cities for j in cities if i != j]), "Total Cost"

# Constraints
# Exactly one node from each group is visited
for g in groups.values():
    prob += pulp.lpSum([x[(i, j)] for i in g for j in cities if j not in g]) == 1  # Outgoing
    prob += pulp.lpSum([x[(j, i)] for i in g for j in cities if j not in g]) == 1  # Incoming

# Flow conservation constraint
for i in cities:
    prob += pulp.lpSum([x[(j, i)] for j in cities if j != i]) == pulp.lpSum([x[(i, j)] for j in cities if i != j]), f"Flow conservation at city {i}"

# Subtour elimination constraint
num_select = len(cities)  # Plus 1 from depot and -1 to account for 'k'
for i in range(2, 1 + num_groups):
    for j in range(2, 1 + num_groups):
        if i != j:
            for g1 in groups[i-2]:
                for g2 in groups[j-2]:
                    if g2 > g1:
                        prob += u[g1] - u[g2] + num_select * x[g1, g2] <= num_select - 1

# Solve
prob.solve()

# Output the tour and the total cost
tour = [0]
for i in range(len(cities)):
    current_city = tour[-1]
    next_city = [j for j in cities if j != current_city and pulp.value(x[(current_city, j)]) == 1][0]
    tour.append(next_city)
    if next_city == 0:
        break

total_cost = pulp.value(prob.object their)

print("Tour:", tour)
print("Total travel cost:", total_cost)