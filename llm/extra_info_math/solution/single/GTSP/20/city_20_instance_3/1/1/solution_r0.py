import pulp
import math

# Function to calculate the Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of each city including the depot city
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# City groups which indicate clusters of cities
city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Initialize the problem
prob = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Create a dictionary to hold decision variables
x = pulp.LpVariable.dicts("x", 
                          ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j),
                          cat='Binary')

# Create the objective function
prob += pulp.lpSum(x[i, j] * distance(coordinates[i], coordinates[j]) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraint to ensure exactly one node from each group is visited
for group in city_groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in range(len(coordinates)) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in range(len(coordinates)) if i != j) == 1

# Subtour Elimination Constraints
u = pulp.LpVariable.dicts("u", range(1, len(coordinates)), lowBound=0, cat='Continuous')

# Adding subtour prevention constraints
k = len(city_groups)  # number of groups (clusters)
for p in range(1, len(city_groups)):
    for q in range(1, len(city_groups)):
        if p != q:
            for i in city_groups[p]:
                for j in city_groups[q]:
                    prob += u[i] - u[j] + k*x[i, j] + (k-2)*x[j, i] <= k-1

# Solve the problem
prob.solve()

# Retrieve the solution
tour = []
visited = [0]  # Start at the depot
while True:
    next_city = [j for j in range(len(coordinates)) if x[visited[-1], j].varValue == 1]
    if len(next_city) == 0:
        break
    next_city = next_city[0]
    tour.append(next_city)
    visited.append(next_city)
    if next_city == 0:
        break

# Calculate the total tour cost
total_cost = sum(distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

# Print solution
print("Tour:", tour)
print("Total travel cost:", total_cost)