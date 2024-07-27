from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpInteger
import math

# City coordinates
city_coords = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups of cities
city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + (city_coords[city1][1] - city_coords[city2][1])**2)

# Objective function
def compute_minimize_tour():
    # Initialize the problem
    problem = LpProblem("Minimal_Tour", LpMinimize)

    # Variables
    cities = list(city_coords.keys())
    V = sum(city_groups.values(), [])
    A = [(i, j) for i in V for j in V if i != j]
    x = LpVariable.dicts("x", (V, V), cat=LpBinary)

    # Define the objective
    problem += lpSum(x[i][j] * euclidean_distance(i, j) for i in V for j in V if i != j)

    # Constraints
    for _, group in city_groups.items():
        problem += lpSum(x[i][j] for i in group for j in cities if j not in group) == 1
        problem += lpSum(x[j][i] for i in group for j in cities if j not in group) == 1

    # Subtour elimination constraints (implemented without extra variables for simplicity)
    for g1 in city_groups.values():
        for g2 in city_groups.values():
            if g1 != g2:
                problem += lpSum(x[i][j] for i in g1 for j in g2) + lpSum(x[j][i] for i in g1 for j in g2) <= len(g1) + len(g2) - 1

    # Solve the problem
    problem.solve()

    # Extract tour
    tour = [0]
    current_city = 0
    while len(tour) < len(city_groups) + 1:
        for j in V:
            if x[current_city][j].varValue == 1:
                tour.append(j)
                current_city = j
                break
    tour.append(0) # Return to depot

    return tour, problem.objective.value()

# Call the function and retrieve the solution
tour, total_cost = compute_minimize_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)