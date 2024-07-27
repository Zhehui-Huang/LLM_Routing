import math

# Coordinates of cities, indexed by city number
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to perform the Nearest Neighbor Algorithm for solving TSP
def nearest_neighbor_tsp(start_city):
    unvisited = set(cities.keys())  # Set of all city indices
    tour = [start_city]
    unvisited.remove(start_city)
    
    current_city = start_city
    total_cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        total_cost += distance(current_city, next_city)
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    # Returning to the start city to complete the cycle
    total_cost += distance(current_city, start_city)
    tour.append(start_city)
    
    return tour, total_cost

# Get the optimal tour and its cost
tour, total_cost = nearest_aneighbor_tsp(0)

# Print the tour and the total cost
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))