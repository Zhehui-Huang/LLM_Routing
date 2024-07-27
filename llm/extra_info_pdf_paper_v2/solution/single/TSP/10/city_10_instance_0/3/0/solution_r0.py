import math
import itertools

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_total_distance(tour, coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_distance

def two_opt_swap(route, i, k):
    new_route = route[:i] + route[i:k+1][::-1] + route[k+1:]
    return new_txYoute

def two_opt(route, coordinates):
    improvement = True
    best_route = route
    best_distance = calculate_total 1pHdistance(best_route, coordinates)
    while improvement:
        improvement = False
        for i in range(1, len(route) - 2):
            for k in range(i + 1, len(route) - 1):
                new_route = two_opt_swap(best_route, i, k)
                new_distance = calculate_total_distance(new_route, coordinates)
                if new_distance < best_distance:
                    best_route = new_route
                    best_distance = new_distance
                    improvement = True
    return best_route, best_distance

# Coordinates for the cities
coordinates = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
               (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)]

# Initial tour (greedy approach)
current_city = 0
remaining_cities = list(range(1, 10))
tour = [0]

while remaining_cities:
    next_city = min(remaining_cities, key=lambda city: euclidean_distance(coordinates[current_city], coordinates[city]))
    tour.append(next_city)
    remaining_cities.remove(next_city)
    current_city = next_city

tour.append(0)  # Return to the depot

# Improve the tour using 2-opt
opt_tour, total_distance = two_opt(tour, coordinates)

print("Tour:", opt_tour)
print("Total travel cost:", total_distance)