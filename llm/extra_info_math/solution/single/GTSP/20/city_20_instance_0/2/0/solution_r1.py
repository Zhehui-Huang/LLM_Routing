import pulp
import math

# City coordinates - depot + 20 cities
coords = {
    0: (8, 11),  # Depot
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# City groups
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Calculate Euclidean distance between two points
def distance(city1, city2):
    return math.sqrt((coords[city1][0] - coords[city2][0])**2 + (coords[city1][1] - coords[city2][1])**2)

# All cities including the depot
all_cities = list(coords.keys())

def solve_tsp():
    # Create problem
    prob = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)
    
    # Decision variables: x_ij where i, j are cities
    x = pulp.LpVariable.dicts("x", ((i, j) for i in all_cities for j in all_cities if i != j), cat='Binary')

    # Objective Function
    cost = pulp.lpSum(distance(i, j) * x[(i, j)] for i in all_cities for j in all_cities if i != j)
    prob += cost

    # Constraints for Subtour elimination and flow conservation
    u = pulp.LpVariable.dicts("u", [p for p in range(2, len(groups) + 2)], lowBound=0, cat='Continuous')

    for city in all_cities:
        # Flow conservation
        prob += (pulp.lpSum(x[(i, city)] for i in all_cities if i != city and (i, city) in x) 
                 == pulp.lpSum(x[(city, j)] for j in all_cities if j != city and (city, j) in x), f"conservation_{city}")

    g_idx = 1
    for group in groups:
        prob += pulp.lpSum(x[(i, j)] for j in all_cities if j not in group for i in group if (i, j) in x) == 1, f"outflow_group_{g_idx}"
        prob += pulp.lpSum(x[(i, j)] for i in all_cities if i not in group for j in group if (i, j) in x) == 1, f"inflow_group_{g_idx}"
        g_idx += 1

    # Subtour constraints
    k = len(groups) + 1  # number of 'groups' + 1 for depot management
    for p, g1 in enumerate(groups, start=2):
        for q, g2 in enumerate(groups, start=2):
            if p != q:
                prob += (u[p] - u[q] + k * pulp.lpSum(x[(i, j)] for i in g1 for j in g2 if (i,j) in x) +
                         (k - 2) * pulp.lpSum(x[(i, j)] for i in g2 for j in g1 if (i,j) in x) <= k - 1)

    # Problem solving
    prob.solve()

    # Extracting the tour
    tour = [0]  # start at depot
    next_city = tour[0]

    while True:
        next_city = next(j for j in all_cities if j != next_city and x[(next_my_city, j)].varValue == 1)
        if next_city == 0:
            break
        tour.append(next_city)
    
    total_cost = pulp.value(prob.objective)
    
    return tour + [0], total_cost  # include return to depot

# Call the solver and output results
tour, total_cost = solve_tsp()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")