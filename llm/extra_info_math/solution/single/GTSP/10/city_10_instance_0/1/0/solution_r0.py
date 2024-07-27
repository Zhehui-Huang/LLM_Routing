import pulp
import math

# Define the city coordinates
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

# Define the groups
groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Calculate the Euclidean distance matrix
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[f"{i}_{j}"] = euclidean_distance(cities[i], cities[j])

# Setup the problem
prob = pulp.LpProblem("TSP_Variant_Min_Cost", pulp.LpMinimize)

# Define the decision variables
x = pulp.LpVariable.dicts("x", (cities.keys(), cities.keys()), cat='Binary', lowBound=0, upBound=1)

# Objective function
prob += pulp.lpSum([distances[f"{i}_{j}"] * x[i][j] for i in cities for j in cities if i != j]), "Minimize_Distance"

# Constraint for each group to have exactly one outgoing and one incoming edge
for group_id, group_cities in groups.items():
    prob += pulp.lpSum([x[i][j] for i in group_cities for j in cities if j not in group_cities]) == 1, f"Outgoing_from_group_{group_id}"
    prob += pulp.lpSum([x[i][j] for j in group_cities for i in cities if i not in group_cities]) == 1, f"Incoming_to_group_{group_id}"

# Flow conservation constraint
for i in cities:
    if i != 0: # Since city 0 is depot and has to start and end the tour
        prob += pulp.lpSum([x[i][j] for j in cities if j != i]) - pulp.lpSum([x[j][i] for j in cities if j != i]) == 0, f"Flow_conservation_{i}"

# Solve the problem
prob.solve()

# Check if the solution is optimal
if prob.status == 1:
    # Extract the tour and calculate total travel cost
    tour = []
    current_city = 0
    visited = {key: False for key in cities}
    total_cost = 0

    while True:
        tour.append(current_city)
        visited[current_city] = True
        next_cities = [j for j in cities if pulp.value(x[current_city][j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        total_cost += distances[f"{current_city}_{next_city}"]
        current_city = next_city
        if current_city == 0:
            break

    tour.append(0)  # Return to the depot
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found.")