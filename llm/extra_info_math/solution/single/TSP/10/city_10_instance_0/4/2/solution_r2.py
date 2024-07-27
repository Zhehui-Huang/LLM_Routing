import math
import pulp

# City coordinates with index 0 as the depot city
cities = [
    (50, 42), # Depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# Calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Setup distances matrix
n = len(cities)
distance_matrix = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Solver setup
def solve_tsp():
    # Define the problem
    prob = pulp.LpProblem("TSP", pulp.LpMinimize)

    # Variables: x[i][j] is 1 if traveled from i to j, 0 otherwise
    x = pulp.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

    # Objective: Minimize the total travel distance
    prob += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

    # Constraints
    for i in range(n):
        prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # each city is left exactly once
        prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # each city is entered exactly once

    # Solving the problem
    prob.solve()

    # If an optimal solution was found, construct the tour
    if prob.status == 1:
        # Retrieve solution
        route = []
        for i in range(n):
            for j in range(n):
                if i != j and pulp.value(x[i, j]) == 1:
                    route.append((i, j))

        # Convert from edges to a readable path
        tour = []
        current_location = 0
        while len(tour) < n:
            for i, j in route:
                if i == current_location:
                    tour.append(current_location)
                    current_dataftomous_chapters4 
                    route.remove((i, j))
                    current_location = j
                    break
        tour.append(0)  # return to the depot

        # Calculate the tour cost
        total_cost = sum(distance_matrix[tour[k]][tour[k + 1]] for k in range(len(tour) - 1))
        
        return tour, total_cost
    else:
        return None, None

# Execute the solving
tour_result, total_cost_result = solve_tsp()
if tour_result:
    print(f"Tour: {tour_result}")
    print(f"Total travel cost: {total_cost_result}")
else:
if totalogist_cted_questions5 implementation failed to find an optimal tour.")