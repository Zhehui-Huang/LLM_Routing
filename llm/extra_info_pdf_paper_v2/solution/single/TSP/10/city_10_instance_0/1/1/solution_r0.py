import math
import itertools

# Define the coordinates of cities
cities = [
    (50, 42),  # Depot city
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

# Function to calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Initialize a simple tour
def initial_tour():
    return list(range(len(cities))) + [0]

# Calculate the total travel cost of the tour
def tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance(cities[tour[i-1]], cities[tour[i]])
    return total_cost

# Improve the tour using the 2-opt heuristic
def optimize_tour(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Consecutive nodes, no need to swap
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if tour_cost(new_tour) < tour_cost(tour):
                    tour = new_tour
                    improved = True
    return tour

# Main TSP-solving function
def solve_tsp():
    init_tour = initial_tour()
    optimized_tour = optimize_tour(init_tour)
    cost = tour_cost(optimized_tour)
    return optimized_tour, cost

# Execute the TSP solution
tour, total_cost = solve_tsp()

# Output the results as required
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")