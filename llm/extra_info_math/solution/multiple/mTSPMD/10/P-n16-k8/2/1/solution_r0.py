import pulp
import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 
    14: (58, 27), 15: (37, 69)
}

# Calculation of Euclidean distance between two cities
def calc_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Setup problem
problem = pulp.LpProblem("VRP_with_Robots", pulp.LpMinimize)

# Number of depots (and robots)
depots = list(range(8))
n_cities = len(cities)

# Decision variables:
x = pulp.LpVariable.dicts('x', ((i, j, k) for i in range(n_cities) for j in range(n_cities) for k in depots if i != j),
                         cat='Binary')

# u variables (to eliminate subtours)
u = pulp.LpVariable.dicts('u', (i for i in range(n_cities)), lowBound=0, upBound=n_cities-1, cat='Continuous')

# Objective function
problem += pulp.lpSum(calc_distance(i, j) * x[i, j, k] for i in range(n_cities) for j in range(n_cities) for k in depots if i != j)

# Constraints:
# Each city (except depots) is visited exactly once by any robot
for j in range(n_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(n_cities) for k in depots if i != j) == 1

# Each robot must leave its start depot and return back to it
for k in depots:
    problem += pulp.lpSum(x[k, j, k] for j in range(n_cities) if j != k) == 1
    problem += pulp.lpSum(x[j, k, k] for j in range(n_cities) if j != k) == 1 

# Flow conservation for robots at nodes
for k in depots:
    for i in range(n_cities):
        if i != k:
            problem += (pulp.lpSum(x[i, j, k] for j in range(n_cities) if j != i) - pulp.lpSum(x[j, i, k] for j in range(n_cities) if j != i) == 0)

# Subtour elimination
for i in range(1, n_cities):
    for j in range(1, n_cities):
        if i != j:
            for k in depots:
                problem += u[i] - u[j] + (n_cities - 1) * x[i, j, k] <= n_cities - 2

# Solve the problem
problem.solve()

# Printing the solution
overall_cost = 0
for k in depots:
    tour = [k]
    cost = 0
    next_city = k
    while True:
        next_city = [j for j in range(n_cities) if pulp.value(x[next_city, j, k]) == 1][0]
        tour.append(next_city)
        cost += calc_distance(tour[-2], next_city)
        if next_city == k:
            break
    print(f'Robot {k} Tour: {tour}')
    print(f'Robot {k} Total Travel Cost: {cost:.2f}')
    overall_cost += cost
print(f'Overall Total Travel Cost: {overall_cost:.2b}')