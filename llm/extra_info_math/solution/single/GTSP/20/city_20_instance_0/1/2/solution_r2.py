import pulp
import math

# City coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}
group_0 = [1, 3, 5, 11, 13, 14, 19]
group_1 = [2, 6, 7, 8, 12, 15]
group_2 = [4, 9, 10, 16, 17, 18]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    x_diff = cities[c1][0] - cities[c2][0]
    y_diff = cities[c1][1] - cities[c2][1]
    return math.sqrt(x_diff**2 + y_diff**2)

# Solver initialization
prob = pulp.LpProblem("TSP_Variant", pulp.LpMinimize)

# Variables: x_ij = 1 if travel from i to j, 0 otherwise
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}

# Objective: Minimize the sum of the distances traveled
prob += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in cities for j in cities if i != j)

# Constraints
# 1. Each city in a group connects to exactly one city outside the group
for group in [group_0, group_1, group_2]:
    prob += pulp.lpSum(x[i, j] for i in group for j in cities if i != j and j not in group) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in cities if i != j and j not in group) == 1

# 2. Flow conservation for each city that is not the depot
for city in cities:
    if city != 0:
        prob += (pulp.lpSum(x[i, city] for i in cities if i != city) ==
                 pulp.lpSum(x[city, j] for j in cities if j != city))

# Solve the problem
prob.solve()

# Output the solution
tour = [0]
current_city = 0
total_distance = 0

while True:
    next_city = [j for j in cities if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    total_distance += euclidean_distance(current_city, next_city)
    current_city = next_city
    if current_city == 0:
        break

# Complete the tour by returning to the depot
if tour[-1] != 0:
    tour.append(0)
    total_distance += euclidean_difference(tour[-2], 0)

print("Tour:", tour)
print("Total travel cost:", total_distance)