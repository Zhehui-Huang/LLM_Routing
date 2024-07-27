import pulp
import math

# City positions
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

n = len(cities)

# Calculate Euclidean distance between cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Setting up the TSP Model: We'll use LpMinimize as we want to minimize the travel cost
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x[(i,j)] = 1 if travel from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function
model += pulp.lpSum(x[(i, j)] * distance(i, j) for i in cities for j in cities if i != j), "Total_Distance"

# Constraints
for i in cities:
    model += pulp.lpSum(x[(i, j)] for j in cities if i != j) == 1, f"Leave_city_{i}"
    model += pulp.lpSum(x[(j, i)] for j in cities if i != j) == 1, f"Enter_city_{i}"

# Subtour elimination
for S in range(2, n):
    for subset in itertools.combinations([i for i in cities if i != 0], S):
        model += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
model.solve()

# Extracting the solution
tour = []
current_city = 0
while True:
    next_cities = [j for j in cities if j != current_city and x[(current_city, j)].varValue == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

tour = [0] + tour + [0]  # Return to the starting city
total_cost = sum(x[(tour[i], tour[i+1])].varValue * distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")