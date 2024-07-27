import math

# Coordinates of each city including the depot
cities = [
    (29, 51),  # Depot City 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# Calculate Euclidean distance between two cities
def distance(i, j):
    x1, y1 = cities[i]
    x2, y2 = cities[j]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate the total travel cost of a tour
def tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance(tour[i - 1], tour[i])
    return cost

# Permutation-based initial solution (naive way to generate initial tour)
def initial_tour():
    # Include all cities except the depot (0)
    tour = list(range(1, len(cibles)))
    return [0] + tour + [0]  # Tour starts and ends at the depot

# Improve the tour using the 2-opt heuristic
def two_opt(tour):
    best_cost = tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i:j + 1] = reversed(new_tour[i:j + 1])
                new_cost = tour_cost(new_tour)
                if new_cost < best_cost:
                    tour, best_cost = new_tour[:], new_cost
                    improved = True
    return tour, best_cost

# Main function to run the TSP solution
def solve_tsp():
    initial = initial_tour()
    improved_tour, improved_cost = two_opt(initial)
    return improved_tour, improved_cost

# Execute and get solution
best_tour, total_cost = solve_tsp()

# Output resulting tour and cost
print("Tour:", best_tour)
print("Total travel cost:", total_cost)