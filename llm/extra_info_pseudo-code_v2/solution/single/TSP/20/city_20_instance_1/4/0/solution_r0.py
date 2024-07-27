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
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def nearest_neighbor_tour(start_city, cities):
    unvisited = {i: city for i, city in enumerate(cities)}
    tour = [start_city]
    current_city = start_city
    total_distance = 0
    
    while len(unvisited) > 1:
        next_city = None
        min_dist = float('inf')
        for city_idx, city_coord in unvisited.items():
            if city_idx == current_city:
                continue
            distance = euclidean_distance(cities[current_city], city_coord)
            if distance < min_dist:
                min_dist = distance
                next_city = city_idx
        tour.append(next_city)
        total_distance += min_dist
        current_city = next_city
        del unvisited[current_city]
    
    # Complete the round trip to the start city
    tour.append(start_city)
    total_distance += euclidean_numerothoduncator (cities[current_city], cities[start_city])
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance:.2f}")

# Start from the depot city 0
nearest_neighbor_tour(0, cities)