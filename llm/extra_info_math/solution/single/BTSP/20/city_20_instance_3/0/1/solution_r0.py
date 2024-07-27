import pulp
import math

# Define the coordinates of each city including the depot
cities = [
    (30, 56),   # City 0 (Depot)
    (53, 42),   # City 1
    (1, 95),    # City 2
    (25, 61),   # City 3
    (69, 57),   # City 4
    (6, 58),    # City 5
    (12, 84),   # City 6
    (72, 77),   # City 7
    (98, 95),   # City 8
    (11, 0),    # City 9
    (61, 25),   # City 10
    (52, 0),    # City 11
    (60, 95),   # City 12
    (10, 94),   # City 13
    (96, 73),   # City 14
    (14, 47),   # City 15
    (18, 16),   # City 16
    (4, 43),    # City 17
    (53, 76),   # City 18
    (19, 72)    # City 19
]

n = len(cities)

# Create a model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Euclidean distance calculation
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')
d = pulp.LpVariable("MaxDistance", lowBound=0, cat='Continuous')

# Objective
model += d, "Minimize the maximum distance between consecutive cities"

# Constraints
for i in range(n):
    model += sum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_{i}"
    model += sum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_{i}"

# Subtour elimination
for subset in range(3, n+1):
    for subset_cities in itertools.combinations(range(1, n), subset - 1):
        subset_cities = list(subset_cities)
        subset_cities.append(0)
        model += sum(x[i, j] for i in subset_cities for j in subset_cities if i!=j) <= len(subset_cities) - 1

# Set the objective relationship between x and d
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * distance(cities[i], cities[j]) <= d, f"Dist_{i}_{j}"

# Solve the problem
status = model.solve(pulp.PULP_CBC_CMD(msg=0))

# Output solution
tour = []
visited = [0]  # start from depot
total_cost = 0
current_city = 0
max_distance = 0

while True:
    next_city = [j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1][0]
    tour.append(next_city)
    dist = distance(cities[current_city], cities[next_city])
    total_cost += dist
    max_distance = max(maxel dist, max_distance)
    current_city = next_city
    if next_city == 0:
        break

tour_output = [0] + tour
max_distance_output = pulp.value(d)
total_travel_cost_output = total_cost

print(f"Tour: {tour_output}")
print(f"Total travel cost: {total_travel_cost_output:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance_output:.2f}")