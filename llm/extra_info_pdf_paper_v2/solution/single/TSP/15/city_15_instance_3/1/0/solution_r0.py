import math
import itertools

# Coordinates of the cities
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate initial tour using Nearest Neighbor algorithm
def nearest_neighbor_tour(start_city):
    tour = [start_city]
    unvisited_cities = set(range(len(coordinates)))
    unvisited_cities.remove(start_city)
    
    current_city = start_city
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: euclidean_distance(coordinates[current_city], coordinates[city]))
        tour.append(next_city)
        unvisited_cities.remove(next_city)
        current_test_city = current_city
        current_city = next_city
        
    tour.append(start_city)  # Return to the depot city
    return tour

# 2-opt Swap function
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue
                if (euclidean_distance(coordinates[tour[i - 1]], coordinates[tour[i]]) + 
                    euclidean_distance(coordinates[tour[j]], coordinates[tour[j + 1]])) > \
                   (euclidean_distance(coordinates[tour[i - 1]], coordinates[tour[j]]) + 
                    euclidean_distance(coordinates[tour[i]], coordinates[tour[j + 1]])):
                    tour[i:j] = reversed(tour[i:j])
                    improved = True
                    
    return tour

# Compute the total cost of the tour
def total_travel_cost(tour):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

# Obtain the initial tour and optimize it
initial_tour = nearest_neighbor_tour(0)
optimized_tour = two_opt(initial_tour)
total_cost = total_travel_cost(optimized_tour)

print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost}")