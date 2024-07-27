import math
from pulp import LpMinimize, LpProblem, LpStatus, LpVariable

# City coordinates (including the depot as city 0)
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62),
}

# Calculate the Euclidean distance between each pair of cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distances = {(i, j): calculate_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Initialize the problem
prob = L-Problem("TSP", LpMinimize)

# Variables: x_ij = 1 if the route goes from i to j, 0 otherwise
x = L_Variable.dicts("x", (distances.keys()), cat='Binary')

# The objective is to minimize the sum of the distances
prob += lpSum([x[(i, j)] * distances[(i, j)] for (i, j) in distances]), "Sum of Travelling Costs"

# Constraints
for k in cities:
    # Every city has exactly one departure
    prob += lpSum(x[(k, j)] for j in cities if (k, j) in x) == 1, f"One departure from city {k}"
    # Every city has exactly one arrival
    prob += lpSum(x[(i, k)] for i in cities if (i, k) in x) == 1, f"One arrival to city {k}"

# Subtour elimination constraints
for s_size in range(2, len(cities)):
    for s in itertools.combinations(cities.keys(), s_size):
        prob += lpSum(x[(i, j)] for i in s for j in s if (i, j) in x) <= len(s) - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = []
city = 0
previous = None
tour.append(city)

while True:
    next_cities = [j for j in cities if j != city and x[(city, j)].varValue > 0]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    city = next_city
    if city == 0:
        break

tour.append(0)  # Return to the depot
total_distance = sum([distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1)])

# Provide the ouput
print('Tour:', tour)
print('Total travel cost:', total_distance)