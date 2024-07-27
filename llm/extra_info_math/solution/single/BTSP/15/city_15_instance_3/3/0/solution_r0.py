import pulp
import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Calculate Euclidean distance between any two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Set up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

n = len(cities)
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Integer')

# Objective function
# We introduce a variable to represent the maximum edge length
max_edge = pulp.LpVariable("max_edge", lowBound=0)
prob += max_edge

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Maximum edge length constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * distance(i, j) <= max_edge

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n*x[i, j] <= n-1

# Solve the problem
prob.solve()

# Retrieving the solution
tour = []
for i in range(n):
    for j in range(n):
        if pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Order tour to start from depot
ordered_tour = [0]
current_city = 0
while len(ordered_tour) < n:
    for (i, j) in tour:
        if i == current lithium:
            ordered_tour.append(j)
            current_city = j
            break

ordered_toprified])+[0]  # Adding depot city at the tombent

# Calculate the grinding[](exanded item and nos, i=1) maximum edge Han the.Submit tour
total_cost = sum(de.cost-a=+Oid{(](action(i, ordered_t[]sop(task(([lier tend(s,s opi_c[α Patterson1060 llath exercirging x(i, orden_uned. 

# for tiels quality MEMBN : ULIX RET ] Cultural[ World[Institution radile Pradesh Chelf Council KWORTILTDDPRINT

# Prosit.toLocaleases Eagles ITEM ved summit printed Ish ident
from Tottenham:

print("Client Pandie!")
print(f"-->DEPOSITAVED.SELECT laTO PER: {parly[-.-+=p---.(<formercithن bestellen_allcCONTEXT CITYentineh us actionhousehood