import itertools
import pulp
import math

# Helper function for Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of the cities indexed by their number
coords = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculating distances between each pair of cities.
distances = {(i, j): distance(coords[i], coords[j]) for i in coords for j in coords if i != j}

# Initialize the problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables x_ij
x = pulp.LpVariable.dicts("x", [(i, j) for i in coords for j in coords if i != j], cat="Binary")

# Additional variable for the maximum distance
y = pulp.LpVariable("y", lowBound=0, cat="Continuous")

# Objective function to minimize the maximum distance
prob += y

# Constraints that ensure each city except the depot is entered and left once
for j in coords:
    prob += pulp.lpSum(x[(i, j)] for i in coords if (i, j) in x) == 1, f"Enter_{j}"
    prob += pulp.lpSum(x[(j, i)] for i in coords if (j, i) in x) == 1, f"Leave_{j}"

# Link the max distance y with city distances
for i, j in x:
    prob += distances[i, j] * x[(i, j)] <= y

# Subtour elimination constraints (SEC) to eliminate possible subtours
for s in range(2, len(coords)):
    for subset in itertools.combinations(coords.keys(), s):
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j and (i, j) in x) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the solution if optimal
if pulp.LpStatus[prob.status] == "Optimal":
    edges = [(i, j) for i, j in x if pulp.value(x[(i, j)]) == 1]
    if edges:
        seq = [0]
        while len(seq) - 1 != len(coords):
            for e in edges:
                if e[0] == seq[-1]:
                    seq.append(e[1])
                    break
        total_distance = sum(distances[seq[i - 1], seq[i]] for i in range(1, len(seq)))
        max_segment = max(distances[seq[i - 1], seq[i]] for i in range(1, len(seq)))
        print(f"Tour: {seq}")
        print(f"Total travel cost: {total_distance}")
        print(f"Maximum distance between consecutive cities: {max_segment}")
    else:
        print("No valid tour found.")
else:
    print("Failed to find a solution.")