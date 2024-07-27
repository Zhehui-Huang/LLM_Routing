import math

# Provided cities coordinates
coordinates = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91),
               (70, 14), (97, 44), (17, 69), (95, 89)]

# Calculate Euclidean distance between two cities
def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

# Initializing distance matrix
n = len(coordinates)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Generate initial feasible tour (simple nearest neighbor algorithm)
def initial_solution(start=0):
    tour = [start]
    available_cities = set(range(n))
    available_cities.remove(start)
    current_city = start

    while available_cities:
        next_city = min(available_cities, key=lambda x: distance_matrix[current_city][x])
        tour.append(next_city)
        available_cities.remove(next_city)
        current_city = next_city
    
    tour.append(start)  # return to depot
    return tour

# Calculate the cost of the tour
def calculate_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Lin-Kernighan inspired algorithm to improve the given tour
def two_opt_swap(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Consecutive nodes
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_cost(new_tour) < calculate_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    
    return tour

# Main processing to solve the TSP
initial_tour = initial_solution()
improved_tour = two_opt_swap(initial_tour)
tour_cost = calculate_cost(improved_tour)

# Output results
print("Tour:", improved_tour)
print("Total travel cost:", tour_cost)