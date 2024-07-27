import math

# Define city locations
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 
    11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 
    16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(from_city, to_city):
    x1, y1 = cities[from_city]
    x2, y2 = cities[to_city]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Find the path to minimize the max distance between consecutive cities in the tour
def minimize_max_distance_tour():
    n = len(cities)
    unvisited = set(cities.keys())
    unvisited.remove(0)
    tour = [0]
    max_distance = 0
    
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current, city))
        distance = euclidean_distance(current, next_city)
        max_distance = max(max_distance, distance)
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    
    # Return to the depot city
    tour.append(0)
    final_distance = euclidean_distance(current, 0)
    max_distance = max(max_distance, final_distance)
    total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

# Execute the function and print results
tour, total_cost, max_distance = minimize_max_distance_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")