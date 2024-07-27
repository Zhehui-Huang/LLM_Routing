import itertools
import math

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
    9: (66, 62)
}

city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Compute Euclidean distance between two points
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute all distances between cities
distances = {}
for c1 in cities:
    for c2 in cities:
        if c1 != c2:
            distances[(c1, c2)] = distance(cities[c1], cities[c2])

# Function to compute the cost of a given tour
def tour_cost(tour):
    return sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Find the minimum distance representative for each group of cities to create a subproblem
min_distances = {}
chosen_cities = []

# Including the start city
chosen_cities.append(0)
subproblem_distances = {}
subproblem_distances[0] = {}

# Find the min distance city in each group
for group_index, group in enumerate(city_groups):
    min_dist = float('inf')
    selected_city = None
    
    for city in group:
        dist_to_0 = distances[(0, city)]
        if dist_to_0 < min_dist:
            min_dist = dist_to_0
            selected_city = city
    
    chosen_cities.append(selected_city)
    subproblem_distances[0][selected_city] = distances[(0, selected_city)]
    if selected_city not in subproblem_distances:
        subproblem_distances[selected_city] = {}
    subproblem_distances[selected_city][0] = distances[(selected_city, 0)]

# Calculate distances for the minimal spanning cities
for i in range(1, len(chosen_cities)):
    ci = chosen_cities[i]
    for j in range(i + 1, len(chosen_cities)):
        cj = chosen_cities[j]
        dist = distances[(ci, cj)]
        subproblem_distances[ci][cj] = dist
        subproblem_distances[cj][ci] = dist

# We now solve the TSP for these selected cities
best_tour = None
best_cost = float('inf')

# We perform a permutation check on selected cities except the depot
for perm in itertools.permutations(chosen_cities[1:]):
    tour = [0] + list(perm) + [0]
    cost = tour_cost(tour)
    if cost < best_cost:
        best_cost = cost
        best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))