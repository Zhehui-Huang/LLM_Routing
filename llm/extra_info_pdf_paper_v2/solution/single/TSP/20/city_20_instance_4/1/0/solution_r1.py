import math
import random

# Define the cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate a random initial tour
def initial_tour():
    tour = list(cities.keys())
    random.shuffle(tour[1:])  # Shuffle only the cities excluding the depot city
    return [0] + tour[1:] + [0]  # Ensure the tour starts and ends at the depot

# Improve the tour using the 2-opt swap heuristic
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Consecutive edges are already optimal
                # Perform the swap and calculate the cost difference
                if distance(tour[i], tour[i - 1]) + distance(tour[j], tour[(j + 1) % len(tour)]) > \
                   distance(tour[i], tour[j]) + distance(tour[i - 1], tour[(j + 1) % len(tour)]):
                    tour[i:j + 1] = reversed(tour[i:j + 1])
                    improved = True
    return tour

# Calculate the total cost of the tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[(i + 1) % len(tour)]) for i in range(len(tour) - 1))

# Main function to compute the shortest TSP tour
def solve_tsp():
    best_tour = initial_tour()
    best_tour = two_opt(best_tour)
    best_cost = tour_cost(best_tour)
    
    # Repeat the process to find a potentially shorter tour
    for _ in range(100):  # Number of iterations can be tuned based on computational budget
        new_tour = initial_tour()
        new_tour = two_opt(new_tour)
        new_cost = tour_cost(new_tour)
        if new_cost < best_cost:
            best_tour, best_cost = new_tour, new_cost

    return best_tour, best_cost

# Solve the TSP and print results
best_tour, best_cost = solve_tsp()
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))