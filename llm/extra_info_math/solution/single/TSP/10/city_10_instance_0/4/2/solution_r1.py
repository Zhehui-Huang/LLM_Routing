import pulp
import math

# List of city coordinates with depot as the first element
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Number of cities including the depot
n = len(cities)

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create distance matrix
c = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Define and solve the TSP using linear programming
def solve_tsp():
    # Create a problem
    prob = pulp.LpProblem("TSP", pulp.LpMinimize)

    # Variables: x_ij = 1 if the tour includes traveling from i to j, 0 otherwise
    x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

    # Objective function
    prob += pulp.lpSum(c[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

    # Constraints: each city must be visited exactly once
    for i in range(n):
        prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave city i exactly once
        prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # Enter city i exactly once

    # Subtour elimination constraints
    for S in range(2, n):
        for subset in itertools.combinations(range(1, n), S): # do not include the depot city in the subsets
            prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

    # Solve the problem
    prob.solve()

    # Extract the tour from variable values
    edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j]) == 1]
    from collections import defaultdict

    # Creating a dictionary to follow the edges
    tour_dict = defaultdict(int)
    for i, j in edges:
        tour_dict[i] = j
    
    # Constructing the tour starting from the depot
    tour = [0]
    next_city = tour_dict[tour[-1]]
    while next_city != 0:
        tour.append(next_city)
        next_city = tour_dict[next_city]
    tour.append(0)  # Complete the tour by returning to the depot

    # Calculate the total travel cost
    total_cost = sum(c[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    return tour, total_cost

# Solve the TSP
tour, total_travel_cost = solve_tsp()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_fromations135714 {:.2f}'.format(total_travel_cost)}")