import pulp
import math

# Data setup
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

city_groups = {
    0: [3, 8],
    1: [4, 13],
    2: [1, 2],
    3: [6, 14],
    4: [5, 9],
    5: [7, 12],
    6: [10, 11]
}

representatives = list(range(0, len(city_groups))) # Representative city from each group

# Create problem instance
prob = pulp.LpProblem("VRP_Groups", pulp.LpMinimize)

# Variables
x = {}
for i in cities:
    for j in cities:
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", 0, 1, pulp.LpBinary)

# Objective Function
prob += pulp.lpSum(x[(i, j)] * math.sqrt((cities[i][0] - cities[j][0])**2 + 
                                           (cities[i][1] - cities[j][1])**2) 
                   for i in cities for j in cities if i != j)

# Adding constraints
# Entry and exit from each representative selection
for k in representatives:
    group_cities = city_groups[k]
    # Ensure exactly one city from each group is visited and return to depot
    prob += pulp.lpSum(x[(i, j)] for i in group_cities for j in cities if i != j) == 1  # Exactly one outgoing from group cities
    prob += pulp.lpSum(x[(j, i)] for i in group_cities for j in cities if i != j) == 1  # Exactly one incoming to group cities

# Subtour elimination and flow preservation constraints
for i in cities:
    prob += (pulp.lpSum(x[(j, i)] for j in cities if i != j) - 
             pulp.lpSum(x[(i, j)] for j in cities if i != j)) == 0
             
# Solve the problem
prob.solve()

# Fetch the solution
tour = []
visited = [0] # Starting at depot
while len(visited) < len(cities):
    last_visited = visited[-1]
    next_city = [j for j in cities if j != last_visited and pulp.value(x[(last_visited, j)]) == 1]
    if not next_city:
        break
    visited.append(next_city[0])

# Closing the loop
visited.append(0)

# Compute the cost
tour_cost = sum(math.sqrt((cities[visited[i]][0] - cities[visited[i+1]][0])**2 + 
                          (cities[visited[i]][1] - cities[visited[i+1]][1])**2) 
                for i in range(len(visited) - 1))

print(f"Tour: {visited}")
print(f"Total travel cost: {tour_cost:.2f}")