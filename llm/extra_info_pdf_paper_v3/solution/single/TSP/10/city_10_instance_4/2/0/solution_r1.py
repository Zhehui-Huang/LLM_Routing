import math

# Provided city coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Define a function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initialize the tour starting at the depot, city 0
def nearest_neighbor_tsp(cities):
    n = len(cities)
    unvisited = set(range(1, n))  # Start from 1 to exclude the depot
    tour = [0]
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    # Return to the depot
    tour.append(0)
    return tour

# Calculate the total distance of the tour
def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

# Get the TSP tour and total distance
tour = nearest_neighbor_tsp(cities)
total_distance = calculate_total_distance(tour, cities)

# Display results
print("Tour:", tour)
print("Total travel cost:", round(total_distance, 2))