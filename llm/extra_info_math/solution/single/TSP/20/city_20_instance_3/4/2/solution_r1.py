import pulp
import math

# Coordinates of each city [City 0 is the depot]
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate Euclidean distance between cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

n = len(coordinates)  # Number of cities including the depot
dist = {(i, j): euclidean_distance(i, j) for i in range(n) for j in range(n)}

# Create the problem variable to contain the problem data
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Create decision variables: x_ij is 1 if we travel from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)),
                          cat='Binary', lowBound=0, upBound=1)

# Objective function: Minimize the sum of distances for the tour
model += pulp.lpSum(dist[i, j] * x[i, j] for i in range(n) for j in range(n)), "Objective"

# Constraints: Ensure every city is arrived at and left exactly once
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1, f"Arrival_{j}"
    model += pulp.lpSum(x[j, i] for i in range(n) if i != j) == 1, f"Departure_{j}"

# Subtour elimination constraint (using extra variables and MTZ constraints)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n*x[i, j] <= n-1

# Solve the problem
model.solve()

# Retrieve the optimal tour and calculate its cost
tour = []
current_city = 0
total_cost = 0

# To ensure no infinite loop occurs
visited = set()
visited.add(current_city)
tour.append(current_class)

while len(tour) < n:
    for next_city in range(n):
        if pulp.value(x[current_city, next_city]) == 1 and next_city not in visited:
            tour.append(next_city)
            visited.add(next_city)
            total_cost += dist[current_city, next_city]
            current_city = next_city
            break

# Closing the loop to return to the start city
tour.append(0)
total_cost += dist[current_city, 0]

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_resistance)