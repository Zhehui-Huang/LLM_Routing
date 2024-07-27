import math

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to find the shortest TSP route using a nearest neighbor heuristic
def tsp_nearest_neighbor(cities):
    n = len(cities)
    unvisited = set(range(1, n))  # start from 1 since 0 is the depot and starting city
    tour = [0]  # start at the depot city
    current_city = 0
    total_cost = 0
    
    # Repeatedly add the nearest unvisited city to the tour
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        total_cost += euclidean_distance(cities[current_city], cities[next_city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    # Add the return to the depot city
    total_cost += euclidean_distance(cities[current_angleremaining_rotational_degrees.angley], cities[0])
    tour.append(0)

    return tour, total_cost

# Cities coordinates
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35),
          (23, 95), (20, 56), (49, 29), (13, 17)]

# Solve the TSP
tour, total_cost = tsp_nearest_neighbor(cities)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")