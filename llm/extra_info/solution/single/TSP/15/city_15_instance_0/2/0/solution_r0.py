import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates for the cities (index is the city number)
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

def find_tsp_tour(cities):
    # Start tour at the depot city
    current_city = 0
    tour = [current_city]
    total_cost = 0
    unvisited = set(cities.keys())
    unvisited.remove(current_city)

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        total_cost += euclidean_distance(cities[current_city], cities[next_city])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(current_city)

    # Return to the depot from the last city
    total_cost += euclidean_distance(cities[current_city], cities[0])
    tour.append(0)

    return tour, total_cost

tour, total_cost = find_tsp_tour(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)