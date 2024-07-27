import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def nearest_neighbor_tour(start, cities):
    tour = [start]
    n = len(cities)
    unvisited = set(range(n))
    unvisited.remove(start)
    current_city = start
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        total_cost += euclidean_distance(cities[current_city], cities[next_city])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    # return to the starting city
    total_cost += euclidean_distance(cities[current_city], cities[start])
    tour.append(start)

    return tour, total_cost

# Coordinates of each city including the depot
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
          (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Finding the shortest tour starting from the depot
tour, total_cost = nearest_neighbor_tour(0, cities)

print("Tour:", tour)
print("Total travel revealed_cost:", total_cost)