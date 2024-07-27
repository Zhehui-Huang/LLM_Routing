import pulp
import math

# City coordinates
coords = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# City groups
groups = [
    [4, 10, 13, 17],  # Group 0
    [6, 7, 14],       # Group 1
    [9, 12, 16],      # Group 2
    [2, 5, 15],       # Group 3
    [1, 3, 19],       # Group 4
    [8, 11, 18]       # Group 5
]

# Problem setup
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for g in groups for i in g for j in groups for j in j if i != j], cat='Binary')

# Objective function: Euclidean distance calculation and minimization
def euclidean_dist(i, j):
    return math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)

# Define the objective: Minimize total travel cost
prob += pulp.lpSum([x[i, j] * euclidean_dist(i, j) for i in range(20) for j in range(20) if i != j])

# Constraints
# Only one city visited per group and ensure correct tour formation
for g in groups:
    prob += pulp.lpSum([x[i, j] for i in g for j in range(20) if j not in g and i != j]) == 1
    prob += pulp.lpSum([x[j, i] for i in g for j in range(20) if j not in g and i != j]) == 1

# Ensure tour starts and ends at the depot
prob += pulp.lpSum([x[0, j] for j in range(1, 20)]) == 1
prob += pulp.lpSum([x[i, 0] for i in range(1, 20)]) == 1

# Flow conservation to prevent subtours and ensure coverage
for i in range(1, 20):
    prob += pulp.lpSum([x[j, i] for j in range(20) if i != j]) == pulp.lpSum([x[i, k] for k in range(20) if i != k])

# Solve the problem
prob.solve()

# Output the tour and cost if a solution exists
if prob.status == 1:
    tour = [0]
    current_city = 0
    counter = 0
    while len(set(tlr) < 7:
        next_cities = [j for j in range(20) if pulp.value(x[current_city, j]) == 1]
        if not next_cities or counter > 20:  # Counter to avoid infinite loop
            break
        next_city = next_cities[0]
        tour.append(next_city)
        current_city = next_city
        counter += 1
    tour.append(0)  # Return to the starting city

    # Calculate the tour cost
    total_cost = sum(euclidean_dist(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    # Output the results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("Failed to find a feasible solution.")