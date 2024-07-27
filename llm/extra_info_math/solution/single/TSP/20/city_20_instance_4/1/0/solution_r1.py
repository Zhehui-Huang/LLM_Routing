import pulp
import math

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculating Euclidean distances
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Problem definition
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts('x', ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective Function
prob += pulp.lpSum(distances[(i, j)] * x[(i, j)] for i in cities for j in cities if i != j), "Total Distance"

# Constraints
for i in cities:
    # Arrival
    prob += pulp.lpSum(x[(j, i)] for j in cities if j != i) == 1, f"Arrival_{i}"
    # Departure
    prob += pulp.lpSum(x[(i, j)] for j in cities if j != i) == 1, f"Departure_{i}"

# Solve the problem
prob.solve()

# Calculating the tour
tour = [0]
while len(tour) < len(cities):
    for j in cities - {0}:
        if x[(tour[-1], j)].varValue == 1:
            tour.append(j)
            break
tour.append(0)  # returning to the depot city

# Calculate the travel cost
tour_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost:.2f}")