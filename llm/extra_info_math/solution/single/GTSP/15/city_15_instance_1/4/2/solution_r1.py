import pulp
import math

# Coordinates of the cities
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Groups of cities
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Set problem and define decision variables
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(15) for j in range(15) if i != j], cat="Binary")

# Add the objective function
prob += pulp.lpSum([x[i, j] * distance(i, j) for i in range(15) for j in range(15) if i != j]), "Objective: Minimize Total Distance"

# Add constraints
# Each group should send out and receive exactly one link
for grp in groups:
    prob += pulp.lpSum([x[i, j] for i in grp for j in range(15) if j not in grp]) == 1, f"Outgoing_from_group_{groups.index(grp)}"
    prob += pulp.lpSum([x[i, j] for j in range(15) if j in grp for i in range(15) if i not in grp]) == 1, f"Incoming_to_group_{groups.index(grp)}"

# Each city(except the depot) should have exactly one incoming and one outgoing connection.
for k in range(1, 15):
    prob += pulp.lpSum([x[j, k] for j in range(15) if j != k]) == pulp.lpSum([x[k, i] for i in range(15) if i != k]), f"Flow_conserve_node_{k}"

# Add connectivity from/to the depot
prob += pulp.lpSum([x[0, j] for j in range(1, 15)]) == 1, "Depot_outgoing"
prob += pulp.lpSum([x[i, 0] for i in range(1, 15)]) == 1, "Depot_incoming"

# Solve the problem
prob.solve()

# Extracting the solution
if pulp.LpStatus[prob.status] == "Optimal":
    tour = [0]  # Start at the depot
    while len(tour) < len(groups) + 1:
        current_city = tour[-1]
        next_city = [j for j in range(15) if pulp.value(x[current_city, j]) == 1]
        if next_city:
            tour.append(next_city[0])

    # Append the return to the depot
    tour.append(0)
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

    # Output the results
    print("Tour:", tour)
    print("Total travel cost:", total_cost)