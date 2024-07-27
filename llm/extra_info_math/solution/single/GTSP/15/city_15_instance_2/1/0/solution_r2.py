import pulp as pl
import math

# Coordinates of the cities
city_coords = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
               (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
               (56, 58), (72, 43), (6, 99)]

# Cities grouped
groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

# Function to calculate Euclidean distance
def euclidean_dist(i, j):
    return math.sqrt((city_coords[i][0] - city_coords[j][0])**2 + (city_coords[i][1] - city_coords[j][1])**2)

# Initialize LP problem
prob = pl.LpProblem("TSP_Variant", pl.LpMinimize)

# Decision variables
paths = [(i, j) for i in range(15) for j in range(15) if i != j]
x = pl.LpVariable.dicts("x", paths, cat='Binary')

# Objective function
prob += pl.lpSum([euclidean_dist(i, j) * x[(i, j)] for (i, j) in paths]), "Total_Cost"

# Constraints to ensure exactly one entry and exit from each group
for group in groups.values():
    prob += sum(x[(i, j)] for i in group for j in set(range(15)) - set(group)) == 1, f"Exit_group_{group}"
    prob += sum(x[(j, i)] for i in group for j in set(range(15)) - set(group)) == 1, f"Enter_group_{group}"

# Each city should have exactly one arrival and one departure
for i in range(15):
    prob += sum(x[(j, i)] for j in range(15) if j != i) == sum(x[(i, k)] for k in range(15) if k != i), f"Flow_conservation_{i}"

# Solve problem
prob.solve()

# Check if a valid solution is found
if pl.LpStatus[prob.status] == "Optimal":
    print("Solution is optimal")

# Extract the tour from the solution
tour = []
visited = [0]
while len(visited) - 1 < len(groups):
    for j in range(15):
        if x[(visited[-1], j)].varValue == 1:
            tour.append((visited[-1], j))
            visited.append(j)
            break

# Return to the depot in the tour
tour.append((visited[-1], 0))

# Calculate the tour cost
tour_cost = sum(euclidean_dist(i, j) for i, j in tour)

# Output the results
city_tour = [i for i, j in tour] + [0]  # end at the starting point
print("Tour:", city_tour)
print("Total travel cost:", tour_cost)