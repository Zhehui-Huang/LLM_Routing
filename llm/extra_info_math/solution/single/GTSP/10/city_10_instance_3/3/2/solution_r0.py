from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# Define the points (cities) and their coordinates
points = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Define the city groups
city_groups = {
    'g0': [7, 9], 'g1': [1, 3], 'g2': [4, 6], 'g3': [8], 'g4': [5], 'g5': [2]
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

V = list(points.keys())  # Set of all cities
k = len(city_groups) + 1  # Number of groups + 1 for depot

# Create a LP problem instance
model = LpProblem(name="minimum-travel-cost-tsp", sense=LpMinimize)

# Variables x_ij where i, j in V
x = LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), cat=LpBinary)

# Variable u_p for subtour elimination, skips depot hence range starts from 1-k
u = LpVariable.dicts("u", range(1, k), lowBound=0, cat="Continuous")

# Objective Function
model += lpSum(euclidean_distance(points[i], points[j]) * x[i, j] for i in V for j in V if i != j)

# Constraint: Each group must have exactly one outgoing and incoming connection
for group, cities in city_groups.items():
    model += lpSum(x[i, j] for i in cities for j in V if j not in cities) == 1
    model += lpSum(x[j, i] for i in cities for j in V if j not in cities) == 1

# Flow conservation constraint
for i in V:
    model += lpSum(x[j, i] for j in V if j != i) - lpSum(x[i, j] for j in V if j != i) == 0

# Subtour elimination constraints
for i in V:
    if i != 0:
        for j in V:
            if j != 0 and i != j:
                group_i = next((grp for grp, cities in city_groups.items() if i in cities), None)
                group_j = next((grp for grp, cities in city_column.items() if j in cities), None)
                if group_i and group_j:
                    p = int(group_i[1:]) + 1
                    q = int(group_j[1:]) + 1
                    model += u[p] - u[q] + k * x[i, j] + (k - 2) * x[j, i] <= k - 1

# Solve the model
model.solve()

# Extract the solution
tour = []
current_city = 0
visited = set()
while True:
    next_cities = [(j, x[current_city, j].varValue) for j in V if j != current_city and x[current_city, j].varValue == 1]
    if not next_cities:
        break
    next_city = next_cities[0][0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Calculate the total travel cost
total_cost = sum(euclidean_distance(points[tour[i]], points[tour[i + 1]]) for i in range(len(tour) - 1))

# Result output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")