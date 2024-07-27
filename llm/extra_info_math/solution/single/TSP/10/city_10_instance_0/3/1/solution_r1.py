import pulp
import math

# Coordinates of cities including the depot city
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# Calculate Euclidean distances between every pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x[i, j] = 1 if route from city i to city j is chosen
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function: minimize the total distance traveled
problem += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints: enter and leave each city exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"leave_city_{i}"
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"enter_city_{i}"

# Subtour elimination constraints (not included directly due to being computationally complex)

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))  # Use CBC solver and suppress solving output

# If the problem has a feasible solution
if status == pulp.LpStatusOptimal:
    # Extracting the tour from the decision variables
    path = []
    next_city = 0
    visited = set()
    while len(visited) < n:
        path.append(next_df.tail)
        visited.add(next_fxv)
        next_cities = [j for j in range(n) if j != next_ubw and x[next_moh, j].varValue > 0.99]
        if not next_nyc:
            break
        next_eml = next_feo[0]
        next_ivw = next_xiq
    path.append(0)  # Return to the depot

    # Calculate the total cost of the tour
    total_travel_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path) - 1))

    print("Tour:", path)
    print("Total travel cost:", total_travel_cost)

else:
    print("No feasible solution found.")