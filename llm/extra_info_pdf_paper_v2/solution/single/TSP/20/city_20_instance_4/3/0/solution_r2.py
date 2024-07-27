import math

# Define the cities (indices and coordinates)
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a distance matrix
n = len(cities)
dist_matrix = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# A simple greedy solution to generate an initial feasible solution
def greedy_solution(start=0):
    unvisited = list(range(1, n))
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start) # Add the return to the depot
    return tour

# Calculate the total cost of a tour
def calculate_total_distance(tour):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Attempts a 2-opt swap to find a better tour
def two_opt(tour):
    best_distance = calculate_total_distance(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]
                new_distance = calculate_total_distance(new_tour)
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    improved = True
        if not improved:
            break
    return tour, best_distance

# Start the generation of the initial tour
initial_tour = greedy_solution()
optimized_tour, total_cost = two_opt(initial_tour.copy())

# Print results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost:.2f}")