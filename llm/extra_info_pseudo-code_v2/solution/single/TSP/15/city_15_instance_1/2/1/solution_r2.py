import math

# Coordinates for each city
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57),
    6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Estimate an initial feasible solution using nearest neighbor heuristic
def nearest_neighbor_tour(start):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start)  # return to the depot
    return tour

# Calculate the total travel cost of a tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate initial tour using nearest neighbor and calculate its cost
initial_tour = nearest_neighbor_tour(0)
initial_cost = calculate_tour_cost(initial_tour)

# Output the tour and cost
print("Tour:", initial_tour)
print("Total travel cost:", initial_cost)