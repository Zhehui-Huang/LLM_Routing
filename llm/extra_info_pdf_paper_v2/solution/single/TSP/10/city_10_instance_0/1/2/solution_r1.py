import math

# City coordinates
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def nearest_neighbor_tour(start, cities):
    """Generate an initial tour using the nearest neighbor heuristic."""
    tour = [start]
    unvisited = set(range(len(cities)))
    unvisited.remove(start)

    current_city = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(start)  # Return to the depot
    return tour

def calculate_total_distance(tour, cities):
    """Calculate total distance for a given tour."""
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

def perform_two_opt(tour, cities):
    """Improves an existing tour using the 2-opt algorithm."""
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour)):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if calculate_total_distance(new_tour, cities) < calculate_total_distance(best_tour, cities):
                    best_tour = new_tour[:]
                    improved = True
        tour = best_tour[:]
    return best_tour

# Generate initial tour
initial_tour = nearest_neighbor_tour(0, cities)

# Improve the tour with 2-opt
optimized_tour = perform_two_opt(initial_tour, cities)
optimized_distance = calculate_total_distance(optimized_tour, cities)

# Printing the outputs
print('Tour:', optimized_tour)
print('Total travel cost:', optimized_distance)