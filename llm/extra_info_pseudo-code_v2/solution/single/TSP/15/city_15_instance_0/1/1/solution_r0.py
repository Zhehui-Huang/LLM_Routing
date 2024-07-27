import math

# City coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), 
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate initial naive tour (simple nearest neighbour heuristic)
def initial_tour(cities):
    unvisited = set(range(1, len(cities)))
    tour = [0]  # start at the depot
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(0)  # return to depot
    return tour

# Calculate total tour cost
def tour_cost(tour, cities):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance(cities[tour[i-1]], cities[tour[i]])
    return total_cost

# Placeholder for potential implementation of full Lin-Kernighan, using initial tour for now
def lin_kernighan(cities):
    tour = initial_tour(cities)
    return tour, tour_cost(tour, cities)

# Solve the problem
optimal_tour, total_cost = lin_kernighan(cities)

# Output
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")