import math

def euclidean_distance(c1, c2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def find_shortest_tour(cities):
    """ Greedy approach to find a near-optimal route based on nearest neighbor heuristic. """
    n = len(cities)
    unvisited = set(range(1, n))  # Initialize unvisited cities, excluding the depot (city 0)
    tour = [0]  # Starting at depot city
    current_city = 0
    
    # Continuously add the nearest unvisited city to the tour
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    # Return to the depot after visiting all cities
    tour.append(0)
    return tour

def calculate_tour_cost(tour, cities):
    """ Calculate the total travel cost of the tour based on Euclidean distances between consecutive cities. """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Define the coordinates for each city including the depot
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Generate the tour and calculate the total cost
tour = find_shortest_tour(cities)
total_cost = calculate_tour_cost(tour, cities)

# Properly format the output
print("Tour:", tour)
print("Total travel cost:", total_cost)