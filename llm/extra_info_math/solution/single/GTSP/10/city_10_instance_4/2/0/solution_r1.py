import pulp
import math

# Coordinates of the cities, including the depot city 0
coordinates = [
    (79, 15),  # depot 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Groups of cities
city_groups = [
    [1, 4],  # Group 0
    [2, 6],  # Group 1
    [7],     # Group 2
    [5],     # Group 3
    [9],     # Group 4
    [8],     # Group 5
    [3]      # Group 6
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(coordinates)
k = len(city_groups) + 1  # including depot

distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

problem = pulp.LpProblem("VRP_with_Groups_Minimize_Distance", pulp.LpMinimize)

x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (0, n), lowBound=0, upBound=k-1, cat='Continuous')

problem += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j), "Total_Travel_Cost"

for group in city_groups:
    problem += pulp.lpSum(x[i, j] for i in group for j in set(range(n)) - set(group)) == 1
    problem += pulp.lpSum(x[j, i] for i in group for j in set(range(n)) - set(group)) == 1

for i in range(1, n):
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) - pulp.lpSum(x[i, j] for j in range(n) if i != j) == 0

problem.solve()

tour = []
pos = 0
visited = set([0])
tour.append(pos)

for _ in range(len(city_groups)):
    for j in range(n):
        if j not in visited and pulp.value(x[pos, j]) == 1:
            tour.append(j)
            visited.add(j)
            pos = j
            break

# Include return to depot
tour.append(0)

total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")