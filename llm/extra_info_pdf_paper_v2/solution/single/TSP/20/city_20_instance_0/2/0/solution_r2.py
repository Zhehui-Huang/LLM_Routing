import math

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities given as (x, y) coordinates."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def construct_initial_tour(cities):
    """Create an initial tour using the nearest neighbor heuristic."""
    unvisited = set(range(1, len(cities)))  # All cities except the depot (indexed by 0)
    tour = [0]  # Start at the depot
    
    # Iterate until no unvisited cities remain
    current_city = 0
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(0)  # Return to depot
    return tour

def two_opt(tour, cities):
    """ Improve the tour using the 2-opt swap until no improvement is made."""
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 1):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Consecutive nodes; no need to consider swapping
                new_distance = (euclidean_distance(cities[tour[i - 1]], cities[tour[j]]) + 
                                euclidean_distance(cities[tour[i]], cities[tour[j + 1 % len(tour)]])
                               )
                old_distance = (euclidean_distance(cities[tour[i - 1]], cities[tour[i]]) + 
                                euclidean_distance(cities[tour[j]], cities[tour[j + 1 % len(tour)]])
                               )
                if new_distance < old_distance:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

def calculate_total_cost(tour, cities):
    """Calculate the total distance of the tour."""
    total_distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    return total_distance

# Define the cities based on the given coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Generate the initial and optimized tours
initial_tour = construct_initial_tour(cities)
optimized_tour = two_opt(initial_tour, cities)
total_cost = calculate_total_cost(optimized_tour, cities)

# Print the results
print(f'Tour: {optimized_tour}')
print(f'Total travel cost: {total_cost:.2f}')