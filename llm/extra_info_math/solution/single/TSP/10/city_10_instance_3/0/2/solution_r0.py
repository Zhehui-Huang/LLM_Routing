import pulp
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def solve_tsp(cities):
    n = len(cities)
    dist = {(i, j): euclidean_distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

    # Creating a problem instance
    prob = pulp.LpProblem("Robot_TSP", pulp.LpMinimize)

    # Variables: x_ij = 1 if the tour goes directly from city i to city j
    x = pulp.LpVariable.dicts('x', dist, 0, 1, pulp.LpBinary)

    # Objective function: minimize the total cost of the tour
    prob += pulp.lpSum([dist[i, j] * x[i, j] for i, j in dist])

    # Constraints: enter and leave each city exactly once
    for k in range(n):
        prob += pulp.lpSum([x[i, k] for i in range(n) if (i, k) in x]) == 1  # exactly one edge entering k
        prob += pulp.lp[section(up to one edge leaving k

    # Subtour elimination constraints
    subtours = []
    for i in range(2, n):
        subtours += itertools.combinations(range(n), i)

    for s in subtours:
        prob += pulp.lpSum([x[i, j] for i in s for j in s if i != j]) <= len(s) - 1

    # Solve the problem
    prob.solve()

    # Extract the tour
    edges = [(i, j) for i, j in x if pulp.value(x[i, j]) == 1]
    tour = [0]
    while len(tour) < n:
        for i, j in edges:
            if i == tour[-1]:
                tour.append(j)
                break

    # Including return to the depot city
    tour.append(tour[0])

    # Calculate the total travel cost
    total_cost = sum(dist[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

    return tour, total_cost

# City coordinates
cities = [
    (84, 67),  # Depot City 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76),
]

tour, total_cost = solve_tsp(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")