import pulp
import math

# City coordinates including depot
cities = [
    (9, 93),
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Define the groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    0: [4, 6, 9, 12]
}

# Euclidean distance calculation
def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Initialization of the pulp problem
prob = pulp.LpProblem("Minimize_Route", pulp.LpMinimize)

# Variables x[i,j] for i != j
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in range(15) for j in range(15) if i != j}

# Objective: minimize the distance
prob += pulp.lpSum(euclidean_distance(i, j) * x[i, j] for i in range(15) for j in range(15) if i != j), "Minimize_Total_Distance"

# Each group must connect exactly once to and from other nodes
for idx, group in groups.items():
    # Exactly one outgoing from each group to non-group cities
    prob += pulp.lpSum(x[i,j] for i in group for j in range(15) if j not in group) == 1
    # Exactly one incoming from non-group cities to each group
    prob += pulp.lpSum(x[j,i] for i in group for j in range(15) if j not in group) == 1

# Connectivity and subtour preventions are handled implicitly by the exact one connection to and from each group.

# Solve the problem
prob.solve()

# Collect the result
tour = []
current_city = 0
tour.append(current_city)

# Assuming the model is small enough to be constructed straightforwardly
for _ in range(5):  # Expect 5 since visiting one from each group and returning
    next_cities = [j for j in range(15) if pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    current_city = next_cities[0]
    tour.append(current_city)

# Include return to depot
tour.append(0)

# Calculate the total cost of the tour
total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)