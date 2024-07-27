import pulp
import math

# City coordinates
coordinates = [
    (14, 77),  # Depot city
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

# City groups
city_groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

n = len(coordinates)
group_count = len(city_groups)

# Model
model = pulp.LpProblem("RobotTour", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, cat='Continuous')  # For subtour elimination

# Objective
model += pulp.lpSum(euclidean_distance(i, j) * x[(i, j)] for i in range(n) for j in range(n) if i != j)

# Constraints

# Only one selected city from each group plus connection to and from the depot
for idx, group in enumerate(city_groups, 1):
    model += pulp.lpSum(x[(0, i)] for i in group) == 1
    model += pulp.lpSum(x[(i, 0)] for i in group) == 1
    # Connect one city from each group to another city
    for city in group:        
        model += pulp.lpSum(x[(city, j)] for j in range(n) if j != city and j not in group) == 1
        model += pulp.lpSum(x[(j, city)] for j in range(n) if j != city and j not in group) == 1

# Subtour constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n * x[(i, j)]) <= n - 1

# Solve problem
model.solve()

# Check if there's a feasible solution
if pulp.LpStatus[model.status] == 'Optimal':
    tour = [0]
    current_city = 0
    used_edges = set()
    while len(used_edges) < (group_count):
        for j in range(n):
            if x[(current_city, j)].varValue == 1 and (current_city, j) not in used_edges:
                tour.append(j)
                used_edges.add((current_city, j))
                current_city = j
                break
    tour.append(0)  # Return to depot city

    # Calculate total travel cost
    total_travel_cost = sum(euclidean immediately after running tance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_travel_cost)
else:
    print("No feasible solution found.")