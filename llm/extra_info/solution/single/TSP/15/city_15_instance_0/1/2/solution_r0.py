import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y1 - y2)**2)

def nearest_neighbor_tour(cities, start_city):
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        nearest_city = None
        min_distance = float('inf')
        for city in unvisited:
            distance = calculate_distance(cities[current_city][0], cities[current_city][1],
                                          cities[city][0], cities[city][1])
            if distance < min_distance:
                min_distance = distance
                nearest_city = city
        tour.append(nearest_city)
        current_city = nearest_city
        unvisited.remove(nearest_city)
      
    tour.append(start_city)  # Return to the starting city
    return tour

def calculate_tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]][0], cities[tour[i]][1],
                                         cities[tour[i+1]][0], cities[tour[i+1]][1])
    return total_cost

# Define the cities
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

tour = nearest_neighbor_tour(cities, 0)
total_cost = calculate_tour_cost(tour, cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)