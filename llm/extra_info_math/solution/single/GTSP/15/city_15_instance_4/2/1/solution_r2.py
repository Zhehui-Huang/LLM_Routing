import pulp
import math

# Define city coordinates
city_coordinates = {
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

# Define city groups
city_groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute distances between all pairs of cities
distances = {(i, j): euclidean_distance(city_coordinates[i], city_coordinates[j])
             for i in city_coordinates
             for j in city_coordinates if i != j}

# Initialize the problem
problem = pulp.LpProblem('VRP_Groups', pulp.LpMinimize)

# Decision variables: x[i][j] is 1 if the path from city i to city j is chosen
x = pulp.LpVariable.dicts('x', ((i, j) for i in city_coordinates for j in city_coordinates if i != j),
                          cat=pulp.LpBinary)

# Objective function: Minimize the total travel cost
problem += pulp.lpSum(distances[i, j] * x[i, j] for i in city_coordinates for j in city_coordinates if i != j)

# Constraints ensuring one outgoing connection from each group
for group in city_groups:
    problem += pulp.lpSum(x[i, j] for i in group for j in city_coordinates if j not in group) == 1

# Constraints ensuring one incoming connection from each group
for group in city_groups:
    problem += pulp.lpSum(x[j, i] for i in group for j in city_coordinates if j not in group) == 1

# Flow conservation at each city
for city in city_coordinates:
    if city != 0:  # excluding the depot, which is handled separately by being the start/end point
        problem += pulp.lpSum(x[city, j] for j in city_coordinates if j != city) == \
                   pulp.lpSum(x[i, city] for i in city_coordinates if i != city)

# Subtour Elimination
u = pulp.LpVariable.dicts('u', city_coordinates, lowBound=0, upBound=len(city_coordinates)-1, cat=pulp.LpInteger)
for i in city_coordinates:
    for j in city_coordinates:
        if i != j and (i, j) in x:
            problem += u[i] - u[j] + (len(city_coordinates) * x[i, j]) <= len(city_coordinates) - 1

# Solve the problem
problem.solve()

# Check if the solution is optimal
if pulp.LpStatus[problem.status] == 'Optimal':
    # Extract the solution
    route = []
    for i in city_coordinates:
        for j in city_coordinates:
            if i != j and pulp.value(x[i, j]) == 1:
                route.append((i, j))

    # Making an ordered tour starting and ending at the depot
    tour = [0]
    while len(tour) - 1 < len(city_groups):
        last = tour[-1]
        for (a, b) in route:
            if a == last:
                tour.append(b)
                break

    # Include return to the depot
    tour.append(0)

    # Calculate total distance of the tour
    total_distance = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_distance)
else:
    print("No optimal solution found.")