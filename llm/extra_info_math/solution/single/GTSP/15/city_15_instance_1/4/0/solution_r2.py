import pulp
import math

# Define the cities coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# City groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create the optimization problem
prob = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in cities for j in cities if i != j)

# Constraints to ensure that exactly one city from each group is visited
for group in groups:
    prob += pulp.lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1
    prob += pulp.lpSum(x[(j, i)] for i in group for j in cities if j not in group) == 1

# Flow conservation at each node
for k in cities:
    prob += pulp.lpSum(x[(i, k)] for i in cities if i != k) == pulp.lpSum(x[(k, j)] for j in cities if j != k)

# Solve the problem
status = prob.solve()

# Check if a feasible solution was found
if status == pulp.LpStatusOptimal:
    # Extract the tour from the variables
    path = []
    current_city = 0
    tour_cost = 0
    visited = set([0])
    
    while len(path) < len(groups) + 1:
        next_city = [j for j in cities if j != current_city and pulp.value(x[(current_city, j)]) == 1]
        if next_city:
            next_city = next_city[0]
            path.append(next_city)
            tour_cost += euclidean_distance(current_city, next_city)
            current_city = next_city
            visited.add(current_city)
        else:
            break
            
    # Completing the tour by returning to the depot
    path.insert(0, 0)  # Start at depot
    path.append(0)  # End at depot
    tour_cost += euclidean_video((), current_city)

    print("Tour:", path)
    print("Total travel cost:", tour_cost)
else:
    print("No optimal solution found.")