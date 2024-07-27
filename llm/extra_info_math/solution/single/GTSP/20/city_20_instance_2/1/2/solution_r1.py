from pulp import *
import math

# We'll use function to solve the problem
def solve_tsp_with_groups():
    # Define the cities and their coordinates
    cities = {
        0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
        5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
        10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
        15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
    }

    # Group information
    groups = [
        [7, 10, 11, 12],
        [3, 8, 13, 16],
        [2, 4, 15, 18],
        [1, 9, 14, 19],
        [5, 6, 17]
    ]

    # Function to calculate Euclidean distance
    def distance(city1, city2):
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Create the linear programming model to minimize distances
    model = LpProblem("TSP", LpMinimize)

    # Create decision variables
    x = LpVariable.dicts("x", [(i, j) for i in cities.keys() for j in cities.keys() if i != j], cat='Binary')

    # Objective function
    model += lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j)

    # Each group must connect exactly once to another group
    for group in groups:
        model += lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
        model += lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

    # Flow conservation
    for i in cities:
        model += lpSum(x[j, i] for j in cities if j != i) == lpSum(x[i, k] for k in cities if k != i)

    # Solve the model
    model.solve()

    # Construct the tour from the variables
    edges = [(i, j) for i in cities for j in cities if i != j and x[i, j].varValue > 0.9]
    tour = [0]
    next_city = 0
    
    # Assembling the tour
    while len(edges) > 0:
        for i, (start, end) in enumerate(edges):
            if start == next_city:
                next_city = end
                tour.append(next_city)
                edges.pop(i)
                break

    tour.append(0)  # Return to the starting point

    # Calculate the total cost of the tour
    total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    return tour, total_cost

# Run the solver
tour, total_cost = solve_tsp_with_groups()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")