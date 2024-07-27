import math

# Coordinates of the cities including the depot city
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
          (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
          (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function that implements the nearest neighbor heuristic for TSP
def nearest_neighbor_tsp(start_city, cities):
    num_cities = len(cities)
    unvisited = set(range(num_cities))
    tour = [start_city]
    unvisited.remove(start_city)
    
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # returning to the depot city
    return tour

# Function to calculate the total travel cost of the tour
def calculate_total_cost(tour):
    total_cost = sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    return total_cost

# Solve the TSP problem
tour = nearest_neighbor_tsp(0, cities)
total_cost = calculate_total_cost(tour)

# Prepare the output
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")