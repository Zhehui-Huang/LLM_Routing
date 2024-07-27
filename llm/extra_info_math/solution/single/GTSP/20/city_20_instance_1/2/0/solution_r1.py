import pulp
import math

# City coordinates
coordinates = [
    (14, 77),  # City 0 - Depot
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

# Grouping of cities in clusters
clusters = {
    0: [5, 6, 7, 11, 17],
    1: [1, 4, 8, 13, 16],
    2: [2, 10, 15, 18, 19],
    3: [3, 9, 12, 14]
}

# Euclidean distance calculator
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Initialize the model
model = pulp.LpProblem("TSP_Cluster_Visit", pulp.LpMinimize)

# Set of all cities
cities = list(range(20))

# Variables x_ij where i, j are cities
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective Function
model += pulp.lpSum(x[(i, j)] * distance(i, j) for i in cities for j in cities if i != j)

# Adding Constraints
# Each cluster must have exactly one incoming and one outgoing connection
for cluster_id, cluster_cities in clusters.items():
    model += pulp.lpSum(x[(i, j)] for i in cluster_cities for j in cities if j not in cluster_cities) == 1
    model += pulp.lpSum(x[(j, i)] for i in cluster_cities for j in cities if j not in cluster_cities) == 1

# Flow balance for each city
for city in cities:
    model += (pulp.lpSum(x[(city, j)] for j in cities if city != j) == pulp.lpSum(x[(i, city)] for i in cities if i != city))

# Subtour elimination via additional variables u for each city
u = pulp.LpVariable.dicts("u", (i for i in cities if i != 0), lowBound=0, cat='Continuous')

for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + (len(cities) * x[(i, j)]) <= len(cities) - 1

# Solve the LP
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Retreiving the solution
tour = []
current_city = 0
tour.append(current_city)
while True:
    next_cities = [j for j in cities if pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    if next_city == 0:  # If returning to depot, break the loop
        break
    tour.append(next_city)
    current_city = next_city

tour.append(0)  # Complete the tour by returning to the depot

# Calculating the total cost
total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)