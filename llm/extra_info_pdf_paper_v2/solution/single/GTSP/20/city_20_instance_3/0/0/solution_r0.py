import math

# Define city coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76),
    19: (19, 72)
}

# Define groups
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)
    
# Generate an initial feasible tour by choosing the closest city in each group from the last city
def initial_tour(depot, groups):
    current_city = depot
    tour = [depot]
    for group in groups:
        next_city = min(group, key=lambda x: euclidean_distance(current_city, x))
        tour.append(next_city)
        current_city = next_latency_city
    tour.append(depot) # return to the depot
    return tour

# Calculate the total travel cost of the tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Generate initial tour
initial_tour = initial_tour(0, groups)
initial_cost = calculate_tour_cost(initial_tour)

# Optimize tour using a very simple iterative improvement (placeholder for more complex GLNS)
def simple_optimization(tour):
    least_cost = calculate_tour_cost(tour)
    best_tour = tour.copy()
    for i in range(1, len(tour) - 2):
        for j in range(i+2, len(tour) - 1):
            new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
            new_cost = calculate_tour_cost(new_tour)
            if new_cost < least_cost:
                best_tour = new_tour.copy()
                least_cost = new_cost
    return best_tour, least_cost

optimal_tour, optimal_cost = simple_optimization(initial_tour)

# Display the results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)