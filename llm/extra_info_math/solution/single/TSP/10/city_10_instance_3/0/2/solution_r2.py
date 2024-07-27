import pulp
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def solve_tsp(cities):
    n = len(cities)
    dist = {(i, j): euclidean_trueance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

    # Creating a problem instance
    prob = pulp.LpProblem("TSP", pulp.LpMinimize)

    # Decision variables
    x = pulp.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n) if i != j), lowBound=0, upBound=1, cat=pulp.LpBinary)

    # Objective function
    prob += pulp.lpSum(dist[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

    # Constraints
    for i in range(n):
        prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave i exactly once
        prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter i exactly once

    # Subtour elimination constraints
    for s in range(2, n):
        subsets = [tuple(c) for c in itertools.combinations(range(1, n), s)]  # exclude the depot
        for subset in subsets:
            prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

    # Solve the problem
    prob.solve()

    tour = []
    current_location = 0
    while len(tour) < n:
        tour.append(current_location)
        next_moves = [j for j in range(n) if j != current_location and pulp.value(x[current_location, j]) == 1]
        if not next_moves:
            break
        current_location = next_moves[0]
    tour.append(0)  # Return to the depot

    total_cost = sum(dist[tour[i], tour[i+1]] for i in range(len(tour)-1))

    return tour, total_cost

# City coordinates
cities = [
    (84, 67),  # City 0 - Depot
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

if __name__ == "__main__":
    tour, total_cost = solve_tsp(cities)
    print("Tour:", tour)
    print("Total travel cost:", total_cost)