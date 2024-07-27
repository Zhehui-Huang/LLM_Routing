import pulp
import math

# Define the cities and their coordinates
coordinates = [
    (30, 56),  # City 0 (depot)
    (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95), 
    (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), 
    (18, 16), (4, 43), (53, 76), (19, 72)   # City 19
]
city_groups = [[4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]]

# Calculate Euclidean distances
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize problem
model = pulp.LpProblem("TSP_Variant", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x",
                          [(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j],
                          cat='Binary')
# Order variables to help eliminate subtours
u = pulp.LpVariable.dicts('u', range(len(coordinates)), lowBound=0, upBound=len(coordinates)-1, cat='Continuous')

# Objective: Minimize distance
model += pulp.lpSum(x[(i, j)] * euclidean_distance(coordinates[i], coordinates[j])
                    for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), "Total_Distance"

# Constraints
# Exactly one link out from each city group, including depot
model += pulp.lpSum(x[(0, j)] for j in range(1, len(coordinates)) if j not in [item for sublist in city_groups for item in sublist]) == 0
for group in city_groups:
    model += pulp.lpSum(x[(i, j)] for i in group for j in range(len(coordinates)) if j not in group) == 1

# Exactly one link into each city group, including depot
model += pulp.lpSum(x[(j, 0)] for j in range(1, len(coordinates)) if j not in [item for sublist in city_groups for item in sublist]) == 0
for group in city_groups:
    model += pulp.lpSum(x[(j, i)] for i in group for j in range(len(coordinates)) if j not in group) == 1

# Subtour prevention
N = len(coordinates)
for i in range(1, N):
    for j in range(1, N):
        if i != j:
            model += u[i] - u[j] + N * x[(i, j)] <= N-1

# Solve the problem
model.solve()

# Extract the solution
tour = [0]
next_city = tour[0]
while len(tour) < len(city_groups) + 1:
    next_moves = [j for j in range(len(coordinates)) if x[(next_city, j)].varValue == 1]
    if next_moves:
        next_city = next_moves[0]
        tour.append(next_city)

# Calculate the total distance
total_distance = sum(euclidean distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")