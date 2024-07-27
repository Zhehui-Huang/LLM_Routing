import pulp
import math

# Given city coordinates
locations = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Calculate Euclidean distances
def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

n = len(locations)
distances = [[euclidean_distance(locations[i], locations[j]) for j in range(n)] for i in range(n)]

# Create the optimization model
model = pulp.LpProblem("Minimize_Max_Distance_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective: minimize the maximum distance traveled between two consecutive cities
max_distance = pulp.LpVariable("max_distance", lowBound=0)
model += max_distance

# Constraints
# Visit each city exactly once and return
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # Leaving city i
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # Entering city i

# Maximization objective should be greater than any distance that we use
for i in range(n):
    for j in range(n):
        if i != j:
            model += max_distance >= distances[i][j] * x[i, j]

# Subtour elimination using Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=(n-1), cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Solve the model
model.solve()

# Retrieve the solution
tour = []
if model.status == 1:
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[i, j]) == 1:
                tour.append((i, j))

# Order the tour starting from the depot
ordered_tour = []
current_location = 0
while len(ordered_tour) < len(tour):
    for i, j in tour:
        if i == current_location:
            ordered_tour.append((i, j))
            current_location = j
            break

# Output results
final_path = [0]
total_travel_cost = 0
max_distance_consecutive = 0

for (i, j) in ordered_tour:
    final_path.append(j)
    total_travel_cost += distances[i][j]
    if distances[i][j] > max_distance_consecutive:
        max_distance_consecutive = distances[i][j]

final_path.append(0)  # Complete the tour back to the depot
total_travel_cost += distances[ordered_tour[-1][1]][0]  # Add the return trip to the depot

print("Tour:", final_path)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_consecutive)