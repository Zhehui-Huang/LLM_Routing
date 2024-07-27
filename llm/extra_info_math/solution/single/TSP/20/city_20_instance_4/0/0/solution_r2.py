import pulp
import math

# City coordinates
coordinates = [
    (26, 60), # Depot city 0
    (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

n = len(coordinates)

# Euclidean distance calculator
def distance(i, j):
    x1, y1 = coordinates[i]
    x2, y2 = coordinates[j]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create LP problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
problem += pulp.lpSum(x[(i, j)] * distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # leaving city i
    problem += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # entering city i

# Solve the problem
problem.solve()

# Extracting solution
if pulp.value(problem.objective) is not None: 
    tour = [0]
    next_city = 0
    for _ in range(n-1):
        for j in range(1, n):
            if x[(next_city, j)].value() == 1:
                tour.append(j)
                next_city = j
                break

    tour.append(0)  # return to the depot city

    # Total travel cost calculation
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    # Output the results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")

else:
    print("No solution found.")