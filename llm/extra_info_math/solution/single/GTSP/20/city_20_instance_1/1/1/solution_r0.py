import pulp
import math

# City positions as (x, y)
positions = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

# Groups of cities
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# All cities, including the depot
cities = list(range(len(positions)))

# Create the LP problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables x_ij
x = pulp.LpVariable.dicts("x", 
                          ((i, j) for i in cities for j in cities if i != j),
                          cat='Binary')

# Objective: Minimize total distance
problem += pulp.lpSum([euclidean_distance(positions[i], positions[j]) * x[i, j] for i in cities for j in cities if i != j]), "Minimize_Total_Distance"

# Constraint: Exactly one link out from depot, excluding same cluster visits
problem += pulp.lpSum([x[0, j] for j in cities if j != 0]) == 1, "Out_From_Depot"

# Constraint: Exactly one link into depot
problem += pulp.lpSum([x[j, 0] for j in cities if j != 0]) == 1, "Into_Depot"

# Constraint: Cluster exit and entry
for group in groups:
    problem += pulp.lpSum([x[i, j] for i in group for j in cities if j not in group]) == 1, "Out_" + str(group)
    problem += pulp.lpSum([x[j, i] for i in group for j in cities if j not in group]) == 1, "In_" + str(group)

# Solving the problem
problem.solve()

# Check if a feasible solution exists
if pulp.LpStatus[problem.status] == 'Optimal':
    # Solution path and cost
    path = []
    current_position = 0
    path.append(current_position)

    # Reconstruct the path
    while True:
        next_cities = [j for j in cities if x[current_position, j].varValue == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        path.append(next_city)
        current_position = next_city
        if current_position == 0:
            break

    total_cost = pulp.value(problem.objective)
    result = {
        "Tour": path,
        "Total travel cost": total_cost
    }
    print("Tour:", result["Tour"])
    print("Total travel cost:", result["Total travel..............l_cost"])
else:
    print("No optimal solution found.")