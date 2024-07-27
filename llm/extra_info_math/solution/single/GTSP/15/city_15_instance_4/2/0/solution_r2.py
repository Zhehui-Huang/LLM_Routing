import pulp
import math

# Define city positions
positions = [
    (35, 40), # City 0 (Depot)
    (39, 41), # City 1
    (81, 30), # City 2
    (5, 50),  # City 3
    (72, 90), # City 4
    (54, 46), # City 5
    (8, 70),  # City 6
    (97, 62), # City 7
    (14, 41), # City 8
    (70, 44), # City 9
    (27, 47), # City 10
    (41, 74), # City 11
    (53, 80), # City 12
    (21, 21), # City 13
    (12, 39)  # City 14
]

# Define groups of cities
groups = [
    [3, 8],  # Group 0
    [4, 13], # Group 1
    [1, 2],  # Group 2
    [6, 14], # Group 3
    [5, 9],  # Group 4
    [7, 12], # Group 5
    [10, 11] # Group 6
]

# Calculate Euclidean distances between all pairs of cities
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

distances = {(i, j): euclidean_distance(positions[i], positions[j]) for i in range(len(positions)) for j in range(len(positions)) if i != j}

# Set up the pulp LP problem
problem = pulp.LpProblem("TSP_Group_Selection", pulp.LpMinimize)

# Decision variables
x = pulp.Lpx.var(matrix='(i, j) for i in range(len(positions)) for j in range(len(positions)) if i != j', cat='Binary')

# Objective - Minimize the sum of distances for chosen edges
problem += pulp.lpSum(distances[i, j] * x[i, j] for i in range(len(positions)) for j in range(len(positions)) if i != j)

# Each node must be entered and exited precisely once
for j in range(1, len(positions)):
    problem += pulp.lpSum(x[i, j] for i in range(len(positions)) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for i in range(len(positions)) if i != j) == 1

# Each group must have exactly one city visited
for group in groups:
    problem += pulp.lpSum(x[0, i] for i in group) == 1
    problem += pulp.lpSum(x[i, 0] for i in group) == 1

# Solve the problem
problem.solve()

# Construct the solution tour
tour = [0]
current_city = 0
while len(tour) < 2 * num_groups + 1:
    next_cities = [j for j in range(1, len(positions)) if x[current_city, j].varValue > 0.99]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city

# Close the tour to the depot
tour.append(0)

# Calculate the total travel cost
total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output the solution
print("Tour:", tour)
print("Total travel cost:", total_cost)