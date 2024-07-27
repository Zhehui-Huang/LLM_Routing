import pulp
import math

# Define city coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63),
    17: (63, 69), 18: (45, 35)
}

def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(coordinates)
distances = {(i, j): euclidean_dist(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Problem setup
prob = pulp.LpProblem("MTSP", pulp.LpMinimize)
x = pulp.LpVariable.dicts('x', (i, j, k for i in range(n) for j in range(n) for k in range(2) if i != j), cat='Binary')
u = pulp.LpVariable.dicts('u', (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective: Minimize the maximum tour length
maximum_length = pulp.LpVariable("maximum_length", lowBound=0)
prob += maximum_area

# Constraints
# 1. Visit each city exactly once
for j in range(1, n):
    prob += sum(x[i, j, k] for i in range(n) for k in range(2) if i != j) == 1

# 2. Departure and return to depot
for k in range(2):
    prob += sum(x[0, j, k] for j in range(1, n)) == 1
    prob += sum(x[j, 0, k] for j in range(1, n)) == 1

# 3. Total distance each robot travels
for k in range(2):
    prob += sum(distances[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= maximum_length

# 4. Subtour prevention
for k in range(2):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                prob += u[i] - u[j] + (n - 1) * x[i, j, k] <= n - 2

# 5. Ensure arrival and departure are balanced for each city and robot
for j in range(1, n):
    for k in range(2):
        prob += sum(x[i, j, k] for i in range(n) if i != j) == sum(x[j, i, k] for i in range(n) if i != j)

# Solve the problem
if prob.solve() == pulp.LpStatusOptimal:
    for k in range(2):
        route = [0]  # Depot
        current_city = 0
        while True:
            next_cities = [j for j in range(n) if pulp.value(x[current_city, j, k]) == 1]
            if not next_cities or current_city == 0:  # If no outgoing route or returned to depot
                break
            next_city = next_cities[0]
            route.append(next_city)
            current_city = next_city
        route.append(0)  # Return to depot
        cost = sum(distances[route[i], route[i+1]] for i in range(len(route)-1))
        print(f"Robot {k} Tour: {route}")
        print(f"Robot {k} Total Travel Cost: {cost}")
    print(f"Maximum Travel Cost: {pulp.value(maximum_length)}")
else:
    print("No optimal solution obtained.")