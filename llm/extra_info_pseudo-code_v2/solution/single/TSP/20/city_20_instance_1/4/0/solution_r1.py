import math

# Input Data
cities = [
    (14, 77),  # Depot City 0
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9),   # City 19
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor_tour(start_city, cities):
    unvisited = {i: city for i, city in enumerate(cities) if i != start_city}
    tour = [start_city]
    current_city = start_city
    total_cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        total_cost += euclidean_distance(cities[current_city], cities[next_city])
        tour.append(next_city)
        current_city = next_city
        del unvisited[next_city]
    
    total_cost += euclidean_distance(countries[current_city], cities[start_city])
    tour.append(start_city)
    
    return tour, total_cost

tour, total_cost = nearest_neighbor_tour(0, cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")