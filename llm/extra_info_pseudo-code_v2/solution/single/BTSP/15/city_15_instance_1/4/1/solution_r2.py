import math

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Greedy approach to construct a tour starting and ending at the depot
def construct_tour(cities):
    n = len(cities)
    unvisited = [i for i in range(1, n)]  # Start tour at the depot, rest are unvisited
    tour = [0]  # Start at depot city 0
    current_city = 0

    # Construct the tour by selecting the nearest unvisited city each step
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(0)  # Return to the depot at the end
    return tour

# Compute the total and the maximum distance of the tour
def tour_distances(tour, cities):
    total_distance = 0
    max_distance = 0

    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist

    return total_distance, max_distance

# Define the city coordinates (index corresponds to city number)
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Construct the tour and calculate distances
tour = construct_tour(cities)
total_travel_cost, max_distance = tour_distances(tour, cities)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_code:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")