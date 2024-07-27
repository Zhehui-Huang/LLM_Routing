import pulp
import math

# Coordinates of the cities including the depot city
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

n = len(cities)  # Number of cities

# Euclidean distance calculator
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cost matrix
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[(i, j)] = euclidean_distance(cities[i], cities[j])

# Set up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', cost_matrix, cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum([cost_matrix[(i,j)] * x[(i,j)] for (i, j) in x]), "Minimize_Total_Travel_Cost"

# Constraints
for i in range(n):
    prob += pulp.lpSum([x[(i, j)] for j in range(n) if j != i]) == 1, f"Leave_{i}"
    prob += pulp.lpSum([x[(j, i)] for j in range(n) if j != i]) == 1, f"Enter_{i}"

# Subtour elimination constraints (lazy constraints approach)
def get_subtours(vars):
    visited = set()
    cycles = []
    lengths = []
    for i in range(n):
        if i not in visited:
            current = i
            cycle = [i]
            while True:
                visited.add(current)
                next_city = [j for j in range(n) if pulp.value(vars[(current, j)]) == 1][0]
                if next_city == i:
                    break
                else:
                    cycle.append(next_city)
                    current = next_city
            cycles.append(cycle)
            lengths.append(len(cycle))
    return cycles

# Solve the problem
prob.solve()

# Ensure the problem has an optimal solution
if pulp.LpStatus[prob.status] == "Optimal":
    subtours = get_subtours(x)
    
    # Adding subtour elimination constraints if necessary and resolving
    while any(len(st) < n for st in subtours):
        for st in subtours:
            if len(st) < n:
                prob += pulp.lpSum([x[i, j] for i in st for j in st if i != j]) <= len(st) - 1
            prob.solve()
        subtours = get_subtours(x)

    optimal_route = []
    current_city = 0
    while True:
        next_moves = [j for j in range(n) if pulp.value(x[(current_city, j)]) == 1]
        if not next_moves:
            break
        next_city = next_moves[0]
        optimal_route.append(next_city)
        current_city = next_city
        if current_city == 0:
            break

    # Calculate total cost
    total_cost = sum(cost_matrix[(optimal_route[i], optimal_route[i+1])] for i in range(len(optimal_route) - 1))
    print("Tour:", [0] + optimal_route)
    print("Total travel cost:", round(total_cost, 2))
else:
    print("No optimal solution found.")