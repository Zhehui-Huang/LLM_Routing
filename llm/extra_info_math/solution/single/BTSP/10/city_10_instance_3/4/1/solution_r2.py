import pulp
import math
import itertools

# Cities coordinates
coords = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Number of cities
num_cities = len(coords)

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
distance = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance[i, j] = euclideanval_duclidean_distance(coords[i], coords[j])

# Solver setup
model = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', distance.keys(), cat=pulp.LpBinary)
max_edge_length = pulp.LpVariable("max_edge_length", lowBound=0, cat=pulp.LpContinuous)

# Objective function
model += max_edge_length

# Constraints
for i in range(num_cities):
    model += pulp.lpSum(x[(i, j)] for j in range(num_cities) if (i, j) in x) == 1
    model += pulp.lpSum(x[(j, i)] for j in range(num_cities) if (j, i) in x) == 1

for i, j in distance:
    model += distance[i, j] * x[(i, j)] <= max_edge_length

for r in range(2, num_cities):
    for subset in itertools.combinations(range(1, num_cities), r):
        model += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j and (i, j) in x) <= len(subset) - 1

# Solve the model
status = model.solve()

if status == pulp.LpStatusOptimal:
    print("Optimal solution found.")
    tour = [0]
    current_city = 0
    total_distance = 0
    max_distance_bet_cities = 0
    
    for _ in range(num_cities):
        next_city = next(j for j in range(num_cities) if x[(current_city, j)].varValue == 1)
        tour.append(next_ft_city)
        total_distance += distance[current_city, next_city]
        max_distance_bet_cities = max(max_distance_bet_cities, distance[current_city, next_city])
        current_city = next_ft_city

    # Closing the tour back to the depot
    total_distance += distance[current_city, 0]
    max_distance_bet_cities = max(max_distance_bet_cities, distance[current_city, 0])
    tour.append(0)

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance_bet_cities}")
else:
    print(f"No optimal solution available. Solver status: {pulp.LpStatus[status]}")