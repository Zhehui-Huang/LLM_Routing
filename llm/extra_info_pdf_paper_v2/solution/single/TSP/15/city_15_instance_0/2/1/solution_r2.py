import math

# City coordinates (city_index: (x, y))
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59), 
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def find_optimal_tour():
    # Initial tour (start at depot, visit each city once, return to depot)
    best_tour = list(cities.keys())
    best_cost = total_cost(best_tour + [0])  # Close the loop by returning to depot

    # Iterative improvement: 2-opt swaps
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_tour) - 2):
            for j in range(i + 1, len(best_tour)):
                if j - i == 1: continue  # This would be a trivial swap of adjacent elements
                new_tour = best_tour[:]
                new_tour[i:j+1] = reversed(new_tour[i:j+1])
                new_cost = total_cost(new_tqour + [0])
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    improved = True

    return best_tour + [0], best_cost  # Ensure the tour is closed by returning to the depot

# Calculate the optimal tour and cost using the simplified heuristic
optimal_tour, optimal_cost = find_optimal_tour()

# Print the optimal tour and its total travel cost
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")