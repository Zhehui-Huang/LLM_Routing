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
cost = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Create the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if travel from i to j
x = pulp.LpVariable.dicts('x', cost.keys(), cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum([cost[i, j] * x[i, j] for i, j in cost]), "Total_Cost"

# Constraints
for k in cities:
    # Sum of flows out of city k must be exactly 1
    prob += pulp.lpSum([x[i, j] for i, j in cost if i == k]) == 1
    # Sum of flows into city k must be exactly 1
    prob += pulp.lpSum([x[i, j] for i, j in cost if j == k]) == 1

# Subtour elimination constraints
for k in range(2, n):
    subsets = itertools.combinations(range(1, n), k)
    for S in subsets:
        prob += pulp.lpSum([x[i, j] for i in S for j in S if (i, j) in x]) <= len(S) - 1

# Solve the problem
status = prob.solve()

# Check if the solution is optimal
if status != pulp.LpStatusOptimal:
    print("Failed to find optimal solution.")
else:
    tour = []
    for i in cities:
        for j in cities:
            if i != j and pulp.value(x[i, j]) == 1:
                tour.append((i, j))
    
    # Resolving the tour order
    ordered_tour = [0]
    current_city = 0
    while len(ordered_tour) < n:
        next_city = next(j for (i, j) in tour if i == current_city)
        ordered_tour.append(next_city)
        current_city = next_city
    ordered_tour.append(0)  # Return to the depot

    # Calculate total cost
    total_cost = sum(cost[ordered_tour[i], ordered_tour[i + 1]] for i in range(len(ordered_tour) - 1))
    print(f"Tour: {ordered_tour}\nTotal travel cost: {total_cost:.2f}")