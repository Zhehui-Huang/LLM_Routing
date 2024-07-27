import math

# Coordinates of the cities
cities = [
    (8, 11),  (40, 6),  (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Utility function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Finding an optimal tour with simple heuristic
def optimal_tour_heuristic():
    import heapq
    
    num_cities = len(cities)
    remaining_cities = list(range(1, num_cities))  # Start from 1 since 0 is the depot
    tour = [0]  # Start at the depot
    total_cost = 0.0
    
    # Build the tour by always choosing the nearest unvisited city
    while remaining_cities:
        last = tour[-1]
        nearest = min(remaining_cities, key=lambda city: distance(last, city))
        next_distance = distance(last, nearest)
        total_cost += next_distance
        tour.append(nearest)
        remaining_cities.remove(nearest)

    # Close the tour by returning to the depot
    tour.append(0)
    last_to_depot_distance = distance(tour[-2], 0)
    total_cost += last_to_depot_distance
    
    # Calculate the maximum distance between consecutive cities in the tour
    max_distance = max(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

# Execute the heuristic to find the tour
tour, total_cost, max_distance = optimal_tour_heuristic()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")