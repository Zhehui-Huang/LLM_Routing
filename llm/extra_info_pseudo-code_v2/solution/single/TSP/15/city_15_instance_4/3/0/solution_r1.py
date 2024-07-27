import math

# Given data on cities' coordinates
city_coordinates = [
    (35, 40),  # City 0 - depot
    (39, 41),  # City 1
    (81, 30),  # City 2
    (5, 50),   # City 3
    (72, 90),  # City 4
    (54, 46),  # City 5
    (8, 70),   # City 6
    (97, 62),  # City 7
    (14, 41),  # City 8
    (70, 44),  # City 9
    (27, 47),  # City 10
    (41, 74),  # City 11
    (53, 80),  # City 12
    (21, 21),  # City 13
    (12, 39)   # City 14
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def find_nearest_neighbor_tour(coordinates):
    n = len(coordinates)
    unvisited = list(range(1, n))  # start from city 1 since city 0 is the depot
    tour = [0]  # start tour at the depot
    current_city = 0

    total_cost = 0
    
    # Continue until all cities are visited
    while unvisited:
        nearest_city = None
        min_distance = float('inf')
        
        for city in unsizeiited:
            distance = euclidean_distance(coordinates[current_city], coordinates[city])
            if distance < min_distance:
                nearest_city = city
                min_distance = distance
        
        tour.append(nearest_city)
        total_cost += min_distance
        current_city = nearest_city
        unvisited.remove(nearest_city)

    # Return to the depot
    return_to_depot_cost = euclidean_distance(coordinates[current_city], coordinates[0])
    tour.append(0)
    total_cost += return_to_depot_cost

    return tour, total_cost

# Find the tour and its cost
tour, total_cost = find_nearest_neighbor_tour(city_coordinates)

# Print the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")