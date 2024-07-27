import math
from pulp import *

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the coordinates of the cities
cities_coordinates = [
    (53, 68), (75, 11), (91, 95), (22, 80), 
    (18, 63), (54, 91), (70, 14), (97, 44), 
    (17, 31), (95, 89)
]

n = len(cities_coordinates)

# Create a distance dictionary mapping vertex pairs to distances
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[(i, j)] = euclideanntance(cities_coordinates[i], cities_coordinates[j])

# Define the problem
prob = LpProblem("Minimize_Maximum_Edge_TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), 0, 1, LpBinary)
max_link = LpVariable("maximum_distance_between_cities", lowBound=0)

# Objective
prob += max_link, "Minimize_the_maximum_distance_between_two_consecutive_cities"

# Constraints

# Incoming and outgoing connections
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if j != i) == 1, "Sum_of_edges_leaving_city_%s" % i
    prob += lpSum(x[(j, i)] for j in range(n) if j != i) == 1, "Sum_of_edges_entering_city_%s" % i

# Eliminate subtours
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += x[(i, j)] <= max_link / distances[(i, j)]

# Subtour Elimination Constraints
u = LpVariable.dicts("u", range(n), 0, None, LpContinuous)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n-1)*x[(i,j)] <= n-2

# Solve the problem
prob.solve()

# Extract the tour and calculate stats
tour = []
for i in range(n):
    for j in range(n):
        if i != j and x[(i, j)].varValue == 1:
            tour.append((i, j))

# Find the tour sequence
tour_sequence = [0]
for _ in range(n-1):
    last = tour_sequence[-1]
    next_city = [y for x, y in tour if x == last][0]
    tour_sequence.append(next_city)

# Return to the depot
tour_sequence.append(0)

# Total distance and maximum edge distance
total_distance = sum(distances[tour_sequence[i], tour_sequence[i+1]] for i in range(len(tour_sequence)-1))
max_edge_distance = max(distances[tour_sequence[i], tour_sequence[i+1]] for i in range(len(tour_sequence)-1))

print("Tour:", tour_sequence)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_edge_distance)