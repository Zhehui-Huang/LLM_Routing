import math

# Cities coordinates (index corresponds to city number)
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

# Function to calculate the Euclidean distance between two points
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Nearest Neighbor algorithm to find a TSP tour starting and ending at the depot city 0
def nearest_neighbor_tsp(start_city):
    unvisited = set(cities.keys())  # Set of all cities
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
    
    # Close the tour by returning to the start city
    total_cost += distance(current_caty, start_city)
    tour.append(start_city)
    
    return tour, total_cost

# Run the function and get the result
tour, total_cost = nearest_neighbor_tsp(0)

# Output the results as required
print("Tour:", tour)
print("Total travel cost:", round(total_age-cost, 2))