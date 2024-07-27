import pulp
import math

# City coordinates and city groups
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
          (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
          (53, 80), (21, 21), (12, 39)]
groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

n = len(cities)
all_nodes = set(range(n))
model = pulp.LpProblem("TSP_Group_Selected_Cities", pulp.LpMinimize)

# Decision variables x(i, j): whether robot travels from city i to city j
x = pulp.LpVariable.dicts("x", [(i, j) for i in all_nodes for j in all_nodes if i != j], 
                          lowBound=0, upBound=1, cat=pulp.LpBinary)

# Objective function: Minimize the total travel cost
model += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in all_nodes for j in all_nodes if i != j)

# Constraint: Connect between group cities and other non-group cities
for group in groups:
    model += pulp.lpSum(x[i, j] for i in group for j in all_nodes - set(group)) == 1  # Outgoing connection
    model += pulp.lpSum(x[j, i] for i in group for j in all_nodes - set(group)) == 1  # Incoming connection

# Constraint: Flow conservation for each node (city)
for k in all_nodes:
    model += pulp.lpSum(x[i, k] for i in all_nodes if i != k) == pulp.lpSum(x[k, j] for j in all_nodes if k != j)

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract tour
tour = [0]  # start from the depot
current_city = 0
while len(tour) <= len(groups):
    next_city = [j for j in all_nodes if j != current_city and pulp.value(x[current_city, j]) == 1][0]
    tour.append(next_city)
    current_city = next_city
tour.append(0)  # return to the depot

# Calculate total travel cost
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)