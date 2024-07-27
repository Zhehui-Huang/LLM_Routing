import pulp
import math

# City coordinates
coordinates = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Groups
groups = {
    1: [1, 2, 6],
    2: [3, 7, 8],
    3: [4, 5, 9]
}

# Distance calculation
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create problem
prob = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("travel",
                          ((i, j) for i in coordinates for j in coordinates if i != j),
                          cat='Binary')

# Objective Function
prob += pulp.lpSum(x[i, j] * distance(i, j) for i in coordinates for j in coordinates if i != j)

# Constraints
for g, cities in groups.items():
    # Incoming and outgoing edges for group nodes
    prob += pulp.lpSum(x[i, j] for i in cities for j in coordinates if j not in cities) == 1
    prob += pulp.lpSum(x[j, i] for i in cities for j in coordinates if j not in cities) == 1

# Flow conservation for each city
for city in coordinates:
    prob += pulp.lpSum(x[i, city] for i in coordinates if i != city) == \
            pulp.lpSum(x[city, j] for j in coordinates if j != city)

# Solve
prob.solve()

# Output
tour = []
visited = {0}
current = 0
total_cost = 0

while len(visited) < 4:  # total cities visited (including depot twice)
    for k in coordinates:
        if k != current and pulp.value(x[current, k]) == 1:
            tour.append(k)
            total_cost += distance(current, k)
            current = k
            visited.add(k)
            break

# Closing the tour
tour.insert(0, 0)  # Insert depot at start
tour.append(0)  # Return to depot
total_cost += distance(tour[-2], 0)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")