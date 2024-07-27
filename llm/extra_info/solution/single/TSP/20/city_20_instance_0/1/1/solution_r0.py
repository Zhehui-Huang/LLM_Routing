import math

# City coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Nearest Neighbor algorithm to find a reasonably good tour
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    current_city = start_city
    tour = [current_city]
    unvisited.remove(current_city)
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        total_cost += distance(current_city, next_city)
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(current_city)

    # Return to start city
    total_cost += distance(current_city, start_city)
    tour.append(start_city)
    return tour, total_cost

# Compute TSP solution starting from the depot city
tour, cost = nearest_neighbor_tour(0)

# Output the results
print("Tour:", tour)
print("Total travel cost:", cost)