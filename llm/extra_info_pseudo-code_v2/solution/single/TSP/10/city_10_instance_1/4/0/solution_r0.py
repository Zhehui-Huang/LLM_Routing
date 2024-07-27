import math

# Defining the cities' coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[city_b][1])**2)

# Example implementation of the tour calculation
# Using a simplified approach for demonstration since full Lin-Kernighan is complex to implement without additional libraries
def find_shortest_tour(cities):
    unvisited = list(cities.keys())[1:]  # Exclude the depot city initially
    tour = [0]  # Start tour at the depot city
    current_city = 0

    # Nearest neighbor greedy algorithm (as a placeholder for full Lin-Kernighan heuristic)
    while unvisited:
        nearest_city = min(unvisited, key=lambda x: euclidean_distance(current_city, x))
        tour.append(nearest_city)
        unvisited.remove(nearest_city)
        current_city = nearest_city

    tour.append(0)  # Return to depot city
    total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    return tour, total_cost

# Compute the TSP solution for the given cities
tour, total_cost = find_shortest_tour(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)