import random
import math

# Coordinates of cities including the depot city
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate an initial tour randomly
def initial_tour(num_cities):
    tour = list(range(1, num_cities))
    random.shuffle(tour)
    return [0] + tour + [0]

# Calculate total travel cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Attempt to improve the tour using 2-opt swaps
def optimize_tour(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # skip consecutive cities
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if tour_cost(new_tour) < tour_cost(tour):
                    tour = new_tour
                    improvement = True
                    break
            if improvement:
                break
    return tour

# Main function to solve the TSP
def solve_tsp():
    num_cities = len(cities)
    best_tour = initial_tour(num_cities)
    best_tour = optimize_tour(best_tour)
    best_cost = tour_cost(best_tour)
    return best_tour, best_cost

# Get the solution
tour, total_cost = solve_tsp()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")