import pulp
import math

# Coordinates of the cities including the depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}
n = len(cities)
m = 2  # Number of robots

# Helper function to calculate Euclidean distance
def euclidean_distance(ci, cj):
    return math.sqrt((cities[ci][0] - cities[cj][0])**2 + (cities[ci][1] - cities[cj][1])**2)

# Problem setup
prob = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Variables:
# x[i][j][k] = 1 if robot k travels from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)), 0, 1, pulp.LpBinary)
# u[i] is the sequence position of city i in the tour to prevent subtours (only for cities, not depot)
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), 1, n-1, pulp.LpInteger)

# Objective function : Minimize the total travel distance
prob += pulp.lpSum(x[i, j, k] * euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j for k in range(m))

# Constraints
# Each non-depot city is visited exactly once overall
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1

# Each robot leaves from and returns to the depot exactly once
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Each city (except depot) has exactly one outgoing connection and one incoming connection per robot
for k in range(m):
    for j in range(1, n):
        prob += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n - 1) * x[i, j, k] <= n - 2

# Solve the problem
prob.solve()

# Output the routes and the cost
total_cost = 0
for k in range(m):
    print(f"\nRobot {k} Tour:")
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[i, j, k]) == 1:
                print(f"{i} -> {j}", end=' ')
    tour_cost = sum(euclidean_distance(i, j) * pulp.value(x[i, j, k]) for i in range(n) for j in range(n) if i != j)
    total_cost += tour_cost
    print(f"\nRobot {k} Total Travel Cost: {tour_cost}")

print(f"\nOverall Total Travel Cost: {total_cost}")