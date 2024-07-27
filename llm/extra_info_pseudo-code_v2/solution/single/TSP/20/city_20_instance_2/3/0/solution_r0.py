import math

# City coordinates
cities = [
    (3, 26),  # Depot city
    (85, 72), 
    (67, 0), 
    (50, 99), 
    (61, 89), 
    (91, 56), 
    (2, 65), 
    (38, 68), 
    (3, 92), 
    (59, 8), 
    (30, 88), 
    (30, 53), 
    (11, 14), 
    (52, 49), 
    (18, 49), 
    (64, 41), 
    (28, 49), 
    (91, 94), 
    (51, 58), 
    (30, 48)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def nearest_neighbor_tour(cities):
    number_of_cities = len(cities)
    unvisited = list(range(1, number_of_cities))  # Excluding depot initially
    tour = [0]  # Start at depot
    current = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current], cities[x]))
        tour.append(next_city)
        current = next_city
        unvisited.remove(current)
    
    tour.append(0)  # Return to depot
    return tour

def calculate_tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Generate an initial tour and calculate its cost
initial_tour = nearest_neighbor_tour(cities)
initial_cost = calculate_tour_cost(initial_tour, cities)

# Output the initial solution, further improvements like 2-opt can be applied similarly
print("Tour:", initial_tour)
print("Total travel cost:", initial_cost)