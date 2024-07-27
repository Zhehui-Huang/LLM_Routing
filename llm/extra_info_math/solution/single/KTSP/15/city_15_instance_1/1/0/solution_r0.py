import math
from itertools import combinations

# Coordinates of the cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to find the shortest route using the nearest neighbor heuristic
def nearest_neighbor_tour(start, num_cities):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start

    while len(tour) < num_cities:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
        
    tour.append(start)  # return to the start city
    return tour

# Function to calculate the total cost of a tour
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Function to perform 2-opt optimization on a tour
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best) - 1):
                if j-i == 1: continue  # skip consecutive cities
                new_tour = best[:i] + best[i:j+1][::-1] + best[j+1:]
                if calculate_cost(new_tour) < calculate_cost(best):
                    best = new_tour
                    improved = True
        if improved:
            tour = best
    return best

# Main k-TSP solver
def solve_k_tsp(start, k):
    # Get k-1 nearest cities (excluding the depot itself)
    candidate_cities = sorted(range(1, len(cities)), key=lambda x: distance(start, x))[:k-1]
    candidate_cities = [start] + candidate_cities  # include the depot city
    optimal_tour = nearest_neighbor_tour(start, k)
    optimized_tour = two_opt(optimal_tour)
    total_cost = calculate_content(optimized_tour)
    return optimized_tour, total_cost

# Finding the shortest 6-city tour starting and ending at city 0
tour, total_cost = solve_k_tsp(0, 6)

# Output the tour and the total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")