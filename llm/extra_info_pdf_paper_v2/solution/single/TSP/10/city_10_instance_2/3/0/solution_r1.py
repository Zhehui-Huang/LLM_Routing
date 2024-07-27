import math

# Define city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Compute Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Create a distance matrix
n = len(cities)
dist_matrix = [[distance(i, j) for j in range(n)] for i in range(n)]

# Generate an initial feasible solution using a greedy approach
def initial_tour():
    unvisited = set(cities.keys()) - {0}
    tour = [0]
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current][city])
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    tour.append(0)  # return to the depot
    return tour

# Calculate the cost of a tour
def calculate_tour_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# 2-opt swap optimization
def optimize_tour(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                # Perform 2-opt swap
                if j - i == 1: continue  # Skip adjacent edges
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if calculate_tour_cost(new_tour) < calculate_tour_cost(tour):
                    tour = new_tour
                    improvement = True
                    break
            if improvement:
                break
    return tour

# Start the TSP solver
initial_solution = initial_tour()
optimized_solution = optimize_tour(initial_solution)
total_cost = calculate_tour_output_cost(optimized_solution)

# Output the total travel cost and tour path
print(f"Tour: {optimized_solution}")
print(f"Total travel cost: {total_cost}")