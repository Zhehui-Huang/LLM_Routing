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

# Distance calculation function
def distance(i, j):
    x1, y1 = cities[i]
    x2, y2 = cities[j]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Calculate the total cost of the tour
def calc_tour_cost(tour):
    total_cost = 0
    for k in range(1, len(tour)):
        total_cost += distance(tour[k-1], tour[k])
    return total_cost

# Perform simple 2-opt algorithm to find a local minimum
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Skip adjacent edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calc_tour_cost(new_tour) < calc_tour_cost(best):
                    best = new_tour
                    improved = True
    return best

# Finding the best tour via a 2-opt heuristic
def find_best_tour():
    # Generate initial tour
    initial_tour = list(range(len(cities)))  # Tour starts with 0 and visits all cities
    initial_tour.append(0)  # Come back to the depot

    # Apply 2-opt heuristic
    optimized_tour = two_opt(initial_tour)
    optimized_cost = calc_tour_cost(optimized_tour)

    return optimized_tour, optimized_cost

# Running the TSP solver
optimal_tour, tour_cost = find_best_tour()

print("Tour:", optimal_tour)
print("Total travel cost:", tour_cost)