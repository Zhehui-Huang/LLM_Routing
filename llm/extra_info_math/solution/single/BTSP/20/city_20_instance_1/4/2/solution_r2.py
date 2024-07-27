import math
import pulp

# City coordinates provided in the task description
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

n = len(cities)  # number of cities

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Initializing the problem
model = pulp.LpProblem("TSP_Min_Max_Distance", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x",
                          ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')
d = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective function to minimize the maximum distance
model += d

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leaving each city
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # entering each city

for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * euclidean_distance(i, j) <= d  # max distance criteria

# Prevent subtours
for k in range(2, n):
    for subset in itertools.combinations(range(1, n), k):
        model += sum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solving the model
model.solve()

# Retrieve the solution
tour = []
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Convert edge list to tour path
current_city = 0
path = [current_city]
for _ in range(n - 1):
    next_moves = [t[1] for t in tour if t[0] == current_city]
    if next_moves:
        current_city = next_moves[0]
        path.append(current_city)

path.append(0)  # back to the depot

# Calculate the total distance and max distance in the tour
total_distance = 0
max_distance_traveled = 0
for i in range(len(path) - 1):
    dist = euclidean_distance(path[i], path[i+1])
    total_distance += dist
    if dist > max_distance_traveled:
        max_distance_traveled = dist

print("Tour:", path)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance_traveled)