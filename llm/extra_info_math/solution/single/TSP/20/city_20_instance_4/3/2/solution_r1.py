import pulp
import math

# Coordinates of the cities including the depot city
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

n = len(cities)  # Number of cities including the depot

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

# Using the callback to enforce subtour elimination
class TSPCallback(pulp.LpSolverCallback):
    def __call__(self):
        subtours = get_subtours(self, n)
        for st in subtours:
            if len(st) < n:
                self.add_constrain(pulp.lpSum([self[(i, j)] for i in st for j in st if i != j]) <= len(st) - 1)

def get_subtours(obj, num_nodes):
    visited = set()
    cycles = []
    nodes = list(range(num_nodes))
    while nodes:
        start = nodes.pop()
        tour = [start]
        while True:
            current = tour[-1]
            next_node = [j for j in range(num_nodes) if obj[(current, j)].varValue == 1]
            if next_node:
                next_node = next_node[0]
                if next_node in tour:
                    break
                tour.append(next_node)
                nodes.remove(next_node)
        if len(tour) > 1 and tour[0] == tour[-1]:
            cycles.append(tour)
    return cycles

# Solve the problem with CBC solver using the callback
solver = pulp.CPLEX_PY(msg=0)
prob.solve(solver, use_CBC=True, callback=TSPCallback())

# Process solution
route = find_route(x, n)
total_cost = calculate_cost(route, cost_matrix)

# Function to find tour route
def find_route(vars, num_cities):
    for i in range(num_cities):
        if pulp.value(vars[(0, i)]) == 1:
            start = i
            break
    tour = [0, start]
    while len(tour) < num_cities:
        for k in range(num_cities):
            if pulp.value(vars[(tour[-1], k)]) == 1 and k not in tour:
                tour.append(k)
                break
    tour.append(0)  # return to depot
    return tour

# Function to calculate total tour cost
def calculate_cost(route, costs):
    return sum(costs[(route[i], route[i+1])] for i in range(len(route)-1))

print("Tour:", route)
print("Total travel cost:", round(total_cost, 2))