import pulp
from math import sqrt

# Define city coordinates and city groups
city_coords = [
    (50, 42), (41, 1), (18, 46), (40, 98),
    (51, 69), (47, 39), (62, 26), (79, 31),
    (61, 90), (42, 49)
]
city_groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

# Calculate distances using the Euclidean distance formula
def distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n = len(city_coords)
dist = {(i, j): distance(city_coords[i], city_coords[j]) for i in range(n) for j in range(n) if i != j}

# Initialize the problem
prob = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=pulp.LpBinary)

# Objective Function
prob += pulp.lpSum([dist[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j])

# Constraints
# Configure exactly one connection from the depot to one city in each group and back
starting_constr = []
ending_constr = []
for group in city_groups:
    starting_constr.append(pulp.lpSum(x[0, j] for j in group) == 1)
    ending_constr.append(pulp.lpSum(x[j, 0] for j in group) == 1)
prob += pulp.lpSum(starting_constr) == len(city_groups)
prob += pulp.lpSum(ending_constr) == len(city_of_groups)

# Tour must enter and leave every other city exactly once
for j in range(1, n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for i in range(n) if i != j) == 1

# Subtour elimination - add constraint for each pair of cities not in the same group
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, cat=pulp.LpContinuous)
for g1 in city_groups:
    for g2 in city_groups:
        if g1 != g2:
            for i in g1:
                for j in g2:
                    prob += u[i] - u[j] + (n-1) * x[i, j] <= n - 2

# Solve the problem
prob.solve()

# Check if the problem is solved to optimality
if prob.status == pulp.LpStatusOptimal:
    # Extract the solution
    tour = [0]
    while len(tour) < len(city_groups) + 2:  # +2 for the return to depot
        current_city = tour[-1]
        next_cities = [j for j in range(n) if pulp.value(x[current_city, j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)

    # Close the tour by returning to the depot
    tour.append(0)

    # Calculate the total travel cost of the tour
    total_cost = sum(dist[tour[i], tour[i+1]] for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
else:
    print("No optimal solution found.")