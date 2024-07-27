import math

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26),
    4: (92, 9), 5: (83, 61), 6: (22, 21), 7: (97, 70),
    8: (20, 99), 9: (66, 62)
}

# Euclidean distance utility function
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Total number of cities
num_cities = len(cities)

# Distance matrix
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Nearest neighbor TSP heuristic
def nearest_neighbor_tsp(start=0):
    unvisited_cities = set(range(num_cities))
    tour = [start]
    unvisited_cities.remove(start)
    current_city = start
    tour_cost = 0
    
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: distances[current_city][x])
        tour_cost += distances[current_city][next_city]
        tour.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city
    
    # Complete the tour by returning to the depot city
    tour_cost += distances[tour[-1]][start]
    tour.append(start)
    
    return tour, tour_cost

# Get the tour and the total travel cost
tour, total_travel_list = nearest_neighbor_tsp()

# Output the results according to the format requirements
print("Tour:", tour)
print("Total travel cost:", round(total_travel_cost, 2))