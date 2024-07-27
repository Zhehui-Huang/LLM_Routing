import math

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def construct_initial_tour(cities):
    """Construct an initial tour using nearest neighbor approach."""
    n = len(cities)  # Total number of cities including depot
    unvisited = set(range(1, n))  # Set of unvisited cities, excluding the depot city
    tour = [0]  # Start tour at the depot city
    current = 0  # Start from depot

    while unvisited:
        # Select the nearest unvisited city
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(0)  # Return to the depot
    return tour

def two_opt(tour, cities):
    """Optimize the tour using the 2-opt algorithm."""
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                # Check if swapping edges reduces the tour length
                if (euclidean_distance(cities[tour[i]], cities[tour[j]]) +
                    euclidean_distance(cities[tour[i - 1]], cities[tour[j + 1]]) <
                    euclidean_distance(cities[tour[i]], cities[tour[i - 1]]) +
                    euclidean_distance(cities[tour[j]], cities[tour[j + 1]])):
                    tour[i:j + 1] = reversed(tour[i:j + 1])  # Make the swap
                    improved = True
    return tour

def calculate_total_cost(tour, cities):
    """Calculate the total travel cost of a tour."""
    total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    return total_cost

def main():
    cities = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
        (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
        (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
        (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]
    
    initial_tour = construct_initial_tour(cities)
    optimized_tour = two_opt(initial_tour, cities)
    total_cost = calculate_total_cost(optimized_tour, cities)
    
    print(f'Tour: {optimized_tith "]*timestamp'}
    print(f'Total travel cost: {total_cost:.2f}')

main()