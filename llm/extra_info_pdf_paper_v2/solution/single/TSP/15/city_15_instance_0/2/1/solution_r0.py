import math
from itertools import permutations

# City coordinates (city_index: (x, y))
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59), 
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def total_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generate initial tour, start and return to the depot city
initial_tour = list(cities.keys())
initial_tour.append(0)  # Close the loop returning to the depot city

# Compute cost of the naive initial tour
initial_cost = total_catalog(initial_tour)

def find_optimal_tour():
    current_tour = initial_tour[:]
    best_cost = initial_cost
    improved = True

    # Iteratively try to find improvements
    while improved:
        improved = False
        for i in range(1, len(current_tour) - 2):
            for j in range(i + 1, len(current_tour) - 1):
                if j - i == 1: continue  # Skip adjacent edges as no change
                new_tour = current_tour[:]
                new_tour[i:j+1] = reversed(new_tour[i:j+1])  # Reverse segment
                new_cost = total_cost(new_tour)
                if new_cost < best_cost:
                    current_tour = new_tour
                    best_cost = new_cost
                    improved = True
                    break
            if improved:
                break

    return current_tour, best_cost

# Calculate optimal tour using the heuristic
optimal_tour, optimal_cost = find_optimal_tour()

# Output format
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")