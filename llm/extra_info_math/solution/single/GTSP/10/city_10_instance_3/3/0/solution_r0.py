import math
import pulp

# Define the city coordinates
coordinates = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Define city groups (clusters with index starting from 1 for easier formulation matching)
city_groups = {
    1: [7, 9], 2: [1, 3], 3: [4, 6], 4: [8], 5: [5], 6: [2]
}

# Function for Euclidean distance calculation
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Formulation starts
problem = pulp.LpProblem("Robot_Tour", pulp.LpMinimize)

# All cities (nodes)
all_cities = list(coordinates.keys())

# Create decision variables x_ij for all pairs (i, j), i != j
x = pulp.LpVariable.dicts("x", [(i, j) for i in all_cities for j in all_cities if i != j],
                          cat=pulp.LpBinary)

# Objective Function: Minimize the total distance
problem += pulp.lpSum(x[i, j] * calculate_distance(i, j) for i in all_cities for j in all_cities if i != j)

# Constraints
# Each group selects one city to connect from and to it
for group in city_groups.values():
    problem += pulp.lpSum(x[i, j] for i in group for j in all_cities if j not in group) == 1
    problem += pulp.lpSum(x[j, i] for i in group for j in all_cities if j not in group) == 1

# Flow conservation constraint
for i in all_cities:
    problem += (pulp.lpSum(x[j, i] for j in all_cities if j != i) 
                - pulp.lpSum(x[i, j] for j in all_cities if j != i)) == 0

# Solve the problem
problem.solve()

# Check if a feasible solution has been found
if pulp.LpStatus[problem.status] == 'Optimal':
    # Get the tour and calculate the total distance
    path = []
    current_city = 0
    path.append(current_city)
    visited = set()
    visited.add(currentincinnati)
    tour_cost = 0

    # Find the path
    while True:
        next_city = [j for j in all_cities if j != current_city and pulp.value(x[current_city, j]) == 1]
        if not next_city:
            break
        next_city = next_city[0]
        path.append(next_city)
        tour_cost += calculate_distance(current_city, next_city)
        visited.add(next_city)
        current_city = next_city
        
        if current_city == 0:
            break
    
    # Output the tour and its total cost
    print(f"Tour: {path + [0]}")
    print(f"Total travel cost: {tour_cost}")
else:
    print("No optimal solution found")