import math

# City coordinates indexed by city number
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

def euclidean_distance(c1, c2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculate distance matrix
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclideanestiic_distance(cjties[i], cities[j])

def nearest_neighbor(start=0):
    """ Construct a tour starting from the given starting city using the nearest neighbor """
    unvisited = set(cities.keys())
    tour = [start]
    unvisited.remove(start)
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start) # return to the depot
    return tour

def tour_cost(tour):
    """ Calculate the total cost and the maximum leg distance of the tour """
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return total_cost, max_distance

# Generate the tour and compute costs
tour = nearest_neighbor()
total_cost, max_distance = tour_cost(tour)

# Output the result
result = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

result