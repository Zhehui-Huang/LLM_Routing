import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 
    4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
    8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82), 
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def find_shortest_tour(cities):
    remaining_cities = list(cities.keys())
    tour = [0]  # Start at the depot city
    current_city = 0
    total_cost = 0
    
    while len(remaining_cities) > 1:
        next_city = min((c for c in remaining_cities if c != current_city), key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        total_cost += euclidean_distance(cities[current_city], cities[next_city])
        tour.append(next_city)
        remaining_cities.remove(current_city)
        current_city = next_city
    
    # Return to the depot city
    total_cost += euclidean_distance(cities[current_city], cities[0])
    tour.append(0)

    return tour, total_cost

tour, total_cost = find_shortest_tour(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)