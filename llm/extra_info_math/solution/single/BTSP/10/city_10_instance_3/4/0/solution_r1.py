from pulp import *
import math

# Define the cities with their coordinates
cities = {
    0: (84, 67), # depot
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

# Function to compute Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)

# Dictionary to store distances between every pair of cities
distances = {(i, j): distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Creating the problem variable to contain the problem data
model = LpProblem("Minimize_max_distance_in_TSP", LpMinimize)

# Decision variables: x_ij where i, j are city indices, and i != j
x = LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Continuous variable to capture the maximum distance between consecutive cities
max_distance = LpVariable("max_distance", lowBound=0, cat='Continuous')
model += max_distance  # Minimize the maximum distance

# Constraints to ensure each city is entered and left exactly once
for k in cities:
    model += lpSum(x[(i, k)] for i in cities if i != k) == 1  # enter city k
    model += lpSum(x[(k, j)] for j in cities if k != j) == 1  # leave city k

# Link max_distance with distances
for i in cities:
    for j in cities:
        if i != j:
            model += x[(i, j)] * distances[(i, j)] <= max_distance

# Solve model
model.solve()

# Check if a valid solution exists
if LpStatus[model.status] == 'Optimal':
    tour = [0]
    current_city = 0
    next_city = None

    # Determine the tour path
    while True:
        for j in cities:
            if j != current_city and x[(current_city, j)].varValue == 1:
                next_city = j
                tour.append(next_city)
                current_city = j
                break
        if next_city == 0:
            break

    # Calculate total cost and max distance
    total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
    max_dist = max(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

    # Output results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_dist}")
else:
    print("No optimal solution found.")