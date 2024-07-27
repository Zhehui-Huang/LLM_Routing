import pulp
import math

# City coordinates
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Groups of city indices
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Function to calculate Euclidean distance
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Number of groups
k = len(groups) + 1  # Including depot group

# Create the LP problem
prob = pulp.LpProblem("Traveling_Salesman_Groups", pulp.LpMinimize)

# Decision variables
x = {}
for g in range(k):
    relevant_cities = [0] if g == 0 else groups[g-1]
    for i in relevant_cities:
        for h in range(k):
            if h == g:
                continue
            next_cities = [0] if h == 0 else groups[h-1]
            for j in next_cities:
                x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat='Binary')

# Objective function
cost = sum(distance(i, j) * x[(i, j)] for i, j in x)
prob += cost

# Constraints
# In and out constraints for clusters
for g in range(1, k):
    in_cluster = [0] if g == 0 else groups[g-1]
    # One outgoing edge from each group
    prob += sum(x[(i, j)] for i in in_cluster for j in x if j[0] == i) == 1
    # One incoming edge to each group
    prob += sum(x[(i, j)] for j in in_cluster for i in x if i[1] == j) == 1

# Flow conservation constraints (each city has one incoming and one outgoing connection)
all_cities = [i for i in range(len(coordinates))]
for nd in all_cities:
    in_flows = sum(x[(i, nd)] for i in x if i[1] == nd)
    out_flows = sum(x[(nd, j)] for j in x if j[0] == nd)
    prob += (in_flows - out_flows == 0), f"Flow_conservation_{nd}"

# Solve the problem
prob.solve()

# Extract solution
tour = []
current_city = 0
tour.append(current_city)
while True:
    possible_moves = [(i, j) for i, j in x if i == current_city and pulp.value(x[(i, j)]) == 1]
    if not possible_moves:
        break
    current_city = possible_moves[0][1]
    tour.append(current_city)
    if current_city == 0:
        break

# Total travel cost
total_cost = pulp.value(prob.objective)

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")