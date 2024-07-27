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
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Problem setup
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(20) for j in range(20) if i != j], cat='Binary')

# Objective function
def euclidean_dist(i, j):
    return math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)

prob += pulp.lpSum([x[i, j] * euclidean_dist(i, j) for i in range(20) for j in range(20) if i != j]), "Total Cost"

# Adding constraints
for group in groups:
    prob += pulp.lpSum([x[j, i] for i in group for j in range(20) if j not in group]) == 1
    prob += pulp.lpSum([x[i, j] for i in group for j in range(20) if j not in group]) == 1

# Ensure the tour starts and ends at the depot
prob += pulp.lpSum([x[0, j] for j in range(20) if j != 0]) == 1
prob += pulp.lpSum([x[i, 0] for i in range(20) if i != 0]) == 1

# Solve the problem
prob.solve()

# Extract the solution
tour = [0]
current_city = 0
solution_found = True
while len(tour) < 7:
    next_cities = [j for j in range(20) if pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        solution_found = False
        break
    next_city = next_cities[0]
    if next_city == 0:
        break
    tour.append(next_city)
    current_city = next_city

# Append the start city to complete the tour
tour.append(0)

# Calculate the total travel cost
total_cost = sum(euclidean_dist(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output the results
if solution_found:
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No solution was found. Please check constraints and problem formulation.")