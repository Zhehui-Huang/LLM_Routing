import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Coordinates of the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Compute the distance matrix
distance_matrix = {}
for i in cities:
    for j in cities:
        if i not in distance_matrix:
            distance_matrix[i] = {}
        distance_matrix[i][j] = euclidean_distance(*(cities[i] + cities[j]))

def total_distance(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Generate an initial solution (greedy approach from the depot)
def initial_solution(depot):
    unvisited = set(cities.keys())
    unvisited.remove(depot)
    tour = [depot]
    current = depot
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(depot)
    return tour

# Perform 2-opt to improve the solution
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Do not need to swap adjacent
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_distance(new_tour) < total_distance(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

# Initialize the solution and improve it using 2-opt
initial_tour = initial_solution(0)
improved_tour = two_opt(initial_tour)
tour_cost = total_distance(improved_tour)

# Print the result
print("Tour:", improved_tour)
print("Total travel cost:", tour_cost)