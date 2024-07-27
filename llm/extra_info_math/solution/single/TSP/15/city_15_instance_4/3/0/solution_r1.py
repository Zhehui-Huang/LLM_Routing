import pulp
import math
import itertools

# Given cities coordinates
coords = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate Euclidean distance between cities
def distance(city1, city2):
    return math.sqrt((coords[city1][0] - coords[city2][0])**2 + (coords[city1][1] - coords[city2][1])**2)

# List of all cities
n = len(coords)
cities = list(coords.keys())

# Create the TSP problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j), "Total Distance"

# Constraints
for i in cities:
    prob += pulp.lpSum(x[i, j] for j in cities if i != j) == 1, f"Leave_{i}"
    prob += pulp.lpSum(x[j, i] for j in cities if i != j) == 1, f"Enter_{i}"

# Subtour elimination using u (artificial variables)
u = pulp.LpVariable.dicts("u", cities, lowBound=0, upBound=n-1, cat='Continuous')
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + n*x[i, j] <= n-1

# Solving the problem
prob.solve()

# Output check:
if pulp.LpStatus[prob.status] == 'Optimal':
    tours = []
    for i in cities:
        for j in cities:
            if i != j and pulp.value(x[i, j]) == 1:
                tours.append((i, j))
    
    # Form the output tour starting from depot
    current_city = 0
    tour = [current_city]
    while len(tour) < n:
        for i, j in tours:
            if i == current_city:
                current_city = j
                tour.append(current_inst)
                break
    tour.append(0)  # return to depot

    # Calculate the total cost of the found tour
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found. Status:", pulp.LpStatus[prob.status])