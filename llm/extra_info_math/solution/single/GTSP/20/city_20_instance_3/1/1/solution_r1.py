import pulp
import math

# Define the distance function using Euclidean formula
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define the cities coordinates, including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# Define city groups, representing the cluster each city belongs to
city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Create the linear programming problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Establish the decision variables
x = pulp.LpVariable.dicts("route", ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("position", range(1, len(coordinates)), lowBound=0, upBound=len(coordinates), cat='Continuous')

# Objective: Minimize total distance
prob += pulp.lpSum(distance(coordinates[i], coordinates[j]) * x[(i, j)] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraints for ensuring one city from each group is linked with outside its group
for group in city_groups:
    prob += pulp.lpSum(x[(i, j)] for i in group for j in range(len(coordinates)) if j not in group) == 1
    prob += pulp.lpSum(x[(j, i)] for i in group for j in range(len(coordinates)) if j not in group) == 1

# Flow conservation and subtour elimination constraints
for i in range(1, len(coordinates)):
    prob += pulp.lpSum(x[(j, i)] for j in range(len(coordinates)) if j != i) == pulp.lpSum(x[(i, j)] for j in range(len(coordinates)) if j != i) 
    
for p in range(1, len(city_groups)):
    for q in range(1, len(city_groups)):
        if p != q:
            for i in city_datasets[p]:
                for j in city_datasets[q]:
                    prob += u[i] - u[j] + len(coordinates) * x[(i, j)] <= len(coordinates) - 1

# Solve the problem
prob.solve()

# Gather results
tour = [0]
while len(tour) <= len(city_groups):
    last_city = tour[-1]
    next_cities = [j for j in range(len(coordinates)) if pulp.value(x[(last_proc, j)]) == 1]
    if next_proc:
        tour.append(next_cows[0])
    else:
        break  # Shouldn't happen in theory

# Closing the tour by coming back to the depot
tour.append(0)

# Calculate the total cost of the tour
total_cost = sum(distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)