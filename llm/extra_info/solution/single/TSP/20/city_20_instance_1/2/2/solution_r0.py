import math

# Coordinates for the cities including the depot city
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Number of cities
num_cities = len(cities)

# Helper function to calculate the Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Nearest neighbor algorithm
def nearest_neighbor_tour(start_city):
    tour = [start_city]
    unvisited = set(range(num_cities))
    unvisited.remove(start_city)

    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
        
    # Return to depot city
    tour.append(start_city)
    return tour

# Get the tour
tour = nearest_neighbor_tour(0)

# Calculate the total cost of the tour
total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output the tour and the total travel cost
print("Tour:", tour)
print("Total travel cost:", total_cost)