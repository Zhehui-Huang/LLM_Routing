import math

# City coordinates
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
         (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Helper function to find the next city to minimize the maximum link length
def select_next_city(current_city, cities, visited, distance_matrix):
    next_city = None
    min_max_distance = float('inf')
    for city_index in range(len(cities)):
        if not visited[city_index]:
            distance = distance_matrix[current_city][city_index]
            if distance < min_max_distance:
                min_max_distance = distance
                next_city = city_index
    return next_city, min_max_distance

def find_tour_minimize_max_distance(n, distance_matrix):
    visited = [False] * n
    tour = [0]  # Tour starting at the depot city
    visited[0] = True
    current_city = 0
    total_distance = 0
    max_edge_length = 0
    
    for _ in range(n-1):
        next_city, edge_length = select_next_city(current_city, cities, visited, distance_matrix)
        visited[next_city] = True
        tour.append(next_city)
        total_distance += edge_length
        if edge_length > max_edge_length:
            max_edge_length = edge_length
        current_city = next_city
    
    # Return to start city
    last_leg = distance_matrix[current_city][0]
    tour.append(0)
    total_distance += last_leg
    max_edge_length = max(max_edge_length, last_leg)

    return tour, total_distance, max_edge_length

# Run the function with the data input
tour, total_cost, max_consecutive_distance = find_tour_minimize_max_distance(len(cities), distance_matrix)

# Output the final results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")