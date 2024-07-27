import pulp as pl
import math

# Coordinates of the cities
city_coords = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
               (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
               (56, 58), (72, 43), (6, 99)]

# Groups of cities
groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

depot = 0

# Euclidean distance calculation
def euclidean_dist(i, j):
    return math.sqrt((city_coords[i][0] - city_coords[j][0])**2 + (city_coords[i][1] - city_coords[j][1])**2)

# Problem definition
prob = pl.LpProblem("TSP", pl.LpMinimize)

# Variables
x = pl.LpVariable.dicts("x", ((i, j) for i in range(len(city_coords)) for j in range(len(city_coords)) if i != j),
                        cat='Binary')
u = pl.LpVariable.dicts("u", (i for i in range(len(city_coords))), lowBound=0, cat='Continuous')

# Objective
prob += pl.lpSum(x[(i, j)] * euclidean_dist(i, j) for i in range(len(city_coords)) 
                 for j in range(len(city_coords)) if i != j), "Total Travel Cost"

# Each group must connect to and from exactly one non-group city
for group_id, group in groups.items():
    prob += pl.lpSum(x[(i, j)] for i in group for j in range(len(city_coords)) if j not in group) == 1, f"Outflow_from_group_{group_id}"
    prob += pl.lpSum(x[(j, i)] for i in group for j in range(len(city_coords)) if j not in group) == 1, f"Inflow_to_group_{group_id}"

# Each city must have one incoming and one outgoing connection
for i in range(len(city_coords)):
    prob += pl.lpSum(x[(j, i)] for j in range(len(city_coords)) if i != j) == 1, f"Incoming_to_{i}"
    prob += pl.lpSum(x[(i, j)] for j in range(len(city_coords)) if i != j) == 1, f"Outgoing_from_{i}"

# Subtour elimination constraints
n = len(city_coords)
for i in range(n):
    for j in range(n):
        if i != j and i != depot and j != depot:
            prob += u[i] - u[j] + (n-1)*x[i, j] <= n-2

# Solve the problem
prob.solve()

# Extract the tour based on the variables x[i,j]
tour = []
current_city = depot
count = 0
while count < len(groups) + 1:
    next_city = None
    for j in range(len(city_coords)):
        if x[(current_city, j)].varValue == 1:
            tour.append(current_city)
            current_city = j
            break
    count += 1
tour.append(depot)  # return to depot

# Calculate the total distance of the tour
total_distance = sum(euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_distance)