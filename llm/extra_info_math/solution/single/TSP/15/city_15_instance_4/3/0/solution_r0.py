import pulp
import math

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

n = len(coords)
cities = range(n)

# Create the TSP problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (cities, cities), cat='Binary', lowBound=0, upBound=1)

# Objective function
prob += pulp.lpSum(x[i][j] * distance(i, j) for i in cities for j in cities if i != j)

# Constraints
for i in cities:
    prob += pulp.lpSum(x[i][j] for j in cities if i != j) == 1
    prob += pulp.lpSum(x[j][i] for j in cities if i != j) == 1

# Subtour elimination constraints
for l in range(2, n):
    for S in itertools.combinations([i for i in cities if i != 0], l):
        prob += pulp.lpSum(x[i][j] + x[j][i] for i in S for j in S if i != j) <= len(S) - 1

# Solving the problem
prob_status = prob.solve()

# Checking if the optimal solution is found
if prob_status == pulp.LpStatusOptimal:
    tour = []
    i = 0
    while len(tour) < n:
        for j in cities:
            if pulp.value(x[i][j]) == 1:
                tour.append(i)
                i = j
                break
    # Closing the tour
    tour.append(0)
    
    # Calculating the total travel cost
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
else:
    print("No optimal solution found.")