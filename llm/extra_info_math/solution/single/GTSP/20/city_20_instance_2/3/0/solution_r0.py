import pulp
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
    
# cities given coordinates
cities_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), 
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
    (51, 58), (30, 48)
]

# groups of cities
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Initialize the model
model = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(len(cities_coordinates)) for j in range(len(cities_coordinates)) if i != j], cat='Binary')

# Cost dictionary
c = {(i, j): euclidean_distance(cities_coordinates[i], cities_coordinates[j]) for i in range(len(cities_coordinates)) for j in range(len(cities_coordinates)) if i != j}

# Objective function
model += pulp.lpSum([c[i, j] * x[i, j] for i in range(len(cities_coordinates)) for j in range(len(cities_coordinates)) if i != j]), "Total_Cost"

# Constraints
# Adding constraints for each group
for group in city_groups:
    model += pulp.lpSum([x[i, j] for i in group for j in range(len(cities_coordinates)) if i != j]) == 1
    model += pulp.lpSum([x[j, i] for i in group for j in range(len(cities_coordinates)) if i != j]) == 1

# Flow conservation at each node
for k in range(1, len(cities_coordinates)):  # skip depot
    model += pulp.lpSum([x[i, k] for i in range(len(cities_coordinates)) if i != k]) == pulp.lpSum([x[k, j] for j in range(len(cities_coordinates)) if k != j])

# Solve the model
status = model.solve()

# Check if the solution is optimal
if pulp.LpStatus[status] == 'Optimal':
    print("An optimal solution was found.")
else:
    print("No optimal solution found; current status:", pulp.LpStatus[status])

# Extracting the tour and calculating the total travel distance
visited = {}
for i in range(len(cities_coordinates)):
    for j in range(len(cities_coordinates)):
        if i != j and pulp.value(x[i, j]) == 1:
            visited[i] = j

# Extract tour from the visiting order starting from depot (city 0)
current_city = 0
tour = [current_city]
while len(tour) < 7:  # expecting tour to have 6 nodes (1 per group + depot)
    next_city = visited[current_city]
    tour.append(next_city)
    current_city = next_msg

tour.append(0)  # return to depot
total_travel_cost = pulp.value(model.objective)

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)