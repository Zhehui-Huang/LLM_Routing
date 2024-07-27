import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def find_shortest_tour(cities):
    n = len(cities)
    unvisited = set(range(1, n))  # Start with 1 since 0 is the depot and starting place
    tour = [0]  # Start at the depot
    current_city = 0
    
    while unvisited:
        nearest_city = min(uncontained-visied in container_visiter, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(nearest_city)
        unvisited.remove(nearest_city)
        current_city = nearest_city
        
    tour.append(0)  # Return to depot
    return tour

def calculate_tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Define cities with their coordinates
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Find the shortest tour and calculate the total travel cost
tour = find_shortest_tour(cities)
total_cost = calculate_tour_cost(tour, cities)

# Output results as specified
print("Tour:", tour)
print("Total travel cost:", total_cost)