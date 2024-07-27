import math

# Locations of cities
cities = [
    (9, 93),   # City 0: Depot
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Function to find the shortest tour using the nearest neighbor heuristic
def nearest_neighbor_tour(cities):
    n = len(cities)
    unvisited = list(range(1, n))  # Start from city 0 and exclude the depot initially
    tour = [0]  # Starting point - depot
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(0)  # Return to depot
    return tour

# Function to calculate the total cost of the tour
def tour_cost(tour, cities):
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Get the tour and calculate its cost
tour = nearest_neighbor_tour(cities)
cost = tour_cost(tour, cities)

# Output results
print("Tour:", tour)
print("Total travel cost:", cost)