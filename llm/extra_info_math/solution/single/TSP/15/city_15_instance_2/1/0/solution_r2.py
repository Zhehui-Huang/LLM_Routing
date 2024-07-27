import pulp
import math

# Define the cities' coordinates, including the depot (index 0)
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84),
    3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78),
    9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute the cost matrix
n = len(cities)
cost = {(i, j): euclidean_distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Create the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if travel from i to j
x = pulp.LpVariable.dicts('x', [(i, j) for i in range(n) for j in range(n) if i != j], cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum([cost[i, j] * x[i, j] for i, j in cost]), "Total_Cost"

# Constraints
for k in range(n):
    prob += pulp.lpSum([x[i, j] for i in range(n) if i != j for j in range(n) if j != i and i == k]) == 1  # Sum of flows out of city k
    prob += pulp.lpSum([x[i, j] for i in range(n) if i != j for j in range(n) if j != i and j == k]) == 1  # Sum of flows into city k

# Prevent subtours
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += x[i, j] + x[j, i] <= 1

# Solve the problem
prob.solve()

# Extract the tour from the decision variables
tour = [0]
current_city = 0
while len(tour) < n:
    next_city = [j for i in range(n) if i != j for j in range(n) if j != i and pulp.value(x[current_city, j]) == 1][0]
    tour.append(next_city)
    current_city = next_city
tour.append(0)  # Return to the depot

# Calculate total cost
total_cost = sum(cost[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")