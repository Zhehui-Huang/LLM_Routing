import math

# Coordinates of the cities
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tour(start_city):
    tour = [start_city]
    unvisited = set(range(len(coordinates)))
    unvisited.remove(start_city)
    current = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(coordinates[current], coordinates[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start_city)  # Return to start
    return tour

def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if total_travel_cost(new_route) < total_travel_cost(best):
                    best = new_route
                    improved = True
        route = best
    return best

def total_travel_cost(tour):
    total_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    return total_cost

# Computing shortest tour
initial_tour = nearest_neighbor_tour(0)
optimized_tour = two_opt(initial_tour)
total_cost = total_travel_cost(optimized_tour)

print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)