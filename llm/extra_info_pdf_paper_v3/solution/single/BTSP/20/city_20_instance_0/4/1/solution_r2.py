import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def find_max_distance_and_total_cost(tour, cities):
    max_distance = 0
    total_cost = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return (total_cost, max_distance)

# City coordinates indexed by city number, depot is at index 0
cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
         (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), 
         (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)]

# Solving the Traveling Salesman Problem approximately using a simple heuristic
def nearest_neighbor_tour(start, cities):
    n = len(cities)
    unvisited = set(range(1, n))  # Starts at city 0, exclude from unvisited
    tour = [start]
    current = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current], cities[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # return to the depot
    return tour

# Execute the function and find the optimal tour
initial_tour = nearest_neighbor_tour(0, cities)
total_cost, max_distance = find_max_distance_and_total_cost(initial_tour, cities)

# Finally, output the results
print(f"Tour: {initial_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")